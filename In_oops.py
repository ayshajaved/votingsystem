class Voting_program:                                                   #class for the voting_program
    def __init__(self):
        self.ids =[]   
        self.candidatesofvoters=[]
        self.points_1 = 0                                               #setting the initial votes of the candidates as 0
        self.points_2 = 0
        self.condition = True                                           #initializing the condition for the loop to enter the votes
        self.n =1                 
        pass
    def display(self):
        print("***********************")
        print("----VOTING PROGRAM----")
        print("***********************")                                 #displaying the title
    def candidates(self):
        self.candidate_1 = input("Enter the first candidate name:- ")     #User's choice candidates for the voting!
        self.candidate_2 = input("Enter the second candidate name:- ")
        print("Sucessfully added!Voting started!")
        print("----------------------------------")
        print("")     
        self.voting()

    def result(self):
        print(f"{self.n-1} Candidates have entered the votes!")               
        print("The results are compiling!")
        if self.points_1 == self.points_2:                                         #checking which candidate is the winner
            print("It's a tie..")
        elif (self.points_1 > self.points_2):                                      #displaying results
            print("{} has won! by {} points".format(self.candidate_1, (self.points_1-self.points_2))) 
        else:
            print("{} has won! by {} points".format(self.candidate_2, (self.points_2-self.points_1)))

    def ids_candidate(self):
        result = dict(zip(self.ids, self.candidatesofvoters))
        for i in result:
            print(f"The id{i} voted for {result[i]} candidate!")

    def voting(self):
        while self.condition:
            print(f"The candidates are {self.candidate_1} and {self.candidate_2}!")#displaying the candidates
            self.id = input(f"Enter your 3 digit id (person {self.n}):-")          #message for user id that is unique and of 3 digits
            if len(self.id) >3 or len(self.id) <3:                                 #condition to check whether the id is as required or not!
                print("Id is incorrect!Try again")
            elif self.id in self.ids:                                              #checking whether the same person is casting vote twice
                print("Same person Can't vote twice!(same id)!")
            else:                                                              
                self.ids.append(self.id)                                           #making a list of voter's id
                self.candidate =input("Whom you want to cast the vote?Enter the name:-") #votes are casting
                if self.candidate == "a" or self.candidate == "b":
                    self.candidatesofvoters.append(self.candidate)
                    self.n+=1
                    if self.candidate == self.candidate_1:                         #votes are added to the candidate of voter's choice
                        self.points_1+=1
                    elif self.candidate == self.candidate_2:
                        self.points_2 +=1
                else:
                    print("The name you entered is not a candidate!")              #checking if the user enter's wrong candidate name
            if self.n >=11:                                                        #votes are casting only of 10 voters
                self.condition=False 
            print("")
        self.result()
        self.ids_candidate()

voting_obj = Voting_program()                                                      #object of the voting_program
voting_obj.display()                                                               #calling the methods
voting_obj.candidates()
