import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
import uuid

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# Initialize session state for owner and scheduler
if "owner" not in st.session_state:
    st.session_state.owner = None

if "scheduler" not in st.session_state:
    st.session_state.scheduler = None

if "current_pet_id" not in st.session_state:
    st.session_state.current_pet_id = None

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "completed_task_ids" not in st.session_state:
    st.session_state.completed_task_ids = set()

if "show_priority_view" not in st.session_state:
    st.session_state.show_priority_view = False

if "show_time_view" not in st.session_state:
    st.session_state.show_time_view = False

if "priority_day_filter" not in st.session_state:
    st.session_state.priority_day_filter = "All Days"

if "time_day_filter" not in st.session_state:
    st.session_state.time_day_filter = "All Days"

st.title("🐾 PawPal+")

# st.markdown(
#     """
# Welcome to the PawPal+ starter app.

# This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
# but **it does not implement the project logic**. Your job is to design the system and build it.

# Use this app as your interactive demo once your backend classes/functions exist.
# """
# )

# with st.expander("Scenario", expanded=True):
#     st.markdown(
#         """
# **PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
# for their pet(s) based on constraints like time, priority, and preferences.

# You will design and implement the scheduling logic and connect it to this Streamlit UI.
# """
#     )

# with st.expander("What you need to build", expanded=True):
#     st.markdown(
#         """
# At minimum, your system should:
# - Represent pet care tasks (what needs to happen, how long it takes, priority)
# - Represent the pet and the owner (basic info and preferences)
# - Build a plan/schedule for a day that chooses and orders tasks based on constraints
# - Explain the plan (why each task was chosen and when it happens)
# """
#     )

st.divider()

st.subheader("👤 Owner & Pet Management")

col1, col2, col3 = st.columns(3)
with col1:
    owner_name = st.text_input("Owner name", value="Jordan")
with col2:
    owner_age = st.number_input("Owner age", min_value=0, max_value=120, value=30)
with col3:
    st.empty()

# Create or update Owner in session state
if st.button("Create/Update Owner"):
    # Create Owner if it doesn't exist
    if st.session_state.owner is None:
        st.session_state.owner = Owner(name=owner_name, age=owner_age, special_needs=[], constraints={})
        st.session_state.scheduler = Scheduler(st.session_state.owner)
    else:
        st.session_state.owner.name = owner_name
        st.session_state.owner.age = owner_age
    
    st.success(f"Owner '{owner_name}' created/updated successfully!")

# Display existing owner info
if st.session_state.owner:
    st.info(f"**Current Owner:** {st.session_state.owner.get_name()} (Age: {st.session_state.owner.get_age()})")

st.subheader("🐾 Add a Pet")

col1, col2, col3 = st.columns(3)
with col1:
    pet_name = st.text_input("Pet name", value="Mochi")
with col2:
    pet_age = st.number_input("Pet age", min_value=0, max_value=50, value=3)
with col3:
    species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet to Owner"):
    if st.session_state.owner is None:
        st.error("Please create an owner first!")
    else:
        # Create Pet and add to Owner using add_pet method
        pet_id = str(uuid.uuid4())[:8]
        new_pet = Pet(name=pet_name, age=pet_age, breed=species, special_needs=[])
        st.session_state.owner.add_pet(pet_id, new_pet)
        st.session_state.current_pet_id = pet_id
        st.success(f"Pet '{pet_name}' added to {st.session_state.owner.get_name()}'s collection!")

# Display all pets using get_all_pets method
if st.session_state.owner:
    all_pets = st.session_state.owner.get_all_pets()
    if all_pets:
        st.write("**Your Pets:**")
        for pet_id, pet in all_pets.items():
            pet_info = f"🐾 {pet.get_name()} ({pet.get_breed()}) - Age: {pet.get_age()}"
            if st.session_state.current_pet_id == pet_id:
                st.success(pet_info + " ✓ (Current)")
            else:
                if st.button(f"Select: {pet.get_name()}", key=f"select_{pet_id}"):
                    st.session_state.current_pet_id = pet_id
                    st.rerun()

st.markdown("### 📋 Schedule a Task")
st.caption("Add tasks for the selected pet.")

