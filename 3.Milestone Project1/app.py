MENU_PROMPT = "\n Enter a for Adding new movie, l for list of movies, f for find a movie and q for quit the list : "

movies = []

#fUNCTIONAdding Movie to the list
def add_movie():
    title = input("Enter a Movie title name : ")
    director = input("Enter a movie director you wish to do : ")
    year = input("Enter Movie release year : ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


#Function OF list of movies
def list_movie():
    for movie in movies:
        print_movie(movie)
    # print(f" movie not available at the moment")


#Function OF find of movies
def find_movie():
    search_title = input("Enter movie title you're looking for : ")
    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)
        # else:
        #     print(f"{search_title} movie not available at the moment")

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")

user_options = {
    "a" : add_movie,
    "l" : list_movie,
    "f" : find_movie
}
#selection user options
def Menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Please Enter from the list of a l f q : ")
        selection = input(MENU_PROMPT)

Menu()

