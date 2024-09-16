"""
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
"""
MAX_ITERATIONS = 10000

def nth_perfect_number(n: int):
    """Returns the nth perfect number"""
    perfect_numbers = []
    current_number = 1
    while current_number < MAX_ITERATIONS:
        # get digits
        str_number = str(current_number)
        digits = list(str_number)
        digits = [int(i) for i in digits]

        # check if it is a perfect number
        if sum(digits) == 10:
            perfect_numbers.append(current_number)
            if len(perfect_numbers) == n:
                return current_number

        current_number += 1
    raise ValueError("Reached maximum number of iterations")

if __name__ == "__main__":
    first_perfect_number = nth_perfect_number(1)
    second_perfect_number = nth_perfect_number(2)
    tenth_perfect_number = nth_perfect_number(10)

    print(first_perfect_number)
    print(second_perfect_number)
    print(tenth_perfect_number)
