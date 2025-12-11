class Member:
    VALID_TYPES = {'student', 'faculty', 'community'}
    BASE_CLASS_FEE = 10.0
    
    def __init__(self, member_id, name, membership_type):
        self._id = member_id
        self._name = name
        self._membership_type = (membership_type if membership_type in self.VALID_TYPES 
                               else 'community')
        self._active = True
        self._balance = 0.0
    
    @property
    def id(self): return self._id
    
    @property
    def name(self): return self._name
    
    @property
    def membership_type(self): return self._membership_type
    
    @property
    def active(self): return self._active
    
    @property
    def balance(self): return self._balance
    
    def deactivate(self):
        if self._active:
            self._active = False
            return True
        return False
    
    def add_charge(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def apply_payment(self, amount):
        if amount > 0:
            self._balance -= amount
            return True
        return False
    
    def calculate_class_fee(self):
        if self._membership_type == 'student':
            return self.BASE_CLASS_FEE * 0.5
        elif self._membership_type == 'faculty':
            return self.BASE_CLASS_FEE * 0.75
        return self.BASE_CLASS_FEE
    
    def __str__(self):
        status = 'Active' if self._active else 'Inactive'
        return f"[{self._id}] {self._name} ({self._membership_type}, {status}) Balance: ${self._balance:.2f}"
