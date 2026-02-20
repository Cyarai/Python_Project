import time

password = '123'

print("Cracking Password")

for i in range(1000):
    guess = str(i).zfill(3)
    print("trying", guess)
    time.sleep(0.05)

    if guess == password:
        print("Password foundd and it was ", guess)
        break