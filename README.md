# SportsScores

Your task is to create a score tracker for Intramurals. For every team, you will create a list that includes the following

## Team List Contents
- Name
- Games Played
- Wins
- Losses
- Ties
- Goals For
- Goals Against

## Order of the program
Start by asking how many teams are playing. Create a loop for the number of teams, read in the names, set all the values to 0, and then append the new team to a list of teams.

```
team=[name,0,0,0,0,0,0]
teams.append(team)
```

Next, you will bring up a loop for the menu.

## Menu Contents
1. Add Score
2. See Team Stats
3. See Overall Standings
4. Quit

## 1) Add score
The user will enter:
- team 1 name
- team 2 name (could also pick from a list)
- goals for team 1
- goals for team 2

  You will then find the teams, update their games played, goals for, goals against, and decide if it's a win, lose or tie.

## 2) See Team Stats
Print out a list of team names. The user will pick one and then you will print out all of the statistics
```
Team: Irish
Games Played: 8
Wins: 5  Losses: 2  Ties: 1
Goals For: 25
Goals Against: 9
```

## 3) See Overall Standings
List the teams in order from most team points to least. 
Team points = Wins * 2 + Ties * 1
If the points are tied, use the higher Goals For
If the Goals For are tied, use the lower Goals Against
If the Goals Against are tied, place them in any order.

## 4) Quit
Say goodbye and break out of the loop
