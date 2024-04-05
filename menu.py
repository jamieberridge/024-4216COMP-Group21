# List of visualisations formatted in lists to allow for easy manipulation 
baileyTrends = [
    "(1) Weekend alcohol consumption and grade", 
    "(2) Age distribution of students",
    "(3) Relationship Status by Parental Cohabitation",
    "(4) Travel vs study time"
]

jamieTrends = [
    "(5) Effect of Internet Access on final grade",
    "(6) Optimal Study Time by final grade",
    "(7) Effect on having a guardian of same sex on grades",
    "(8) Relationship between the parents education level and the students grades"
    "(9) How much does study time improve students on average?"
    "(10) Comparison between how a relationship affects grades of each gender"
]

leeTrends = [
    # Names of trends here
]

domTrends = [
    # Names of trends here
]

# Loop to display the visualisation options and allow the user to select another option or exit
while True:
    # Display the user with options on whose trends to see
    userInput = input("Whose visualisations do you want to see? \n(1) Bailey's, \n(2) Jamie's, \n(3) Lee's, \n(4) Dom's, \n(5) View Full List, \n(0) Exit \n- ")

    if userInput == ('1'):
        for x in baileyTrends:  
            print(x)
    elif userInput == ('2'):
        for x in jamieTrends:
            print(x)
    elif userInput == ('3'):
        for x in leeTrends:
            print(x)
    elif userInput == ('4'):
        for x in domTrends:
            print(x)
    elif userInput == ('5'):
        for x in baileyTrends+jamieTrends+leeTrends+domTrends:
            print(x)
    elif userInput == ('0'):
        break
    else:
        print("Invalid Input")
        break
    
    # Asking the user what trend they'd like to see from their selected list
    userInput = input("- ")
    if userInput == '0':
        break
    elif userInput == '1':
        with open('bailey/grade-alcoholConsumption.py') as file:
            exec(file.read())
    elif userInput == '2':
        with open('bailey/histogram.py') as file:
            exec(file.read())
    elif userInput == '3':
        with open('bailey/romantic.py') as file:
            exec(file.read())
    elif userInput == '4':
        with open('bailey/studyTime.py') as file:
            exec(file.read())
    elif userInput == '5':
        with open('jamie/internet.py') as file:
            exec(file.read())
    elif userInput == '6':
        with open('jamie/optimalStudyTime.py') as file:
            exec(file.read())
    elif userInput == '7':
        with open('jamie/sameSexGuardian.py') as file:
            exec(file.read())
    elif userInput == '8':
        with open('jamie/parentEducation.py') as file:
            exec(file.read())
    elif userInput == '9':
        with open('jamie/studyTimeImprovement.py') as file:
            exec(file.read())
    elif userInput == '10':
        with open('jamie/.py') as file:
            exec(file.read())