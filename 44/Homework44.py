Name = 'Leizer Feldberger'
Address = '87 bath st'
Friends = ['tom doe','jake frank','ted cruze','joe biden']
print(f'Name: {Name} Address: {Address} Friends: {Friends}')
print(Name[::3])
print(Friends[-2][1:-1:])
for i in range(1, 11):
    for j in range(1, 11):
      print(i, 'x', j, '=', i*j)
import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")