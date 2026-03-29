from pawpal_system import Owner, Pet, Task, Scheduler

# Create an Owner
owner = Owner(name="Sarah Johnson", age=28, special_needs=[], constraints={"budget": "flexible", "work_hours": "9-5"})

# Create at least two Pets
dog = Pet(name="Max", age=3, breed="Golden Retriever", special_needs=["needs daily exercise"])
cat = Pet(name="Whiskers", age=5, breed="Siamese", special_needs=["indoor only"])

# Add pets to owner
owner.add_pet("pet_001", dog)
owner.add_pet("pet_002", cat)

# Create a Scheduler (the "Brain")
scheduler = Scheduler(owner)

# Create Tasks with different times for the dog
task1 = Task(
    task_id="task_001",
    name="Morning Walk",
    description="Take Max for a walk in the park to get exercise and socialize",
    task_type="walk",
    time="08:00",
    frequency="daily",
    duration=30,
    priority=3,
    pet_id="pet_001"
)

task2 = Task(
    task_id="task_002",
    name="Breakfast",
    description="Feed Max with high-quality dog food and fresh water",
    task_type="feeding",
    time="08:30",
    frequency="daily",
    duration=10,
    priority=2,
    pet_id="pet_001"
)

task3 = Task(
    task_id="task_003",
    name="Afternoon Play",
    description="Playtime with toys and fetch games for mental stimulation",
    task_type="exercise",
    time="14:00",
    frequency="daily",
    duration=45,
    priority=2,
    pet_id="pet_001"
)

# Create tasks for the cat
task4 = Task(
    task_id="task_004",
    name="Cat Feeding",
    description="Serve Whiskers wet and dry food with fresh water",
    task_type="feeding",
    time="09:00",
    frequency="twice daily",
    duration=10,
    priority=3,
    pet_id="pet_002"
)

task5 = Task(
    task_id="task_005",
    name="Litter Box Cleaning",
    description="Clean the litter box daily to maintain hygiene",
    task_type="grooming",
    time="17:00",
    frequency="daily",
    duration=5,
    priority=2,
    pet_id="pet_002"
)

# Add all tasks to the scheduler
scheduler.add_task("pet_001", task1)
scheduler.add_task("pet_001", task2)
scheduler.add_task("pet_001", task3)
scheduler.add_task("pet_002", task4)
scheduler.add_task("pet_002", task5)

# Print Today's Schedule
print("=" * 60)
print("🐾 PAWPAL - TODAY'S PET CARE SCHEDULE 🐾")
print("=" * 60)
print(f"\nOwner: {owner.get_name()} (Age: {owner.get_age()})")
print(f"Constraints: {owner.get_constraints()}")

# Display all schedules
scheduler.display_all_plans()

# Additional info: Show all tasks organized by priority
print("\n" + "=" * 60)
print("ALL TASKS ORGANIZED BY PRIORITY")
print("=" * 60)
priority_tasks = scheduler.organize_all_tasks_by_priority()
for priority in sorted(priority_tasks.keys(), reverse=True):
    print(f"\nPriority Level {priority}:")
    for task in priority_tasks[priority]:
        pet = owner.get_pet(task.get_pet_id())
        print(f"  - {task.get_name()} ({pet.get_name()}) at {task.get_time()}")

print("\n" + "=" * 60)


