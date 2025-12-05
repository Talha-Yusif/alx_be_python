class Movie:
    def __init__(self,title,director):
        self.title=title
        self.director=director
        self._is_rented=False
    def is_rent(self):
        if self._is_rented==False:
            self._is_rented=True
    def is_return_movie(self):
        if self._is_rented==True:
            self._is_rented=False
    def is_available(self):
        if self._is_rented==False:
            return True
        else:
            return False

class MovieLibrary:
    def __init__(self):
        self._Movies=[]
    def add_movie(self,movie):
        self._Movies.append(movie)
    def rent_movie(self,title):
        for movie in self._Movies:
            if title==movie.title:
                movie.is_rent()
                return
        print(f"{title} cannot be found")

    def return_movie(self,title):
        for movie in self._Movies:
            if title==movie.title:
                movie.is_return_movie()
                return
        print(f"{title} cannot be found")
    
    def list_available_movies(self):
        for movie in self._Movies:
            if movie.is_available():
                print(f"{movie.title} by {movie.director} is avalable")
 


