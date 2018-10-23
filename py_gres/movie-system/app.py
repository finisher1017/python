from movie import Movie
from user import User

current_user = User("Jonathan")
my_movie = Movie("The Godfather", "Crime/Drama", True)
another_movie = Movie("The Godfather: Part II", "Crime/Drama", True)
third_movie = Movie("Three Billboards", "Drama/Dark Comedy", False)

#current_user.movies.append(my_movie)
#current_user.movies.append(another_movie)
#current_user.movies.append(third_movie)

current_user.add_movie(name, genre, False)

print(current_user)
print(current_user.movies)
print(current_user.watched_movies())

user.save_to_file()
