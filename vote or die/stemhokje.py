dominique = 0
zacharia = 0
while True:
    Stem = input("Op wie wil je stemmen?\n") .lower()
    if Stem =="dominique":
        dominique += 1

    if Stem =="zacharia":
        zacharia += 1
    if Stem =="uitslag":
        if dominique > zacharia:
            print ("Dominique heeft gewonnen!")
        if zacharia > dominique:
            print ("Zacharia heeft gewonnen!")
        if zacharia == dominique:
            print("Dominique en zacharia hebben gelijk aantal stemmen")
            break
