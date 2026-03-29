# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

1. The inital design takes into account the owner, pet, constraints set by both and uses that to design a daily plan that then creates a task to be completed. 
2. Classes such as : 
a.Owner- determines the constraints for the plan 
b.Pet- effects the constraints and information present in the plan 
c.Daily plan- takes into account the information from the pet and owner to create a scheduled task. 
d.Scheduler- Displays the Daily and scheduled plans, also allows editing of the displayed plans  

Attributes: 
a.Owner - name, age, specialNeeds, decides the constraints for plan
b.Pet - name, age, breed, specialNeeds, plan must take into account the dog and the dog recieved a plan  
c.Scheduler- takes information from first two classes to determine a Dailyplan/ task for the pet and displays it with editing capabilities for the owner.
d.Plan-describes the time and priority of the taks such as : walks, feeding, medicine, grooming, etc

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

1. Yes the design change because there was a missing link between the tasks and pets to ensure each pet was uniquely tied to their plan/ tasks. 
2. The change made was the addition of a pet_id for each of the tasks so that they are uniquely tied to one pet and a owner can view all of their pets by unique ids. 
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
