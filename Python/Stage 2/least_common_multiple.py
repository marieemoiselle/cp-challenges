def get_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def get_lcm(a, b):
    return (a * b) # get_gcd (a, b)

def main():
    n = int(input("Enter number of inputs: "))
    numbers = list(map(int, input(f"Enter {n} inputs: ").split()))

    result = numbers[0]

    # iteration for LCM
    for i in range(1, n):
        result = get_lcm(result, numbers[i])
    
    print(f"LCM = {result}")

if __name__ == "__main__":
    main()