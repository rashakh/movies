import webbrowser
class Movie():
	""" This class initiate a movie and its characteristics """

	VALID_RATINGS = ['G','PG','PG-13','R']

	def __init__(self,title):
		self.title = title

	def storyline(self,storyline):
		self.storyline = storyline

	def poster(self,poster):
		self.poster_image_url = poster

	def trailer(self,trailer):
		self.trailer_youtube_url = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer)
