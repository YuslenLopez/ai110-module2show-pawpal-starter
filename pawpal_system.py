#backend logic layer where all classes live

import uuid
from datetime import datetime, timedelta

class Owner:
    """Manages multiple pets and provides access to all their tasks."""
    
    def __init__(self, name: str, age: int, special_needs: list = None, constraints: dict = None):
        """Initialize an Owner with name, age, special needs, and constraints."""
        self.name = name
        self.age = age
        self.special_needs = special_needs if special_needs else []
        self.constraints = constraints if constraints else {}
        self.pets = {}  # Dictionary to store multiple pets
    
    def get_name(self) -> str:
        """Return the owner's name."""
        return self.name
    
    def get_age(self) -> int:
        """Return the owner's age."""
        return self.age
    
    def get_special_needs(self) -> list:
        """Return the owner's special needs."""
        return self.special_needs
    
    def get_constraints(self) -> dict:
        """Return the owner's constraints for the plan."""
        return self.constraints
    
    def set_constraints(self, constraints: dict) -> None:
        """Set constraints for the plan."""
        self.constraints = constraints
    
    def add_pet(self, pet_id: str, pet) -> None:
        """Add a pet to the owner's collection."""
        self.pets[pet_id] = pet
    
    def remove_pet(self, pet_id: str) -> None:
        """Remove a pet from the owner's collection."""
        if pet_id in self.pets:
            del self.pets[pet_id]
    
    def get_pet(self, pet_id: str):
        """Retrieve a specific pet by ID."""
        return self.pets.get(pet_id)
    
    def get_all_pets(self) -> dict:
        """Return all pets owned by this owner."""
        return self.pets
    
    def get_all_tasks(self) -> list:
        """Get all tasks from all owned pets."""
        all_tasks = []
        for pet in self.pets.values():
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Pet:
    """Stores pet details and a list of tasks."""
    
    def __init__(self, name: str, age: int, breed: str, special_needs: list = None):
        """Initialize a Pet with name, age, breed, and optional special needs."""
        self.name = name
        self.age = age
        self.breed = breed
        self.special_needs = special_needs if special_needs else []
        self.daily_plan = None
        self.tasks = []  # List of tasks for this pet
    
    def get_name(self) -> str:
        """Return the pet's name."""
        return self.name
    
    def get_age(self) -> int:
        """Return the pet's age."""
        return self.age
    
    def get_breed(self) -> str:
        """Return the pet's breed."""
        return self.breed
    
    def get_special_needs(self) -> list:
        """Return the pet's special needs."""
        return self.special_needs
    
    def get_daily_plan(self):
        """Return the pet's current daily plan."""
        return self.daily_plan
    
    def set_daily_plan(self, plan) -> None:
        """Set the daily plan for the pet."""
        self.daily_plan = plan
    
    def add_task(self, task) -> None:
        """Add a task to the pet's task list."""
        self.tasks.append(task)
    
    def remove_task(self, task_id: str) -> None:
        """Remove a task from the pet's task list."""
        self.tasks = [task for task in self.tasks if task.get_id() != task_id]
    
    def get_tasks(self) -> list:
        """Return all tasks for this pet."""
        return self.tasks


