class Materia:
    #Estrutura de materias e construtor
    def __init__(self, name, reqs):
        self.name = name
        self.reqs = reqs
        self.done = False
        self.able = False
#       self.horario = horario

    #settar estado da materia para done
    def setDone(self):
        self.done = True

    #Pega cada materia q ja foi feita, percorre os requisitos de todas materias e tira elas da lista de requisitos
    #n ficou bom, mto o q melhorar
    def isable(self, allmat):
        for mat in allmat:
            if mat.done:
                for m in allmat:
                  if mat.name in m.reqs:
                    m.reqs.remove(mat.name)

        #resolvendo um pequeno problema de listas com elementos vazios ['']
        for mat in allmat:
            if all(mat.reqs):
                pass
            else:
                mat.reqs.clear()
                mat.able = True

        #verifica se a lista de requisitos esta vazia, para saber se pode fazer a materia
        if self.reqs:
            self.able = False
        else:
            self.able = True


    #Metodo para criar a lista de materias
    def allmat(filename):
        file = open(filename, "r")
        matlist = []

        for linha in file:
            mat = linha.split(":")
            requisitos = mat[1].rstrip("\n").split(",")
            matlist.append(Materia(mat[0], requisitos))

        return matlist
