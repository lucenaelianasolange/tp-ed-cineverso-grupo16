class Pelicula:
    def __init__(self, titulo, director, anio, genero):
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} ({self.anio}) - Dirigida por {self.director}, Género: {self.genero}"

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        self._director = value

    @property
    def anio(self):
        return self._año

    @anio.setter
    def anio(self, value):
        self._año = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    def __repr__(self):
        return f"Pelicula(titulo='{self.titulo}', director='{self.director}', anio={self.anio}, genero='{self.genero}')"
