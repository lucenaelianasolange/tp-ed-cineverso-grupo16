class Clientes:
    def __init__(self, dni, name):
        self._id = dni
        self._name = name
        self._historia = []

    def __str__(self):
        return f"identificación {self._id} nombre: {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 0 :
            self._name = value

        else:
            raise ValueError("nombre no puede ser vacio")


    @property
    def historil(self):
        if len(self._historia) > 0:
            for i in self._historia:
                print(i)
        else:
            print("no hay historial de busqueda")

    @historil.deleter
    def historil(self):
        self._historia.clear()
        print("historial borrado")

    def watchMovie():pass

    def removeMovie():pass

    def rateMovie():pass

    def recommendMovie():pass

    def recommendHistorial():pass