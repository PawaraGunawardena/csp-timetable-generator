import copy


input_path = raw_input("Input Location: ")
output_path = raw_input("Output Location: ")

#Function to read input data
def get_input(location):
    
    with open(location, 'r') as input_data:                         #open for read data
        input_value = input_data.read()
        input_subject_list = input_value.split('\n')
        input_data_sprt = []; 
        for current_subject in input_subject_list:
            input_data_sprt.append(current_subject.split(','))
        return input_data_sprt

#Function to assign timeslots to each subjects    
def shedule_time_slot(depth):
    global time_slots_assigned
    global state_of_time_slots_assigned
    global subject_state_possibleTimes

##    print time_slots_assigned
##    print state_of_time_slots_assigned
##    print subject_state_possibleTimes

    #print "Depth : "+str(depth)
    #print "Length of the Input Array: "+str(len(subject_state_possibleTimes))
    
    if(depth == len(subject_state_possibleTimes)):                              #Termination Condition of the Recursion
        return True

    #Read all the Current Values in the Recursion Depth
    current_subject_name = subject_state_possibleTimes[depth][0]
    current_possible_time_slots = subject_state_possibleTimes[depth][2:]
    current_subject_category_state = subject_state_possibleTimes[depth][1]

    #print current_subject_name
    #print current_possible_time_slots
    #print current_subject_category_state

    if (current_subject_category_state == "c"):                             #Consider the Compulsory Subjects as a seperate category with Optional Subjects                                 
        for slot in current_possible_time_slots:
            if (slot not in state_of_time_slots_assigned.keys()):           #If the time slot available for current cubject is not assigned for any other before           
                time_slots_assigned[depth][0] = current_subject_name
                time_slots_assigned[depth][1] = slot
                state_of_time_slots_assigned[slot] = ["c"]
                #print time_slots_assigned
                
                shedule_time_slot(depth+1)
                return True
##                if (shedule_time_slot(depth+1)):
##                    return True      
##                else:
##                    return False
                
        else:
            
            current_subject_slots_degree = {}
            for slot in current_possible_time_slots:
 
                if("c" not in state_of_time_slots_assigned[slot] ):                #If the time slot available for current cubject is assigned for optional subject
                                                                                #get the minmum assigned subject as follows
                    current_subject_slots_degree[slot] = len(state_of_time_slots_assigned[slot])
            if(len(current_subject_slots_degree)>0):
                subject_min_degree_head = min(current_subject_slots_degree, key=lambda k: current_subject_slots_degree[k]) #select the minmum assigned subject 
                time_slots_assigned[depth][0] = current_subject_name
                time_slots_assigned[depth][1] = subject_min_degree_head
                state_of_time_slots_assigned[subject_min_degree_head].append("c")

                shedule_time_slot(depth+1)
            else:
                return False



    
    elif (current_subject_category_state == "o"):               # if the current subject is optional then can assign timeslot
        for slot in current_possible_time_slots:
            if (slot not in state_of_time_slots_assigned.keys()):           #if previously not assigned then do this
                time_slots_assigned[depth][0] = current_subject_name
                time_slots_assigned[depth][1] = slot
                state_of_time_slots_assigned[slot] = ["o"]
                #print time_slots_assigned
                shedule_time_slot(depth+1)
                
                return True
            
##            if (shedule_time_slot(depth+1)):
##                return True          
##            else:
##                return False
        else:
            current_subject_slots_degree = {}
            for slot in current_possible_time_slots:                
                current_subject_slots_degree[slot] = len(state_of_time_slots_assigned[slot])      #get the minmum assigned subject as follows

            if(len(current_subject_slots_degree)>0):
                subject_min_degree_head = min(current_subject_slots_degree, key=lambda k: current_subject_slots_degree[k])   #select the minmum assigned subject 
                time_slots_assigned[depth][0] = current_subject_name
                time_slots_assigned[depth][1] = subject_min_degree_head
                state_of_time_slots_assigned[subject_min_degree_head].append("o")

                shedule_time_slot(depth+1)
            else:
                return False
