num = int(input("Enter a number: "))

faculteit = 1


if num < 0:
    print("Sorry, faculteit does not exist for negative numbers")
elif num == 0:
    print("De faculteit of 0 is 1")
else:
    for i in range(1,num + 1):
        faculteit = faculteit*i
    print("De faculteit of",num,"is",faculteit)
