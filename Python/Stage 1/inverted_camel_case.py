# user input
input_str = input("Enter string in CamelCase: ")

result = ""

for i in range(len(input_str)):
    # space before uppercase letters (except the first one)
    if input_str[i].isupper() and i != 0:
        result += " "
    
    # invert the case
    if input_str[i].isupper():
        result += input_str[i].lower()
    else:
        result += input_str[i].upper()

# show result
print(result)