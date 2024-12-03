import re

results = []
conditional_results = []

def calculate_results(text) -> None:
    pattern = r"mul\(\d+,\d+\)"

    matches = re.findall(pattern, line)
    
    for match in matches:
        numbers = re.search(r"mul\((\d+),(\d+)\)", match)
    
        num1 = int(numbers.group(1))
        num2 = int(numbers.group(2))

        results.append(num1 * num2)


# def calculate_conditional_results(text) -> None:
#    pattern = r"do\(\)(?:(?!don't\().)*?mul\(\d+,\d+\)"
#    
#    matches = re.finditer(pattern, text)
#    
#    for match in matches:
#        mul_matches = re.findall(r"mul\((\d+),(\d+)\)", match.group())
#
#        for num1, num2 in mul_matches:
#            conditional_results.append(int(num1) * int(num2))


with open("input.txt", "r") as file:
    for line in file:
        calculate_results(line)
        # calculate_conditional_results(line)


print("Total: ", sum(results))
# print("Total Conditional: ", sum(conditional_results))

