from models.member import Member
from models.fitness_class import FitnessClass
from models.trainer import Trainer

class FitnessCenter:
    def __init__(self):
        self._members = []
        self._classes = []
        self._trainers = []
        self._next_member_id = 1
        self._next_class_id = 1
        self._next_trainer_id = 1
    
    # === STATIC UTILITY METHODS ===
    @staticmethod
    def read_int(prompt, min_value=None, max_value=None):
        while True:
            try:
                value = int(input(prompt))
                if min_value is not None and value < min_value:
                    print(f'Please enter a value >= {min_value}')
                    continue
                if max_value is not None and value > max_value:
                    print(f'Please enter a value <= {max_value}')
                    continue
                return value
            except ValueError:
                print('Please enter a valid integer.')

    @staticmethod
    def read_nonempty(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print('Input cannot be empty.')

    @staticmethod
    def pause():
        input('\nPress Enter to continue...')

    # === MEMBER OPERATIONS ===
    def add_member(self, name, membership_type):
        member = Member(self._next_member_id, name, membership_type)
        self._members.append(member)
        print(f'Member added with id {self._next_member_id}')
        self._next_member_id += 1
        return member
    
    def find_member(self, member_id):
        for member in self._members:
            if member.id == member_id:
                return member
        return None
    
    def list_members(self, show_details=True):
        print('\n=== Members ===')
        if not self._members:
            print('No members found.')
            return
        for member in self._members:
            if show_details:
                print(member)
            else:
                print(f"[{member.id}] {member.name}")
        print()
    
    def deactivate_member(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print('Member not found.')
            return False
        if member.deactivate():
            print(f'Member {member.name} is now inactive.')
            return True
        print('Member is already inactive.')
        return False
    
    def add_charge_to_member(self, member_id, amount):
        member = self.find_member(member_id)
        if not member:
            print('Member not found.')
            return False
        if member.add_charge(amount):
            print(f"Added ${amount:.2f} to {member.name}'s balance.")
            return True
        print('Invalid amount.')
        return False
    
    def apply_payment(self, member_id, amount):
        member = self.find_member(member_id)
        if not member:
            print('Member not found.')
            return False
        if member.apply_payment(amount):
            print(f'Recorded payment of ${amount:.2f} from {member.name}.')
            return True
        print('Invalid amount.')
        return False
    
    # === CLASS OPERATIONS ===
    def create_class(self, name, difficulty, capacity):
        cls = FitnessClass(self._next_class_id, name, difficulty, capacity)
        self._classes.append(cls)
        print(f'Fitness class created with id {self._next_class_id}')
        self._next_class_id += 1
        return cls
    
    def find_class(self, class_id):
        for cls in self._classes:
            if cls.id == class_id:
                return cls
        return None
    
    def list_classes(self, show_enrollment=True):
        print('\n=== Fitness Classes ===')
        if not self._classes:
            print('No classes found.')
            return
        for cls in self._classes:
            if show_enrollment:
                print(cls)
            else:
                print(f"[{cls.id}] {cls.name}")
        print()
    
    def enroll_member_in_class(self, member_id, class_id):
        member = self.find_member(member_id)
        if not member:
            print('Member not found.')
            return False
        
        cls = self.find_class(class_id)
        if not cls:
            print('Class not found.')
            return False
        
        success, message = cls.enroll(member)
        print(message)
        if success:
            fee = member.calculate_class_fee()
            member.add_charge(fee)
            print(f'Charged ${fee:.2f} for class (base ${Member.BASE_CLASS_FEE:.2f}, type: {member.membership_type}).')
        return success
    
    def list_class_roster(self, class_id):
        cls = self.find_class(class_id)
        if not cls:
            print('Class not found.')
            return
        print(f'\nRoster for {cls.name}:')
        roster = cls.get_roster()
        if not roster:
            print('No members enrolled.')
            return
        for member in roster:
            print(f'- {member.name} ({member.membership_type})')
    
    # === TRAINER OPERATIONS ===
    def add_trainer(self, name, specialty):
        trainer = Trainer(self._next_trainer_id, name, specialty)
        self._trainers.append(trainer)
        print(f'Trainer added with id {self._next_trainer_id}')
        self._next_trainer_id += 1
        return trainer
    
    def find_trainer(self, trainer_id):
        for trainer in self._trainers:
            if trainer.id == trainer_id:
                return trainer
        return None
    
    def list_trainers(self, show_schedule=True):
        print('\n=== Trainers ===')
        if not self._trainers:
            print('No trainers found.')
            return
        for trainer in self._trainers:
            if show_schedule:
                print(trainer)
            else:
                print(f"[{trainer.id}] {trainer.name}")
        print()
    
    def update_trainer_schedule(self, trainer_id):
        trainer = self.find_trainer(trainer_id)
        if not trainer:
            print('Trainer not found.')
            return False
        
        print('Current schedule:')
        for slot in trainer.schedule:
            print(f'- {slot}')
        
        print('1. Replace schedule')
        print('2. Add to schedule')
        choice = self.read_int('Choice: ', 1, 2)
        
        if choice == 1:
            trainer.replace_schedule()
            print('Enter new availability (blank to finish):')
            while True:
                slot = input('Availability: ').strip()
                if not slot:
                    break
                trainer.add_availability(slot)
        else:
            print('Enter additional availability (blank to finish):')
            while True:
                slot = input('Availability: ').strip()
                if not slot:
                    break
                trainer.add_availability(slot)
        
        print('Updated schedule:')
        for slot in trainer.schedule:
            print(f'- {slot}')
        return True
    
    # === REPORTING ===
    def show_summary_report(self):
        print('\n=== Summary Report ===')
        total_members = len(self._members)
        active_members = sum(1 for m in self._members if m.active)
        total_balance = sum(m.balance for m in self._members)
        
        print(f'Total members: {total_members}')
        print(f'Active members: {active_members}')
        print(f'Total outstanding balance: ${total_balance:.2f}')
        
        print('\nClasses:')
        for cls in self._classes:
            print(f'- {cls.name} ({cls.difficulty}): {cls.enrollment_count}/{cls.capacity} enrolled')
        
        print('\nTrainers:')
        for trainer in self._trainers:
            print(f'- {trainer.name} ({trainer.specialty})')
        print()
