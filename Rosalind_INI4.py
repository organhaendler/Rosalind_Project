# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

def input_is_int():
    while True:
        try:
            user_input = int(input("Enter an integer smaller 10000:"))
            if user_input > 9999:
                print("This number is not smaller 1000!")
                continue
        except:
            print("This is not an integer!")
        else:
            return user_input

def check_if_a_is_smaller_b(a, b):
    if a<b:
        print("Input is OK!")
    else:
        print("The first value needs to be smaller than the second one!")
        main()

def calculate_sum_of_odds(a, b):
    sum_of_odds = 0
    for i in range(a, b+1):
        if i%2 == 1:
            sum_of_odds= sum_of_odds + i
    return sum_of_odds

def main():
    a = input_is_int()
    b = input_is_int()
    check_if_a_is_smaller_b(a, b)
    sum_of_odds = calculate_sum_of_odds(a, b)
    print(sum_of_odds)

if __name__ == '__main__':
    main()