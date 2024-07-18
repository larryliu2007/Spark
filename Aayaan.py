userInput = input("What would you like to do?\n "
                  "1. Add a Team\n "
                  "2. Update Team Score\n "
                  "3. Inquire a Team's Score\n "
                  "4. Remove a Team\n "
                  "5. Exit Program\n ")

teams = {}

while userInput != 5:

    if userInput == "1":
        #Add a team
        print("Your choice is 1")

        teamName = input("Input the name of the team you want to add. ")
        teamScore = int(input("Input the score of the team you want to add. "))
        teams[teamName] = teamScore
        print(teams)


    elif userInput == "2":
        #Update score of a current team
        print("Your choice is 2 ")
        teamName = input("Input the name of the team who's score you'd like to add to. ")
        teamScore2 = int(input("What would you like to add to their score? "))
        teams[teamName] += teamScore2
        print(teams)

    elif userInput == "3":
        #Find a team's score
        print("Your choice is 3 ")
        teamName = input("Input the name of the team whose score you'd like to inquire. ")
        print(teams[teamName])


    elif userInput == "4":
        #Remove an existing team
        print("Your choice is 4 ")
        teamName = input("Input the name of the team you want to remove. ")
        del teams[teamName]
        print(teams)

    elif userInput == "5":
        #Exit program
        print("Your choice is 5 ")
        break

    userInput = input("What would you like to do?\n "
                  "1. Add a Team\n "
                  "2. Update Team Score\n "
                  "3. Inquire a Team's Score\n "
                  "4. Remove a Team\n "
                  "5. Exit Program\n ")