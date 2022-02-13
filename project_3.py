library = {
    'Harry Potter': 6,
    'Mumi trolles': 9,
    'Alisa': 4 
}

book = input("Enter book(stop - ends the program): ")

while book != "stop":
    if book in library:
        if library[book] > 0:
            library[book] -= 1
            print("You took the book:", book)
        elif library[book] <= 0:
            print("We no longer have such books!")
    elif book not in library:
        library[book] = 0
        library[book] += 1
        print("You have returned the book:", book)

    book = input("Enter book(stop - ends the program): ")

print(library)