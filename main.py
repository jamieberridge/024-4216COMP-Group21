userInput = input("choose (1)weekend alcohol consumption and grade(2)male and female grades")

if userInput == "1":
    with open("grade-alcoholConsumption.py") as file:
        exec(file.read())
elif userInput == "2":
    with open("start.py") as file:
        exec(file.read())

