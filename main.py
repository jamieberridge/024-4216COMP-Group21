userInput = input("choose (1)weekend alcohol consumption and grade(2)age distribution of students (3)Relationship Status by Parental Cohabitation (4)travel vs study time")

if userInput == "1":
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

