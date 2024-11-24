#file = open(r"\\LAPTOP-LTVFNBC9\python\Share\Work.txt")
file = open("C:\\Users\Public\Documents\\P1.txt","w")
file.write(("Ready"))
file.close()
read = ""
run = True
print("waiting for other player")
while run:
    file = open(r"\\LAPTOP-LTVFNBC9\python\Share\Work.txt")
    read = file.read()
    file.close()
    if "Ready" in read:
        run = False
import random,time
guess = int(input("Guess a random number between 1 to 10   "))
run = True
while run:
    walk = int(time.ctime()[17:19])
    walk = walk / 2
    if (walk%2) == 0:
        file = open("C:\\Users\Public\Documents\\P1.txt","w")
        file.write((str(guess)))
        file.close()
        run = False

run = True
print("waiting for other player to guess")
while run:
    file = open(r"\\LAPTOP-LTVFNBC9\python\Share\Work.txt")
    read = file.read()
    file.close()
    if "Ready" in read:
        pass
    else:
        run = False

if guess == int(read):
    print("You lost")
else:
    print("you win ",read)


    
