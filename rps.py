rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
uinput = int(input("What do you choose? Type'0'for Rock, '1' for Paper or '2' for Scissors.\n"))
if uinput == 0:
  print(f"user chose: {rock}")
elif uinput == 1:
  print(f"user chose: {paper}")
elif uinput == 2:
  print(f"user chose: {scissors}")
else :
  print("INVALID")
  exit()
  

cinput = random.choice(["rock","paper","scissors"])
if cinput == "rock" :
  print(f"computer choose:{rock}")
elif cinput == "paper" :
  print(f"computer choose:{paper}")
else:
  print(f"computer choose:{scissors}")

if (uinput == 0 and cinput == "paper") or (uinput == 1 and cinput == "scissors") or (uinput == 2 and cinput == "rock"):
  print("You lose!")
elif (uinput == 0 and cinput =="scissors") or (uinput == 1 and cinput == "rock") or (uinput == 2 and cinput == "paper") :
  print("You Win")
else :
  print("Its a draw")