class Task:
    """Represents a single activity (description, time, frequency, completion status)."""
    
    def __init__(self, task_id: str, name: str, description: str, task_type: str, time: str, frequency: str, duration: int, priority: int, pet_id: str, day: str = None):
        """Initialize a Task with ID, name, description, type, time, frequency, duration, priority, pet ID, and day.
        
        Args:
            task_type: Recurrence type - 'once', 'daily', or 'weekly'
            day: Day of week (Monday-Sunday), required for weekly tasks, optional for others
            frequency: Legacy parameter kept for compatibility, not used if task_type is provided
        """
        self.task_id = task_id
        self.name = name
        self.description = description  # Detailed description of the activity
        self.task_type = task_type  # e.g., 'once', 'daily', 'weekly' (recurrence type)
        self.time = time  # e.g., '09:00'
        self.frequency = frequency  # e.g., 'daily', 'twice daily', 'weekly' (legacy)
        self.duration = duration  # Duration in minutes
        self.priority = priority
        self.pet_id = pet_id
        self.day = day  # Day of week (Monday-Sunday)
        self.completion_status = False  # Track if task is completed
    
    def get_id(self) -> str:
        """Return the task ID."""
        return self.task_id
    
    def get_name(self) -> str:
        """Return the task name."""
        return self.name
    
    def get_description(self) -> str:
        """Return the task description."""
        return self.description
    
    def get_task_type(self) -> str:
        """Return the task type."""
        return self.task_type
    
    def get_time(self) -> str:
        """Return the scheduled time for the task."""
        return self.time
    
    def get_frequency(self) -> str:
        """Return the frequency of the task."""
        return self.frequency
    
    def get_duration(self) -> int:
        """Return the task duration in minutes."""
        return self.duration
    
    def get_priority(self) -> int:
        """Return the task priority level."""
        return self.priority
    
    def get_pet_id(self) -> str:
        """Return the pet ID associated with this task."""
        return self.pet_id
    
    def get_day(self) -> str:
        """Return the day of week for this task."""
        return self.day
    
    def is_completed(self) -> bool:
        """Return the completion status of the task."""
        return self.completion_status
    
    def mark_complete(self, status: bool) -> None:
        """Mark the task as completed or not."""
        self.completion_status = status


