# 🧠📓Engage & Apply: Write a Python program that prints all the even numbers between 1 and 20 using a while loop. (Project 1)
# Initialize the variable
num = 2
# Set up the while loop
while num <= 20:
    print(num)  # Print the current number
    num += 2    # Increment the number by 2 to get the next even number


# 👾💻Final Challenge: Write a Python program that processes a range of numbers from 1 to 30. The program should do the following: (Final Challenge)
# Loop through numbers from 1 to 30
for num in range(1, 31):
    if num > 25:  # Stop the loop if the number is greater than 25
        break
    if num % 3 == 0:  # Skip the numbers divisible by 3
        continue
    print(num)  # Print the current number
