class FitnessClass:
    VALID_DIFFICULTIES = {'beginner', 'intermediate', 'advanced'}
    
    def __init__(self, class_id, name, difficulty, capacity):
        self._id = class_id
        self._name = name
        self._difficulty = (difficulty if difficulty in self.VALID_DIFFICULTIES 
                          else 'beginner')
        self._capacity = max(1, capacity)
        self._enrolled_members = []
    
    @property
    def id(self): return self._id
    
    @property
    def name(self): return self._name
    
    @property
    def difficulty(self): return self._difficulty
    
    @property
    def capacity(self): return self._capacity
    
    @property
    def enrollment_count(self): return len(self._enrolled_members)
    
    def enroll(self, member):
        if not member.active:
            return False, "Cannot enroll inactive member"
        if any(m.id == member.id for m in self._enrolled_members):
            return False, "Member already enrolled"
        if self.enrollment_count >= self._capacity:
            return False, "Class is full"
        self._enrolled_members.append(member)
        return True, f"Enrolled {member.name} in {self._name}"
    
    def get_roster(self):
        return self._enrolled_members[:]
    
    def __str__(self):
        return f"[{self._id}] {self._name} ({self._difficulty}, capacity {self._capacity}, enrolled {self.enrollment_count})"