class Scheduler:
    """The 'Brain' that retrieves, organizes, and manages tasks across pets."""
    
    def __init__(self, owner: Owner):
        """Initialize a Scheduler with a reference to the Owner."""
        self.owner = owner  # Reference to the owner who has multiple pets
        self.daily_plans = {}  # Daily plans for each pet
    
    def add_task(self, pet_id: str, task: Task) -> None:
        """Add a task to a specific pet's task list."""
        pet = self.owner.get_pet(pet_id)
        if pet:
            pet.add_task(task)
    
    def remove_task(self, pet_id: str, task_id: str) -> None:
        """Remove a task from a specific pet."""
        pet = self.owner.get_pet(pet_id)
        if pet:
            pet.remove_task(task_id)
    
    def get_all_tasks(self) -> list:
        """Retrieve all tasks from all pets across the owner's collection."""
        return self.owner.get_all_tasks()
    
    def get_pet_tasks(self, pet_id: str) -> list:
        """Retrieve all tasks for a specific pet."""
        pet = self.owner.get_pet(pet_id)
        if pet:
            return pet.get_tasks()
        return []
    
    def generate_daily_plan(self, pet_id: str, date) -> list:
        """Generate a daily plan for a specific pet based on owner and pet constraints."""
        tasks = self.get_pet_tasks(pet_id)
        sorted_tasks = sorted(tasks, key=lambda t: t.get_time())
        return sorted_tasks
    
    def generate_all_daily_plans(self, date) -> dict:
        """Generate daily plans for all pets owned by the owner."""
        plans = {}
        for pet_id, pet in self.owner.get_all_pets().items():
            plans[pet_id] = self.generate_daily_plan(pet_id, date)
        return plans
    
    def display_plan(self, pet_id: str) -> None:
        """Display the current daily plan for a specific pet."""
        pet = self.owner.get_pet(pet_id)
        if pet:
            tasks = self.generate_daily_plan(pet_id, None)
            print(f"\n=== Daily Schedule for {pet.get_name()} ===")
            if tasks:
                for task in tasks:
                    status = "✓" if task.is_completed() else "○"
                    print(f"{status} {task.get_time()} - {task.get_name()} ({task.get_duration()} min) [Priority: {task.get_priority()}]")
                    print(f"  Description: {task.get_description()}")
                    print(f"  Frequency: {task.get_frequency()}")
            else:
                print("No tasks scheduled.")
    
    def display_all_plans(self) -> None:
        """Display all daily plans for all pets."""
        for pet_id in self.owner.get_all_pets().keys():
            self.display_plan(pet_id)
    
    def edit_plan(self, pet_id: str, task_id: str, updates: dict) -> None:
        """Edit a task in a pet's plan with provided updates."""
        pet = self.owner.get_pet(pet_id)
        if pet:
            for task in pet.get_tasks():
                if task.get_id() == task_id:
                    for key, value in updates.items():
                        if hasattr(task, key):
                            setattr(task, key, value)
    
    def organize_tasks_by_time(self, pet_id: str) -> dict:
        """Organize tasks for a specific pet by scheduled time."""
        tasks = self.get_pet_tasks(pet_id)
        organized = {}
        for task in tasks:
            time = task.get_time()
            if time not in organized:
                organized[time] = []
            organized[time].append(task)
        return organized
    
    def organize_all_tasks_by_priority(self) -> dict:
        """Organize all tasks across all pets by priority level."""
        all_tasks = self.get_all_tasks()
        organized = {}
        for task in all_tasks:
            priority = task.get_priority()
            if priority not in organized:
                organized[priority] = []
            organized[priority].append(task)
        return organized
    
    def _prioritize_tasks(self, pet_id: str) -> list:
        """Internal method to prioritize tasks for a specific pet based on constraints and preferences."""
        tasks = self.get_pet_tasks(pet_id)
        return sorted(tasks, key=lambda t: t.get_priority(), reverse=True)
    
    def sort_by_time(self, tasks: list) -> list:
        """Sort tasks by their time attribute in HH:MM format.
        
        Uses a lambda function to convert 'HH:MM' format to minutes since midnight for proper sorting.
        
        Args:
            tasks: List of Task objects to sort
        
        Returns:
            List of Task objects sorted chronologically by time
        
        Example:
            >>> sorted_tasks = scheduler.sort_by_time(tasks)
            >>> # Tasks now ordered: 08:00, 09:00, 14:00, 17:00, etc.
        """
        def time_to_minutes(time_str: str) -> int:
            """Convert HH:MM format to minutes since midnight for comparison."""
            try:
                hours, minutes = map(int, time_str.split(':'))
                return hours * 60 + minutes
            except (ValueError, AttributeError):
                return 0  # Default to start of day if time format is invalid
        
        # Sort using lambda function that converts HH:MM to minutes since midnight
        return sorted(tasks, key=lambda t: time_to_minutes(t.get_time()))
    
    def _get_next_day(self, current_day: str, days_to_add: int) -> str:
        """Helper method to calculate the next day of week.
        
        Args:
            current_day (str): Current day name (Monday-Sunday)
            days_to_add (int): Number of days to add (1 for daily, 7 for weekly)
        
        Returns:
            str: Next day name (Monday-Sunday)
        """
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        try:
            current_index = days_of_week.index(current_day)
            next_index = (current_index + days_to_add) % 7
            return days_of_week[next_index]
        except ValueError:
            return current_day  # Return original if day is invalid
    
    def mark_task_complete(self, pet_id: str, task_id: str) -> None:
        """Mark a task as complete and create a new instance for recurring tasks.
        
        For tasks with 'daily' task_type, the new instance is scheduled for the next day.
        For tasks with 'weekly' task_type, the new instance is scheduled for the same day next week.
        For 'once' tasks, no new instance is created.
        
        Args:
            pet_id (str): The ID of the pet whose task should be marked complete
            task_id (str): The ID of the task to mark as complete
        """
        pet = self.owner.get_pet(pet_id)
        if not pet:
            return
        
        # Find and mark the task as complete
        target_task = None
        for task in pet.get_tasks():
            if task.get_id() == task_id:
                target_task = task
                break
        
        if not target_task:
            return
        
        # Mark current task as complete
        target_task.mark_complete(True)
        
        # Create new task for next occurrence based on task_type
        task_type = target_task.get_task_type().lower()
        
        if task_type in ["daily", "weekly"]:
            # Create new task with same properties
            new_task_id = str(uuid.uuid4())[:8]
            
            # Calculate the next occurrence day based on recurrence type
            current_day = target_task.get_day()
            if task_type == "daily":
                # For daily tasks, shift by 1 day
                next_day = self._get_next_day(current_day, 1)
            elif task_type == "weekly":
                # For weekly tasks, shift by 7 days (same day next week)
                next_day = self._get_next_day(current_day, 7)
            else:
                next_day = current_day
            
            new_task = Task(
                task_id=new_task_id,
                name=target_task.get_name(),
                description=target_task.get_description(),
                task_type=target_task.get_task_type(),  # Preserve recurrence type
                time=target_task.get_time(),
                frequency=target_task.get_frequency(),  # Keep for compatibility
                duration=target_task.get_duration(),
                priority=target_task.get_priority(),
                pet_id=pet_id,
                day=next_day  # Set to shifted day
            )
            # Add new task to the pet
            pet.add_task(new_task)



