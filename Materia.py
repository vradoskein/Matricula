class Materia:
    matlist =[]

    #Estrutura de materias e construtor
    def __init__(self, name, reqs, horario):
        self.name = name
        self.reqs = reqs
        self.done = False
        self.able = False
        self.peso = 0
        self.horario = horario

    #settar estado da materia para done
    def setDone(self):
        self.done = True

    #Pega cada materia q ja foi feita, percorre os requisitos de todas materias e tira elas da lista de requisitos
    #n ficou bom, mto o q melhorar
    def isable(self):
        for mat in Materia.matlist:
            if mat.done:
                for m in Materia.matlist:
                  if mat.name in m.reqs:
                    m.reqs.remove(mat.name)

        #resolvendo um pequeno problema de listas com elementos vazios ['']
        for mat in Materia.matlist:
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

    #define o peso de cada materia, com base nas outras em que ela eh pre requisito
    def pesos(self):
        for m in Materia.matlist:
            if self.name in m.reqs:
                self.peso += 1

    #Metodo para criar a lista de materias
    def allmat(filename):
        file = open(filename, "r")


        for linha in file:
            mat = linha.split(":")
            requisitos = mat[1].rstrip("\n").split(",")
            horarios = mat[2].rstrip("\n").split(",")
            Materia.matlist.append(Materia(mat[0], requisitos, horarios))

        for mat in Materia.matlist:
            mat.pesos()

        return Materia.matlist
