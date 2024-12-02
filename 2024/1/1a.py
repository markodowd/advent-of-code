total_distance = 0

left_values = []
right_values = []

with open("input.txt", "r") as file:
    for line in file:
        left, right = map(int, line.split())

        left_values.append(left)
        right_values.append(right)

left_values = sorted(left_values)
right_values = sorted(right_values)

for left, right in zip(left_values, right_values):
    total_distance += abs(left - right)

print("Total: ", total_distance)
