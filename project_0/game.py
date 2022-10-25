import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100\n"))

    if predict_number > number:
        print("The number must be less!\n")
    elif predict_number < number:
        print("The number must be greater!\n")
    else:
        print(f"You guessed the number!  This number = {number}, for {count} attempts")
        break