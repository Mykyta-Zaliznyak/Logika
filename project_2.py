marks = ""
num_symbol = 0

marks = input("Enter marks:")

marks_list = marks.split(" ")

for symbol in marks_list:
    if symbol == "2":
        num_symbol += 1

print(marks_list)
print(num_symbol)