n = int(input("Enter n: "))

if n == 0:
    tribonacci = 0;
elif n == 1 or n == 2:
    tribonacci = 1
else:
    t0, t1, t2 = 0, 1, 1
    for i in range(3, n + 1):
        t_next = t0 + t1 + t2
        t0, t1, t2 = t1, t2, t_next
    tribonacci = t2

print(f"Element {n} of the Tribonacci Sequence is {n}.")