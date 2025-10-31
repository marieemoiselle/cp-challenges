# dictionaries for numbers and words
ones = {
    "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, 
    "seven":7, "eight":8, "nine":9, "ten":10, "eleven":11, "twelve":12, 
    "thirteen":13, "fourteen":14, "fifteen":15, "sixteen":16, 
    "seventeen":17, "eighteen":18, "nineteen":19
}

tens = {
    "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60,
    "seventy":70, "eighty":80, "ninety":90
}

scales = {"hundred":100, "thousand":1000, "million":1000000}

def parse_number(text):
    text = text.replace("-", " ") # spaces will replace dash
    words = text.split()
    total = 0
    current = 0

    for word in words:
        if word in ones:
            current += ones[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= 100
        elif word in ["thousand", "million"]:
            current *= scales[word]
            total += current
            current = 0
    total += current
    return total

# get user input
text_input = input("Enter string: ")

# convert to number
number = parse_number(text_input)

print(f"\nThe number is: {number}.")