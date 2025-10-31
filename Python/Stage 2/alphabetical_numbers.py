def num_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    
    if 1 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        ten_part = tens[n // 10]
        one_part = ones[n % 10]
        return ten_part + ("" if one_part == "" else " " + one_part)
    else:
        return ""
    
nums = list(map(int, input("Enter integers: ").split()))

# removing the trailing zeroes
nums = [x for x in nums if x != 0]

# sorting via their word representations
sorted_nums = sorted(nums, key = lambda x : num_to_words(x))

print("\nSorted List:")
for n in sorted_nums:
    print(n)