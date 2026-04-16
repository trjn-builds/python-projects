import random


def main():
    n = get_num_iterations("Enter number of iterations: ")
    lower_bound = get_lower_bound("Enter the lower bound of numbers: ")
    upper_bound = get_upper_bound("Enter the upper bound of numbers: ", lower_bound)
    numbers = {i: 0 for i in range(lower_bound, upper_bound + 1)}
    num_generate(n, lower_bound, upper_bound, numbers)
    print_prob(n, lower_bound, upper_bound, numbers)


def num_generate(n, lower_bound, upper_bound, numbers):
    for _ in range(n):
        numbers[random.randint(lower_bound, upper_bound)] += 1


def print_prob(n, lower_bound, upper_bound, numbers):
    print("----------------------------------------")
    for num in numbers:
        print(f"{num: >5}: {((100 * numbers[num])/n):6.2f}%, {numbers[num]}")

    print("----------------------")

    exp_total = 0
    for i in range(lower_bound, upper_bound + 1):
        exp_total += i
    exp_total /= (upper_bound+1)-lower_bound
    exp_total *= n
    print(f"Expected Sum: {round(exp_total)}") 

    act_total = 0
    for num in numbers:
        act_total += num*numbers[num]
    print(f"Actual Sum: {act_total}")

    try:
        print(f"% Difference: {abs(100 * (act_total - exp_total) / exp_total):.2f}")
    except (ZeroDivisionError):
        print("% Difference: Inf (Expected Sum = 0)")
    print("----------------------------------------")

    

def get_num_iterations(prompt_iter):
    while True:
        try:
            n = int(input(prompt_iter))
            return n
        except (ValueError, TypeError):
            pass

def get_lower_bound(prompt_lower):
    while True:
        try:
            lower_bound = int(input(prompt_lower))
            return lower_bound
        except (ValueError, TypeError):
            pass

def get_upper_bound(prompt_upper, lower_bound):
    while True:
        try:
            upper_bound = int(input(prompt_upper))
            if upper_bound > lower_bound:
                return upper_bound
        except (ValueError, TypeError):
            pass
    
while True:
    main()