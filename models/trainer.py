class Trainer:
    def __init__(self, trainer_id, name, specialty):
        self._id = trainer_id
        self._name = name
        self._specialty = specialty
        self._schedule = []
    
    @property
    def id(self): return self._id
    
    @property
    def name(self): return self._name
    
    @property
    def specialty(self): return self._specialty
    
    @property
    def schedule(self): return self._schedule[:]
    
    def add_availability(self, slot):
        slot = slot.strip()
        if slot:
            self._schedule.append(slot)
            return True
        return False
    
    def replace_schedule(self):
        self._schedule.clear()
    
    def get_schedule_str(self):
        return ', '.join(self._schedule) if self._schedule else 'No availability'
    
    def __str__(self):
        return f"[{self._id}] {self._name} - {self._specialty} (Schedule: {self.get_schedule_str()})"
