def super_digit(n):
    # Base case: if single digit, return as int
    if len(n) == 1:
        return int(n)
    else:
        # Sum all digits and call function again (recursion)
        digit_sum = sum(int(d) for d in n)
        return super_digit(str(digit_sum))

# Input from user
num = input("Enter number: ")

# Compute super digit
result = super_digit(num)

# Output result
print(f"The super digit of {num} is {result}.")
