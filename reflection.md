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

1.Scheduler considers the time, priority and days of the tasks.
2.I worked out the constraints both by imagening my own interactions with it if I had a pet and also thinking through what might be a nice feature for users while implementing other items.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

1.The main trade off my scheduler makes it maybe the design of the two types of displays for task analytics.
2.The tradeoff is resonable because my focus is on something that is useable and functional reather than super eye appealing. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

1.I used AI to brain storm the UML and features that would be nice to have for the app. I also used it to autocomplete smaller repetative bits of code. 
2.The prompts that felt most helpful were ones that would ask the AI for ideas rather than answers. This help me formulate my own ideas and features I would like added which the AI then helped implement.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

1.I rejected a couple of implementaion given by the AI. Mostly when the AI accedentaly broke the code due to lack of vision. I would simply undo the changes and try prompting more throughly again till it gave me what I wanted without breaking anything. 
2.Most of my evaluation of what the AI suggested what dont by attempting cases in which thes features would prove helpful. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

1.I tested behaviors of having multiple pets and many tasks of varying time and days.
2.These tests were important to finding out what parts of the code were not working as intended. 

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

1.I'm about 70% confident that my scheduler works for the simple pet owner than needs help tracking tasks for their pets. 
2.If I had more time I would test the edge cases that deal with overlapping time of tasks , the reoccurance of tasks after marked complete and the design of the web app to make it more user friendly. 

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

1.Im satisfied that the app works and that I learn how to use AI in new ways that resulted in a functional prototype. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

1.I would definitely focus on improving the display of the tasks both in functionality and design to make the use of the app more attractive to users. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

1. It is important to take each step slowly and think through what it is exactly you are building and what functionailties the project should contain. To the extent, taking more time to have the AI come up with potential features and bottle necks is a crusial. 
