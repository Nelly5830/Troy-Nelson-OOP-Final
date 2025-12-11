import sys
from fitness_center import FitnessCenter

def member_menu(center):
    while True:
        print('\n=== Member Menu ===')
        print('1. Add member')
        print('2. List members')
        print('3. Deactivate member')
        print('4. Add charge to member')
        print('5. Record payment from member')
        print('6. Back to main menu')
        
        choice = center.read_int('Choice: ', 1, 6)  
        if choice == 1:
            name = center.read_nonempty('Name: ')
            print('Membership types: student, faculty, community')
            mtype = input('Membership type: ').strip().lower()
            center.add_member(name, mtype)
        elif choice == 2:
            center.list_members()
        elif choice == 3:
            center.list_members(show_details=False)
            mid = center.read_int('Enter member id to deactivate: ')
            center.deactivate_member(mid)
        elif choice == 4:
            center.list_members(show_details=False)
            mid = center.read_int('Enter member id to charge: ')
            try:
                amount = float(input('Charge amount: $'))
                center.add_charge_to_member(mid, amount)
            except ValueError:
                print('Invalid amount.')
        elif choice == 5:
            center.list_members(show_details=False)
            mid = center.read_int('Enter member id: ')
            try:
                amount = float(input('Payment amount: $'))
                center.apply_payment(mid, amount)
            except ValueError:
                print('Invalid amount.')
        elif choice == 6:
            break
        center.pause()

def classes_menu(center):
    while True:
        print('\n=== Classes Menu ===')
        print('1. Create fitness class')
        print('2. List fitness classes')
        print('3. Enroll member in class')
        print('4. Show class roster')
        print('5. Back to main menu')
        
        choice = center.read_int('Choice: ', 1, 5)
        if choice == 1:
            name = center.read_nonempty('Class name: ')
            difficulty = input('Difficulty (beginner/intermediate/advanced): ').strip().lower()
            capacity = center.read_int('Capacity: ', 1)
            center.create_class(name, difficulty, capacity)
        elif choice == 2:
            center.list_classes()
        elif choice == 3:
            center.list_members(show_details=False)
            mid = center.read_int('Enter member id: ')
            center.list_classes(show_enrollment=False)
            cid = center.read_int('Enter class id: ')
            center.enroll_member_in_class(mid, cid)
        elif choice == 4:
            center.list_classes(show_enrollment=False)
            cid = center.read_int('Enter class id: ')
            center.list_class_roster(cid)
        elif choice == 5:
            break
        center.pause()

def trainer_menu(center):
    while True:
        print('\n=== Trainer Menu ===')
        print('1. Add trainer')
        print('2. List trainers')
        print('3. Update trainer schedule')
        print('4. Back to main menu')
        
        choice = center.read_int('Choice: ', 1, 4)
        if choice == 1:
            name = center.read_nonempty('Trainer name: ')
            specialty = center.read_nonempty('Specialty (e.g., yoga, strength, cardio): ')
            center.add_trainer(name, specialty)
        elif choice == 2:
            center.list_trainers()
        elif choice == 3:
            center.list_trainers(show_schedule=False)
            tid = center.read_int('Enter trainer id: ')
            center.update_trainer_schedule(tid)
        elif choice == 4:
            break
        center.pause()

def main():
    center = FitnessCenter()
    while True:
        print('\n=== Campus Fitness Center Management ===')
        print('1. Manage members')
        print('2. Manage classes')
        print('3. Manage trainers')
        print('4. Show summary report')
        print('5. Exit')
        
        choice = center.read_int('Choice: ', 1, 5)
        if choice == 1:
            member_menu(center)
        elif choice == 2:
            classes_menu(center)
        elif choice == 3:
            trainer_menu(center)
        elif choice == 4:
            center.show_summary_report()
            center.pause()
        elif choice == 5:
            print('Goodbye!')
            sys.exit(0)

if __name__ == '__main__':
    main()