if st.session_state.current_pet_id and st.session_state.owner:
    current_pet = st.session_state.owner.get_pet(st.session_state.current_pet_id)
    st.info(f"Adding tasks for: **{current_pet.get_name()}**")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    with col4:
        task_time = st.text_input("Time (HH:MM)", value="09:00")
    
    col5, col6 = st.columns(2)
    with col5:
        task_type = st.selectbox("Recurrence", ["once", "daily", "weekly"], index=1)
    with col6:
        task_day = st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=0)
    
    # Convert priority string to numeric value
    priority_map = {"low": 1, "medium": 2, "high": 3}
    priority_numeric = priority_map[priority]
    
    if st.button("Schedule Task"):
        # Create Task object and add via scheduler's add_task method
        task_id = str(uuid.uuid4())[:8]
        new_task = Task(
            task_id=task_id,
            name=task_title,
            description=f"Pet care task: {task_title}",
            task_type=task_type,  # Now 'once', 'daily', or 'weekly'
            time=task_time,
            frequency=task_type,  # Keep compatible with existing code
            duration=int(duration),
            priority=priority_numeric,
            pet_id=st.session_state.current_pet_id,
            day=task_day  # Add day of week
        )
        
        # Use scheduler's add_task method
        st.session_state.scheduler.add_task(st.session_state.current_pet_id, new_task)
        
        # Also store in session tasks list for display
        st.session_state.tasks.append({
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority,
            "time": task_time,
            "task_id": task_id
        })
        st.success(f"Task '{task_title}' scheduled for {current_pet.get_name()}!")
    
    # Display tasks using get_pet_tasks method via scheduler
    st.markdown("#### Current Tasks for this Pet")
    pet_tasks = st.session_state.scheduler.get_pet_tasks(st.session_state.current_pet_id)
    
    if pet_tasks:
        # Display organized by priority using organize_tasks_by_priority style organization
        for task in pet_tasks:
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
            with col1:
                st.write(f"**{task.get_name()}** - {task.get_time()}")
            with col2:
                st.write(f"📅 {task.get_day()}")
            with col3:
                st.write(f"⏱️ {task.get_duration()}min")
            with col4:
                priority_display = {1: "🟢 Low", 2: "🟡 Med", 3: "🔴 High"}
                st.write(priority_display.get(task.get_priority(), ""))
            with col5:
                if st.button("❌ Remove", key=f"remove_{task.get_id()}"):
                    st.session_state.scheduler.remove_task(st.session_state.current_pet_id, task.get_id())
                    st.session_state.tasks = [t for t in st.session_state.tasks if t.get("task_id") != task.get_id()]
                    st.rerun()
    else:
        st.info("No tasks scheduled yet for this pet.")
else:
    st.warning("Please create an owner and add a pet first to schedule tasks.")

# st.divider()

# st.subheader("📅 Build & View Schedule")

# col1, col2 = st.columns(2)

# with col1:
#     if st.button("Generate Schedule for Current Pet"):
#         if st.session_state.owner is None or st.session_state.current_pet_id is None:
#             st.error("Please create an owner and add a pet first!")
#         else:
#             current_pet = st.session_state.owner.get_pet(st.session_state.current_pet_id)
#             pet_tasks = st.session_state.scheduler.get_pet_tasks(st.session_state.current_pet_id)
            
#             if not pet_tasks:
#                 st.warning("No tasks scheduled for this pet. Add some tasks first!")
#             else:
#                 st.success("✓ Schedule generated!")
#                 st.markdown(f"### Daily Schedule for {current_pet.get_name()}")
#                 st.markdown(f"**Owner:** {st.session_state.owner.get_name()}")
                
#                 # Use scheduler's display_plan method
#                 st.session_state.scheduler.display_plan(st.session_state.current_pet_id)

# with col2:
#     if st.button("View All Pets' Schedules"):
#         if st.session_state.owner is None:
#             st.error("Please create an owner first!")
#         else:
#             all_pets = st.session_state.owner.get_all_pets()
#             if not all_pets:
#                 st.warning("No pets added yet.")
#             else:
#                 st.success("✓ Displaying all schedules!")
#                 # Use scheduler's display_all_plans method
#                 st.session_state.scheduler.display_all_plans()

st.divider()

st.subheader("📊 Task Analytics")

