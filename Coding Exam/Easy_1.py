def sum_even_numbers(user_input):
    m = 0
    for i in range(0, user_input + 1, 2):
        m += i
    return m

user_input = int(input("Please type an integer n: "))
print(sum_even_numbers(user_input))