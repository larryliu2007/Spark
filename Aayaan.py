teams = {}

while True:
    userInput = input("What would you like to do?\n "
                      "1. Add a Team\n "
                      "2. Update Team Score\n "
                      "3. Inquire a Team's Score\n "
                      "4. Remove a Team\n "
                      "5. Exit Program\n ")

    if userInput == "1":
        # Add a team
        print("Your choice is 1")
        teamName = input("Input the name of the team you want to add: ")
        while True:
            try:
                teamScore = int(input("Input the score of the team you want to add: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the score.")
        teams[teamName] = teamScore
        print(teams)

    elif userInput == "2":
        # Update score of a current team
        print("Your choice is 2")
        teamName = input("Input the name of the team whose score you'd like to update: ")
        if teamName in teams:
            while True:
                try:
                    teamScore2 = int(input("What would you like to add to their score? "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number to add to the score.")
            teams[teamName] += teamScore2
            print(teams)
        else:
            print("Team not found. Please enter a valid team name.")

    elif userInput == "3":
        # Find a team's score
        print("Your choice is 3")
        teamName = input("Input the name of the team whose score you'd like to inquire: ")
        if teamName in teams:
            print(f"The score of {teamName} is {teams[teamName]}.")
        else:
            print("Team not found. Please enter a valid team name.")

    elif userInput == "4":
        # Remove an existing team
        print("Your choice is 4")
        teamName = input("Input the name of the team you want to remove: ")
        if teamName in teams:
            del teams[teamName]
            print(f"{teamName} has been removed.")
            print(teams)
        else:
            print("Team not found. Please enter a valid team name.")

    elif userInput == "5":
        # Exit program
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
