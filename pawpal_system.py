#backend logic layer where all classes live

class Owner:
    """Represents a pet owner with constraints and preferences."""
    
    def __init__(self, name: str, age: int, special_needs: list = None, constraints: dict = None):
        self.name = name
        self.age = age
        self.special_needs = special_needs if special_needs else []
        self.constraints = constraints if constraints else {}
    
    def get_name(self) -> str:
        """Return the owner's name."""
        pass
    
    def get_age(self) -> int:
        """Return the owner's age."""
        pass
    
    def get_special_needs(self) -> list:
        """Return the owner's special needs."""
        pass
    
    def get_constraints(self) -> dict:
        """Return the owner's constraints for the plan."""
        pass
    
    def set_constraints(self, constraints: dict) -> None:
        """Set constraints for the plan."""
        pass


class Pet:
    """Represents a pet that receives a daily care plan."""
    
    def __init__(self, name: str, age: int, breed: str, special_needs: list = None):
        self.name = name
        self.age = age
        self.breed = breed
        self.special_needs = special_needs if special_needs else []
        self.daily_plan = None
    
    def get_name(self) -> str:
        """Return the pet's name."""
        pass
    
    def get_age(self) -> int:
        """Return the pet's age."""
        pass
    
    def get_breed(self) -> str:
        """Return the pet's breed."""
        pass
    
    def get_special_needs(self) -> list:
        """Return the pet's special needs."""
        pass
    
    def get_daily_plan(self):
        """Return the pet's current daily plan."""
        pass
    
    def set_daily_plan(self, plan) -> None:
        """Set the daily plan for the pet."""
        pass


class Task:
    """Represents a single pet care task."""
    
    def __init__(self, task_id: str, name: str, task_type: str, duration: int, priority: int, pet_id: str):
        self.task_id = task_id
        self.name = name
        self.task_type = task_type  # e.g., 'walk', 'feeding', 'medicine', 'grooming'
        self.duration = duration
        self.priority = priority
        self.pet_id = pet_id
    
    def get_id(self) -> str:
        """Return the task ID."""
        pass
    
    def get_name(self) -> str:
        """Return the task name."""
        pass
    
    def get_task_type(self) -> str:
        """Return the task type."""
        pass
    
    def get_duration(self) -> int:
        """Return the task duration in minutes."""
        pass
    
    def get_priority(self) -> int:
        """Return the task priority level."""
        pass
    
    def get_pet_id(self) -> str:
        """Return the pet ID associated with this task."""
        pass


class Scheduler:
    """Manages pet care tasks and generates daily plans."""
    
    def __init__(self, owner: Owner, pet: Pet):
        self.owner = owner
        self.pet = pet
        self.tasks = []
        self.daily_plan = []
    
    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        pass
    
    def remove_task(self, task_id: str) -> None:
        """Remove a task from the scheduler by ID."""
        pass
    
    def generate_daily_plan(self, date) -> list:
        """Generate a daily plan for the pet based on owner and pet constraints."""
        pass
    
    def display_plan(self) -> None:
        """Display the current daily plan."""
        pass
    
    def edit_plan(self, task_id: str, updates: dict) -> None:
        """Edit a task in the plan with provided updates."""
        pass
    
    def _prioritize_tasks(self) -> list:
        """Internal method to prioritize tasks based on constraints and preferences."""
        pass 

