import math
import random
import json

data = "" # loop exit condition
nPlayers = 2
nDice = 0
nSides = 0


"""
while(data != "0" and data != "end"): # to loop the function as desired

    print("Roll the dice! syntax: '!2d12', '!1D6' (dice < 9 &&0 sides > 1)\n0 to exit\n---------") # instructions
    print("command: $ ",end="") #prompt
    data = input() # receive input

    if (data == "0" or data == "exit"): # if exit command (additional option to terminate)
        break # end loop
    elif (data[:1] == "!" and len(data) > 3): # if first char is '!' and there's more than 3 characters
        nDice = int(data[1]) # number of dice is the value at position 2 (after '!'); nDice < 9 - FIX: catch this error
        nSides = int(data[3:]) # number of sides is the value of all of the remaining digits from position 4 on
    else: # default response if '!' not found
        print("Command not recognized.\n", '"'+data+'"? What the heck is "'+data+'" anyways?') 
        print("Looks like jumbled up characters to me...")
 """      

def rollDice(nDice,nSides):
    sum = 0
    while (nDice>0): # nDice times
        roll = random.randint(1,nSides)
        print(roll,end=" ") # roll and output random int based on how many sides to the die
        sum += roll
        nDice -= 1 # decrement to break loop after all dice are rolled
    print("= ",sum,"\t d",nSides,"\n_________\n",sep="") # print sum
    return sum

with open('charSheets.json') as json_file:
    char1 = json.load(json_file)

i = 0
while i < nPlayers:
    print(char1["players"][i]["skills"]['str'])
    i += 1

def skillTest(id, skill, roll):
    level = char1["players"][id]["skills"][skill]
    if roll >= level:
        return("{} lvl {} check: rolled: {} -> Succeed!".format(skill, level, roll))
    else:
        return("{} lvl {} check: rolled: {} -> Fail.".format(skill, level, roll))

roll1 = rollDice(1,100)
print(roll1)
test1 = skillTest(0, "str", rollDice(1,100))
print(test1)
test2 = skillTest(1, "str", rollDice(1,100))
print(test2)
test3 = skillTest(0, "dodge", rollDice(1,100))
print(test3)
test4 = skillTest(0, "computeruse", rollDice(1,100))
print(test4)
# end

"""
while(data != "0" and data != "end"): # to loop the function as desired

        nDice = 0
        nSides = 0
        sum = 0

        print("Roll the dice! syntax: '!2d12', '!1D6' (dice < 9 &&0 sides > 1)\n0 to exit\n---------") # instructions
        print("command: $ ",end="") #prompt
        data = input() # receive input

        if (data == "0" or data == "exit"): # if exit command (additional option to terminate)
            break # end loop
        elif (data[:1] == "!" and len(data) > 3): # if first char is '!' and there's more than 3 characters
            nDice = int(data[1]) # number of dice is the value at position 2 (after '!'); nDice < 9 - FIX: catch this error
            nSides = int(data[3:]) # number of sides is the value of all of the remaining digits from position 4 on
        else: # default response if '!' not found
            print("Command not recognized.\n", '"'+data+'"? What the heck is "'+data+'" anyways?') 
            print("Looks like jumbled up characters to me...")

        while (nDice>0): # nDice times
            roll = random.randint(1,nSides)
            print(roll,end=" ") # roll and output random int based on how many sides to the die
            sum += roll
            nDice -= 1 # decrement to break loop after all dice are rolled
        print("= ",sum,"\t d",nSides,"\n_________\n",sep="") # print sum
"""