film_list = {
    "Action" : "Spider Man",
    "Drama" : "Titanic",
    "Romance" : "The Great Gatsby"
}

genre = input("Enter a genre(stop - ends the program): ")

while genre != "stop":
    if genre in film_list:
        print(film_list[genre])
    elif genre not in film_list:
        print("There is no such genre or it is not written in the dictionary")

    genre = input("Enter a genre(stop - ends the program): ")
