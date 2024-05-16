#Mututal Functions
from functions import menu, assignRandNum

def main():

    endFlag = False
    while (endFlag != True):
        
        userLyst = []
        sysLyst = []
        menuOpt = menu()
        # 1. User Guess the Number (1-500)
        if menuOpt == 1:
            endFlag = assignRandNum(1, userLyst)        

        # 2. User Guess the Number & Assign Range
        elif menuOpt == 2:
            endFlag = assignRandNum(2, userLyst)

        # # 3. System Guess the Number & Assign Range
        elif menuOpt == 3:
            endFlag = assignRandNum(3,sysLyst)
        # 4. Quit
        elif menuOpt == 4:
            print("Good Bye!")
            endFlag = True
        else:
            print("Invalid option!\n")

        print()

if __name__ == "__main__":
    main()