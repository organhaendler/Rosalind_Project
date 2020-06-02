# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

def input_is_int():
    while True:
        try:
            user_input = int(input("Enter an integer smaller 1000:"))
            if user_input > 999:
                print("This number is not smaller 1000!")
                continue
        except:
            print("This is not an integer!")
        else:
            return user_input

a = input_is_int()
b = input_is_int()
sum_of_odds = int()

for i in range(a, b):
    if i%2:
        print(i)
        sum_of_odds = sum_of_odds + i

print(sum_of_odds)