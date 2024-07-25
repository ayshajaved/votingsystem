print("***********************")
print("----VOTING PROGRAM----")
print("***********************")                           #displaying the title
candidate_1 = input("Enter the first candidate name:- ")   #User's choice candidates for the voting!
candidate_2 = input("Enter the second candidate name:- ")
print("Sucessfully added!Voting started!")
print("----------------------------------")
print("")                                                  
ids =[]   
points_1 = 0                                               #setting the initial votes of the candidates as 0
points_2 = 0
condition = True                                           #initializing the condition for the loop to enter the votes
n =1                                                       #voters are counting
while condition:
    print(f"The candidates are {candidate_1} and {candidate_2}!")#displaying the candidates
    id = input(f"Enter your 3 digit id (person {n}):-")          #message for user id that is unique and of 3 digits
    if len(id) >3 or len(id) <3:                                 #condition to check whether the id is as required or not!
        print("Id is incorrect!Try again")
    elif id in ids:                                              #checking whether the same person is casting vote twice
        print("Same person Can't vote twice!(same id)!")
    else:                                                              
        ids.append(id)                                           #making a list of voter's id
        candidate =input("Whom you want to cast the vote?Enter the name:-") #votes are casting
        if candidate == "a" or candidate == "b":
            n+=1
            if candidate == candidate_1:                             #votes are added to the candidate of voter's choice
                points_1+=1
            elif candidate == candidate_2:
                points_2 +=1
        else:
            print("The name you entered is not a candidate!")    #checking if the user enter's wrong candidate name
    if n >=11:                                                   #votes are casting only of 10 voters
        condition=False 
    print("")

#compiling results
print(f"{n-1} Candidates have entered the votes!")               
print("The results are compiling!")
if points_1 == points_2:                                         #checking which candidate is the winner
    print("It's a tie..")
elif (points_1 > points_2):                                      #displaying results
    print("{} has won! by {} points".format(candidate_1, (points_1-points_2))) 
else:
    print("{} has won! by {} points".format(candidate_2, (points_2-points_1)))

