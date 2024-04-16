import os

# List of trends for Bailey
baileyTrends = [
    "Weekend alcohol consumption and grade",
    "Age distribution of students",
    "Relationship Status by Parental Cohabitation",
    "Travel vs study time"
]

# List of trends for Jamie
jamieTrends = [
    "Effect of Internet Access on final grade",
    "Optimal Study Time by final grade",
    "Effect on having a guardian of same sex on grades",
    "Relationship between the parents education level and the students grades",
    "How much does study time improve students on average?",
    "Comparison between how a relationship affects grades of each gender"
]

# List of trends for Lee
leeTrends = [
    "Family and school support's effect on grades",
    "The effect of age on grade average",
    "The effect of attendance on grades",
    "The effect of health on grades",
    "The effect of nursery attendance on the students prospects of going to higher education",
    "The reason for choosing the school and the students prospects of going to higher education",
]

# List of trends for Dom
domTrends = [
    # Names of trends here
]

# Function to display trends
def displayTrends(trends):
    count = 0
    for x in trends:
        count += 1
        print("{0} -- {1}".format(count, x))

# Function to open a file
def openFile(filePath):
    with open(filePath) as file:
        exec(file.read())

# Function to select a trend
def selectTrend(trends, folder):
    displayTrends(trends)
    x = int(input("Which trend would you like to see? \n- "))
    if x >= 1 and x <= len(trends):
        filePath = os.path.join(folder, f'trend{x}.py')
        if os.path.exists(filePath):
            openFile(filePath)
        else:
            print("File not found.")
    else:
        print("Invalid Input")

# Main loop to select whose visualizations to see
while True:
    userInput = input("Whose visualizations do you want to see? \n(1) Bailey's, \n(2) Jamie's, \n(3) Lee's, \n(4) Dom's, \n(5) View Full List, \n(0) Exit \n- ")

    if userInput == '1' or userInput.lower() == 'bailey':
        selectTrend(baileyTrends, 'bailey')
    elif userInput == '2' or userInput.lower() == 'jamie':
        selectTrend(jamieTrends, 'jamie')
    elif userInput == '3' or userInput.lower() == 'lee':
        selectTrend(leeTrends, 'lee')
    elif userInput == '4' or userInput.lower() == 'dom':
        selectTrend(domTrends, 'dom')
    elif userInput == '5' or userInput.lower() == 'all':
        print("Bailey's trends are:")
        displayTrends(baileyTrends)
        print("Jamie's trends are:")
        displayTrends(jamieTrends)
        print("Lee's trends are:")
        displayTrends(leeTrends)
        print("Dom's trends are:")
        displayTrends(domTrends)
        x = input("Press Enter to continue...")
    elif userInput == '0':
        break
    else:
        print("Invalid Input")
