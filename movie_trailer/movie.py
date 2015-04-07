class Movie:
    '''
    A class that represents a Movie, with attributes 
    title, storyline, poster_image_url, trailer_youtube_url and release_year.
    This will be used to instantiate multiple Movies and display them in the browser
    '''
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, release_year):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_year = release_year