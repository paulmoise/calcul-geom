from forme_geometric import FormeGeometrique


class Carre(FormeGeometrique):

    def __init__(self, nom, cote):
        super().__init__()

        self.name = nom
        self.cote = cote

    def surface(self):
        return self.cote ** 2

    def perimetre(self):
        return self.cote * 4

    def __str__(self):
        return f"Carre {self.name} de cote ({self.cote})"