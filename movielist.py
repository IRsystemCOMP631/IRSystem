import imdb

ia = imdb.Cinemagoer()

top = ia.get_top250_movies()


with open('movie_list.txt', 'w', encoding='utf-8') as outfile:

    for movie in top:
        outfile.write(movie.get("title"))
        outfile.write("\n")


