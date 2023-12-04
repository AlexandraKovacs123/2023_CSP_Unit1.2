'''
This file contains a string with a set of CSV (comma separated values) data.

Part 1: Using a loop, break apart the CSV and store each value in a list
    * A loop similar to last unit may help break apart the string

Part 2: Display the contents of the list showing the index number and the value on screen.

Example: If my string is "John,Jill,Dave" then my list should store John in index 0, Jill in index 1, and Dave in index 2
Example Output:
0 - John
1 - Jill
2 - Dave

No values (other than the string I provide) may be hardcoded.
In other words, if I change the string at the top to something different your program should still work.

Note: There are no turtles in this project.  All output should be to the console using print statements.

Good luck - you have the period!

'''

# Initial set of CSV values
csv ="KingsIndian,QueensGambit,TheColle,TheFrench,TheFriedLiver,TheFourKnights"
indexNum = 0
index = 0
myValues = []
value = ""

#Do Part 1 of the challenge below here
for index in range(len(csv)):
    if csv[index] != ",":
        value += csv[index]
        index += 1

    else:
        myValues.append(value)
        value = ""


#Do part 2 of the challenge below here
index = 0
for printTimes in myValues:
    print(index, "-", printTimes)
    index += 1