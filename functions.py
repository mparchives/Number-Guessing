import random

#-----Mututal Functions-----#
#function for menu
def menu():
    print("Select the number options:")
    print("1. User Guess the Number (1-500)")
    print("2. User Guess the Number & Assign Range")
    print("3. System Guess the Number & Assign Range")
    print("4. Quit")
    action = int(input(">"))
    print()
    return action

#function to find the index
def findIndex(num, lyst):
    
    for i in range(len(lyst)):
        if lyst[i] == num:
            return i

#function to assign range
def assignRandNum(option, lyst):
    
    attemp = 0

    if option == 1:
        randNum = random.randint(1,500)
        lyst.append(1)
        lyst.append(500)
        lyst.append(randNum)
        return userGuess(attemp, randNum, lyst)
    
    if option == 2:
        print("Input 2 differnt integers: ")
        int1 = int(input("First Integer: >"))
        int2 = int(input("Second Integer: >"))

        if int1 == int2:
            print("Two numbers can not be the same!")
            return False
        
        elif int1 < int2:
            randNum = random.randint(int1, int2)
        
        else:
            randNum = random.randint(int2, int1)

        lyst.append(int1)
        lyst.append(int2)
        lyst.append(randNum)
        return userGuess(attemp, randNum, lyst)
    
    if option == 3:
        print("Input 2 differnt integers: ")
        int1 = int(input("First Integer: >"))
        int2 = int(input("Second Integer: >"))

        if int1 == int2:
            print("Two numbers can not be the same!")
            return False
        
        else:
            lyst.append(int1)
            lyst.append(int2)
            option = 0
            index = 0
            return sysGuess(attemp, option, index, lyst)


#function to check if the numbers are duplicates
def duplicate(randNum, lyst):

    for i in lyst:
        if i == randNum:
            return False

    return True


#-----Functions for User Guessing-----# 
#function to let user guess
def userGuess(attemp, randNum, userLyst):

    guessNum = int(input("Guess a number: >"))
    attemp += 1
    userLyst.append(guessNum)
    userLyst.sort()

    if guessNum == randNum:
        print(f"Attemp:{attemp}. You got it, the number is {randNum}!")
        return False
    
    else:

        if len(userLyst) <= 3:
            print(f"Attemp:{attemp}. You did not make your guess.")

        else:
            element = findIndex(randNum, userLyst)
            print(f"Attemp:{attemp}. The number is between {userLyst[element-1]} and {userLyst[element+1]}.")
        
        return userGuess(attemp, randNum, userLyst)


#-----Functions for System Guessing-----#
#function to let system guess
def sysGuess(attemp, option, index, sysLyst):
    
    attemp += 1
    sysLyst.sort()

    flag = False
    while flag != True:
        guessNum = random.randint(sysLyst[index], sysLyst[index+1])
        flag = duplicate(guessNum, sysLyst)

    sysLyst.append(guessNum)

    print("Press 1: Correct, 2: Smaller, 3: Larger:")
    option = int(input(f"Attemp: {attemp}. Is it {guessNum}? >"))

    if option == 1:
        print(f"Your number is {guessNum}!")
        return False
    
    elif option == 2:
        index += 0

    elif option == 3:
        index += 1
    
    else: 
        print("Invalid option")
        option = 0

    return sysGuess(attemp, option, index, sysLyst)
