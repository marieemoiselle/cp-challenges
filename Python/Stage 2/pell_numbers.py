n = int(input("Enter n: "))

if n == 1:
    pell = 1
else:
    pell_0, pell_1 = 0, 1
    pell = 0
    for i in range(2, n + 1):
        pell = 2 * pell_1 + pell_0
        pell_0, pell_1 = pell_1, pell

print(f"Element {n} of the Pell Number Sequence is {pell}.")