col1, col2 = st.columns(2)

with col1:
    if st.button("View Tasks Organized by Priority"):
        st.session_state.show_priority_view = not st.session_state.show_priority_view

with col2:
    if st.button("View Tasks Sorted by Time"):
        st.session_state.show_time_view = not st.session_state.show_time_view

if st.session_state.show_priority_view:
    if st.session_state.owner is None:
        st.warning("No owner created yet.")
    else:
        all_tasks = st.session_state.scheduler.get_all_tasks()
        if not all_tasks:
            st.info("No tasks scheduled yet.")
        else:
            st.markdown("### 📋 Tasks Organized by Priority")
            # Day filter dropdown
            day_options = ["All Days", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            st.session_state.priority_day_filter = st.selectbox(
                "Filter by Day:",
                day_options,
                index=day_options.index(st.session_state.priority_day_filter),
                key="priority_day_select"
            )
            
            # Use scheduler's organize_all_tasks_by_priority method
            organized = st.session_state.scheduler.organize_all_tasks_by_priority()
            priority_labels = {1: "🟢 Low Priority", 2: "🟡 Medium Priority", 3: "🔴 High Priority"}
            
            for priority in sorted(organized.keys(), reverse=True):
                with st.expander(priority_labels.get(priority, f"Priority {priority}")):
                    for task in organized[priority]:
                        # Apply day filter
                        if st.session_state.priority_day_filter != "All Days" and task.get_day() != st.session_state.priority_day_filter:
                            continue
                        
                        pet_name = st.session_state.owner.get_pet(task.get_pet_id()).get_name()
                        
                        col_info, col_button = st.columns([4, 1])
                        with col_info:
                            status = "✓" if task.is_completed() else "○"
                            st.write(f"{status} **{task.get_name()}** ({task.get_duration()}min) - {pet_name}")
                            st.caption(f"📅 {task.get_day()} | 🕐 {task.get_time()} | 🔄 {task.get_task_type()}")
                        
                        with col_button:
                            if not task.is_completed():
                                if st.button("✓ Mark", key=f"priority_complete_{task.get_id()}"):
                                    st.session_state.scheduler.mark_task_complete(task.get_pet_id(), task.get_id())
                                    st.session_state.completed_task_ids.add(task.get_id())
                                    st.success("Task marked complete!")
                                    st.rerun()
                            else:
                                st.caption("✓ Done")

if st.session_state.show_time_view:
    if st.session_state.owner is None:
        st.warning("No owner created yet.")
    else:
        all_tasks = st.session_state.scheduler.get_all_tasks()
        if not all_tasks:
            st.info("No tasks scheduled yet.")
        else:
            st.markdown("### 🕐 All Tasks (Sorted by Time)")
            # Day filter dropdown
            day_options = ["All Days", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            st.session_state.time_day_filter = st.selectbox(
                "Filter by Day:",
                day_options,
                index=day_options.index(st.session_state.time_day_filter),
                key="time_day_select"
            )
            
            sorted_tasks = st.session_state.scheduler.sort_by_time(all_tasks)
            
            for task in sorted_tasks:
                # Apply day filter
                if st.session_state.time_day_filter != "All Days" and task.get_day() != st.session_state.time_day_filter:
                    continue
                
                pet = st.session_state.owner.get_pet(task.get_pet_id())
                priority_display = {1: "🟢 Low", 2: "🟡 Med", 3: "🔴 High"}
                status = "✓" if task.is_completed() else "○"
                
                col_info, col_button = st.columns([4, 1])
                with col_info:
                    st.write(f"{status} **{task.get_time()}** - {task.get_name()}")
                    st.caption(f"🐾 {pet.get_name()} | 📅 {task.get_day()} | ⏱️ {task.get_duration()}min | 🔄 {task.get_task_type()} | {priority_display.get(task.get_priority(), '')}")
                
                with col_button:
                    if not task.is_completed():
                        if st.button("✓ Mark", key=f"time_complete_{task.get_id()}"):
                            st.session_state.scheduler.mark_task_complete(task.get_pet_id(), task.get_id())
                            st.session_state.completed_task_ids.add(task.get_id())
                            st.success("Task marked complete!")
                            st.rerun()
                    else:
                        st.caption("✓ Done")
