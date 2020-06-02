# Solutions for Rosalind "Python Village" exercises
# Exercise INI2.1
# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs
#     have lengths a and b.

def user_input_is_int():
    while True:
        try:
            side_length = int(input("Please enter the length of triangle side as an integer:"))
        except:
            print("This is not an integer number!")
        else:
            return side_length


def calculate_hypothenuse_square(a, b,):
    c_square = a**2 + b**2
    return c_square


a = user_input_is_int()
b = user_input_is_int()
c_square = calculate_hypothenuse_square(a, b)
print(c_square)