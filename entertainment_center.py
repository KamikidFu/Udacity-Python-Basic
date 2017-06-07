import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","Storyline", 
		"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
		"https://www.youtube.com/watch?v=vwyZH85NQC4")
movie2 = media.Movie("m2N","m2S","m2P","m2T")
movie3 = media.Movie("m3N","m3S","m3P","m3T")
#print(toy_story.storyline)
#toy_story.show_trailer()
movies = [toy_story, movie2, movie3]
fresh_tomatoes.open_movies_page(movies)
