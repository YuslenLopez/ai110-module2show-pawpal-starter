"""Tests for the PawPal system."""

import pytest
from pawpal_system import Task, Pet


class TestTaskCompletion:
    """Test task completion functionality."""
    
    def test_mark_complete_changes_status(self):
        """Verify that calling mark_complete() actually changes the task's status."""
        # Arrange: Create a task with completion_status = False
        task = Task(
            task_id="task_001",
            name="Morning Walk",
            description="Walk the dog in the morning",
            task_type="walk",
            time="09:00",
            frequency="daily",
            duration=30,
            priority=1,
            pet_id="pet_001"
        )
        
        # Assert initial state is not completed
        assert task.is_completed() is False
        
        # Act: Mark the task as complete
        task.mark_complete(True)
        
        # Assert: Verify that the task is now marked as completed
        assert task.is_completed() is True
        
        # Act: Mark the task as incomplete
        task.mark_complete(False)
        
        # Assert: Verify that the task is now marked as incomplete again
        assert task.is_completed() is False


class TestTaskAddition:
    """Test task addition to pets."""
    
    def test_adding_task_increases_pet_task_count(self):
        """Verify that adding a task to a Pet increases that pet's task count."""
        # Arrange: Create a pet and verify it starts with no tasks
        pet = Pet(
            name="Buddy",
            age=3,
            breed="Golden Retriever"
        )
        
        # Assert initial task count is 0
        assert len(pet.get_tasks()) == 0
        
        # Act: Create and add a task to the pet
        task1 = Task(
            task_id="task_001",
            name="Morning Walk",
            description="Walk the dog in the morning",
            task_type="walk",
            time="09:00",
            frequency="daily",
            duration=30,
            priority=1,
            pet_id="pet_001"
        )
        pet.add_task(task1)
        
        # Assert: Verify that task count increased to 1
        assert len(pet.get_tasks()) == 1
        
        # Act: Add another task
        task2 = Task(
            task_id="task_002",
            name="Feeding",
            description="Feed the dog",
            task_type="feeding",
            time="18:00",
            frequency="daily",
            duration=15,
            priority=1,
            pet_id="pet_001"
        )
        pet.add_task(task2)
        
        # Assert: Verify that task count increased to 2
        assert len(pet.get_tasks()) == 2
