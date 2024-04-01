# List of visualisations formatted in a list to allow for easy manipulation 
listOfVisualisations = [
    # Bailey's trends
    "(1) Weekend alcohol consumption and grade", 
    "(2) Age distribution of students",
    "(3) Relationship Status by Parental Cohabitation",
    "(4) Travel vs study time",

    "(0) Exit"
    ]

# Loop to display the visualisation options and allow the user to select another option or exit
while True:
    print("Choose a visualisation from the following: ")
    for x in listOfVisualisations:  
        print(x)

    userInput = input("- ")
    if userInput == "0":
        break
    elif userInput == "1":
        with open("grade-alcoholConsumption.py") as file:
            exec(file.read())
    elif userInput == "2":
        with open("histogram.py") as file:
            exec(file.read())
    elif userInput == "3":
        with open("romantic.py") as file:
            exec(file.read())
    elif userInput == "4":
        with open("studyTime.py") as file:
            exec(file.read())