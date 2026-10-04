# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    #seconds_to_hms(3661)   # returns "1:01:01"
    #seconds_to_hms(59)     # returns "0:00:59"
    #seconds_to_hms(7325)   # returns "2:02:05"
    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"

def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    #admission_price(3) # returns 0.0
    #admission_price(10)   # returns 8.0
    #admission_price(30)   # returns 15.0
    #admission_price(70)   # returns 10.0
    if age < 5:
        return 0 
    elif age <= 12:
        return 8
    elif age <= 64:
        return 15
    else:
        return 10



def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    #sum_multiples(10)   # returns 23
    #sum_multiples(20)   # returns 78
    #sum_multiples(1)    # returns 0
    sum = 0
    for number in range(limit): 
        if number % 3 == 0:
            sum += number
        elif number % 5 == 0:
            sum += number
    return sum
def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    #total_of_positives([1, -2, 3, -4, 5])   # returns 9
    #total_of_positives([-1, -2])            # returns 0
    #total_of_positives([10, 20])            # returns 30
    total = 0

    for n in numbers:
        if n > 0:
            total += n;

    return total;

def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    # print(seconds_to_hms(3661))            # 1:01:01
    # print(admission_price(10))             # 8
    # print(sum_multiples(10))               # 23
    # print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()