##            for slot in current_possible_time_slots:
##                if("c" not in state_of_time_slots_assigned[slot]):
##                    time_slots_assigned[depth][0] = current_subject_name
##                    time_slots_assigned[depth][1] = slot
##                    state_of_time_slots_assigned[slot].append("o")
##                    #print time_slots_assigned
##                    shedule_time_slot(depth+1)
##                    
##                    return True
##                
##            else:
##                for slot in current_possible_time_slots:
##                    
##                    time_slots_assigned[depth][0] = current_subject_name
##                    time_slots_assigned[depth][1] = slot
##                    
##                    #print time_slots_assigned
##                    shedule_time_slot(depth+1)
##                    
##                    return True


#Function to assign room to each [subjects, timeslot] combination 
def shedule_room(depth):                                                                #select a room for the (subject, timeslot)
    global time_slots_assigned
    global room_assigned_for_time_given
    global available_rooms
   

    if(depth == len(time_slots_assigned)):
        return True
    current_subject = time_slots_assigned[depth][0]
    current_time_slot = time_slots_assigned[depth][1]
    for room_to_assign in available_rooms:
        room = room_to_assign
        if (current_time_slot not in room_assigned_for_time_given.keys()):
            room_assigned_for_time_given[current_time_slot] = [room]
            time_slots_assigned[depth].append(room)
            shedule_room(depth+1)
            return True
            
        elif(room not in room_assigned_for_time_given[current_time_slot]):
            room_assigned_for_time_given[current_time_slot].append(room)
            time_slots_assigned[depth].append(room)
            shedule_room(depth+1)
            return True
    else:
        return False

#Function to change the subject order in the input. This will give the subject list with minimum possible timeslots to maximum possible timeslots
def change_subject_order(subject_given_order):          #output minimum to maximum with priority to compulsory subjects  
    tekmporary_assigned_optional_array=[]
    temporary_assigned_permanent_array=[]

    #subject_order = []

    for subject in subject_given_order:
        if subject[1] == "o":
            tekmporary_assigned_optional_array.append(subject)
        elif subject[1] == "c":
            temporary_assigned_permanent_array.append(subject)
    temporary_assigned_permanent_array.sort(key=len)
    tekmporary_assigned_optional_array.sort(key=len)
        #subject_order.append(subject)

    subject_order=temporary_assigned_permanent_array+tekmporary_assigned_optional_array
    
    subject_order.sort(key=len)
    return subject_order

#Write output file and return output
def set_output(location, subject_time_room_list):
    data_string = ""
    for row in subject_time_room_list:
        row_string = ""
        for col in row:
            row_string += col + ','
        else:
            row_string = row_string[:-1]
        data_string += row_string + '\n'
    else:
        data_string = data_string[:-1]
    with open(location, 'w') as file_to_write:
        file_to_write.write(data_string)

#Read input data and arrange input data
inputDetails = get_input(input_path)

subject_state_possibleTimes1 = inputDetails[:-1]    #remove rooms 

subject_state_possibleTimes = change_subject_order(subject_state_possibleTimes1)
print "Given Subjet List in Least Constraints Order: "
print subject_state_possibleTimes
print "\n"

available_rooms = inputDetails[-1]    #get rooms details seperately
print "Available Rooms Given:"
print available_rooms
print "\n"

#Arrange Data files to the Implementation

time_slots_assigned = q = [['' for i in xrange(2)] for i in xrange(len(subject_state_possibleTimes))] #Make and empty list for assigned [subject, timeslot] data

state_of_time_slots_assigned = {} #dictionary for keep assigned time slots and the assigned subject condition (Optional or Compulsory)
room_assigned_for_time_given = {} #Dictionary for keep track the assigned room for that time slot
slot_assigned = shedule_time_slot(0) #Call the function to shedule and assign time slots

print "List of Timeslots Assigned Values before rooms assigning: "
print time_slots_assigned
print "\n"
#print state_of_time_slots_assigned

if(slot_assigned):
    result  = shedule_room(0) # Call function to assign rooms to [subject, timeslot] combinations

    #print room_assigned_for_time_given
    print "List of Time Slots Assigned Values after Rooms Assigned: "
    print time_slots_assigned
    print "\n"


    if (result): # if the implementation completed then call the function to output result.
        set_output(output_path, time_slots_assigned)
        print "\nFinal Subject Timeslot Room Solution:"
        for subject_list in time_slots_assigned:
           print subject_list
    else:
        print "Your given Problem do not have an entire Solution. Try to increase the number of Rooms for the timetable."
else:
    print "Your given Problem do not have an entire Solution. Try to have more timeslots for subjects."

raw_input("Input Any Key to Exit")                  #stop elimination of the algorithm at the last step



