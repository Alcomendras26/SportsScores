# Create an Intramural score tracker

# Each team entry is a list that includes
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against

# You will ask how many teams are playing.
# Loop that many times, create a team and set all scores to 0, then append it to your list of teams
# Start an infinite loop for main menu
#   1) Add score
#   2) See Team stats
#   3) See Overall Standings
#   4) Quit

#
#   2) Print a list of team names.
#       Once the user selects, Print out their stats

#   3) Print out the teams in order from most team points to least
#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.

#   4) Say goodbye and break out of the loop


teams=[]
#Number of teams
print("How many teams are playing?")
number_of_teams = int(input())
for i in range(number_of_teams):
    name = input("Team name: ")
    team= [name,0,0,0,0,0]
    teams.append(team)

#Menu

for i in range(number_of_teams):
    print(teams[i])

print("MENU")

print("1:Add Score")
print("2:Team Stats")
print("3:Standings")
print("4:Exit")

Choice=input()

if Choice == "1":
    print("Which teams competed?")
# 1) Enter team 1, team 2, goals for team 1, goals for team 2
#       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie

    for i in range(number_of_teams):
        print(f"{i+1}: {teams[i][0]}")
    selected_team1=int(input("Team number: "))-1

    print(f"You chose {teams[selected_team1][0]}")

    selected_team2 = int(input("Team number: ")) - 1

    print(f"You chose {teams[selected_team2][0]}")

    print("How many wins for each team?")

    wins1=int(input("Wins1:"))
    teams[selected_team1][5]+=wins1


    wins2 = int(input("Wins2:"))
    teams[selected_team2][5] += wins2


    print("How many losses for each team?")

    losses1 = int(input("Losses1:"))
    teams[selected_team1][4] += losses1

    losses2 = int(input("Losses2:"))
    teams[selected_team2][4] += losses2



# Creating lists
#empty = []
#nums = [5]
#mixed = [1, "two", 3.0, True]
# List methods
#nums.append("x") # Add to end
#nums.insert(0, "y") # Insert at index 0
#nums.extend(["z", 5]) # Extend with iterable
#nums.remove("x") # Remove first "x"
#last = nums.pop() # Pop returns last element
# List indexing and checks
#fruits = ["banana", "apple", "orange"]
#fruits[0] # "banana"
#fruits[-1] # "orange"
#"apple" in fruits # True
#len(fruits) # 3