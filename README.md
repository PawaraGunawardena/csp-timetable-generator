This is a Constraint Satisfaction Problem to develop a timetable for a semester. 
There is a list of subjects, a set of possible time slots for each subject and a set of rooms. 
Some subjects are compulsory some are optional.

Following are the constraints to satisfy. 

	1. A given subjects can be assigned only to one of the possible time slots given for that subject. 
	
	2. Two compulsory subjects cannot be in the same time slot (optional subjects may). 
	
	3. Two subjects cannot be assigned to the same room if they are assigned to the same time slot. 
	
Need to assign each subject a time slot and a room. Solution has the source code and exe file. 
This program take two command line arguments; <input_file_name> and <output_file_name>

Given program take a comma separated values (CSV) file of the form given below as input and output a CSV file of the form given below. 
	
	Input.csv -

	Subject_1, c, M1, M3, Tu2
	
	Subject_2, o, Tu1, W1, Th2
	
	Subject_3, c, M1, M3, W1
	
	...
	
	Subject_n, o, M3, Th2
	
	R1, R2, R3
	
1st column: subject name

2nd column: c- compulsory, o-optional

3rd column onwards: possible time slots M1 - Monday slot 1, M3 - Monday slot 3, Tu2 - Tuesday slot 2

etc.

	Output.csv -

	Subject_1, M1, R1
	
	Subject_2, Tu1, R3
	
	Subject_3, M3
	
	...
	
	Subject_n, Th2, R1
	

There is a constraint that says only one possible time slot exists for one subject. 
So the solution consisting with assigning one possible time slot for each subject. 

The Problem have two major types of constraints when assigning a single timeslot for a subject

•	Two compulsory subjects cannot be in the same timeslot

•	Two subjects which have same timeslot cannot be in the same room. 

So the given solution divide the problem into two major constraint satisfaction problems.
Assigning Timeslots for Subjects is first and Assigning rooms for (Subject, Timeslot) Combinations is the second. 

Problem 1 – 

The first problem is assigning a Timeslot for each subject, with no two compulsory subjects in the same timeslot.  

Variable Set (V) – {Given Subject List}
		
Constraints Set (C) – {No two Compulsory subjects in the same timeslot, Variable can have their own set of possible values from timeslots that mentioned under each Subject in the input data}

Domain (D) for Variable Values – {Set of timeslots given. This will differ from Variable to variable.}
	
	Implementation – 
	
Arrange the subjects list in a way, while giving priority to compulsory subjects rearrange subjects with least possible number of timeslots available are at the very beginning of the list. 
			
			If a Compulsory Subject: 
			
	•	Tries to assign a timeslot from available time slots for the subject. At the very first tries to assign a timeslot that do not assigned previously. 
	
	•	If cannot get not assigned time slot then tries to assign a timeslot which has previously assigned for optional subject. And this assignment do base on the degree of the already assigned optional timeslot which available under this subject. (Means:  If all available timeslots at least have assigned previously under a different subject, then assign this one under a timeslot which have no any compulsory subject, and between all available timeslots which have only optional subjects, select the least degree/ least optional subjects assigned timeslot.)
	
	•	If both tries fails then cannot assign a time slot for the subject, and timetable cannot complete. 
	
	
			If an optional subject:
			
	•	Tries to assign a timeslot from available time slots for the subject. At the very first tries to assign a timeslot that do not assigned previously. Because of this it helps to minimize conflicts when assigning rooms.
	
	•	If cannot get not assigned timeslot then tries to assign a timeslot which has previously assigned. And this assignment do base on the degree of the already assigned timeslots which available under this subject. (Means:  If all available timeslots, at least have assigned previously under a different subject, then assign this one under that one, and between all timeslots which available under this, select the least degree/ least subjects assigned timeslot.) 
	
	•	For optional subjects there exist at least one solution from above two selections. 


Problem 2 – 
	
The problem is assigning a room for each (subject, timeslot) that got from the problem-1. Two subjects with same timeslot cannot get into the same room.

		Variable Set (V) – {Given (Subject, Timeslot) Combinations returned from problem 1}
		
		Constraint Set (C) – {Two subjects with same timeslot cannot assigned to same room}
		
Domain (D) for Variable Values – {Set of rooms Available to conduct subjects. This list should give as Input data for the problem. Implementation input will take it at the last line of the input data}

	Implementation – 
	
		Take the output from the problem 1 which gives (subject, timeslot) combinations after assigning timeslot for each subject. 
	
		Tries to assign room for each (subject, timeslot) pair. 
	
		Algorithm keep track of the timeslot and assigned list of rooms for each time slot. 
	
		If the available number of rooms are less than the maximum number of subjects which has the same timeslot, then the timetable cannot complete. 
	(if no_of_rooms < max(no_of_subjects_have_same_time_slot for each time slot) then timetable cannot complete )
	
		Otherwise algorithm will give a complete solution

At the end of the problem 2 it gives the solution for the entire problem as a collection of (subject, timeslot, room) for each given subject.
