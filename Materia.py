class Materia:
    #Estrutura de materias e construtor
    def __init__(self, name, reqs):
        self.name = name
        self.reqs = reqs
        self.done = False
#       self.horario = horario

    #settar estado da materia para done
    def setDone(self):
        self.done = True

    #Recebe uma lista de materias ja feitas,
    #Remove dos requisitos de cada materia as ja feitas
    #True se n tiver pre requisito
    #False se tiver pre requisito
    def aptas(self, done):
        for item in done:
            if item in self.reqs:
                self.reqs.remove(item)

        if self.reqs:
            return False
        else:
            return True

    #Metodo para criar a lista de materias
    def allmat(filename):
        file = open(filename, "r")
        matlist = []

        for linha in file:
            mat = linha.split(":")
            requisitos = mat[1].split(",")
            matlist.append(Materia(mat[0], requisitos))

        return matlist
