import numpy as np

from Graph import Graph


class Materia:
    matlist =[]
    ablesmat = []

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

    #Monta lista com as materia aptas
    @classmethod
    def ablelist(cls):
        #Organiando para a materia mais "importante" seja o primeiro vertice
        #Para q ela tenha a cor 0
        for mat in Materia.matlist:
            if mat.able and not mat in Materia.ablesmat and not mat.done:
                Materia.ablesmat.append(mat)
            elif mat.able and not mat in Materia.ablesmat and not mat.done:
                if Materia.ablesmat:
                    Materia.ablesmat.insert(0, mat)
                else:
                    Materia.ablesmat.append(mat)

    @classmethod
    def prior(cls):
        Materia.ablelist()
        priorlist = Materia.ablesmat
        priorlist.sort(key=lambda x: x.peso, reverse=True)

        copylist = []

        copylist.append(priorlist[0])
        for x in priorlist:
            crt = True
            for y in copylist:
                if Materia.intersection(x.horario, y.horario):
                    crt = False
                    break
                else:
                    pass
            if crt:
               copylist.append(x)

        return copylist

    @classmethod
    def limited(cls, num):
        Materia.ablelist()
        priorlist = Materia.ablesmat
        priorlist.sort(key=lambda x: x.peso, reverse=True)

        copylist = []

        copylist.append(priorlist[0])
        for x in priorlist:
            crt = True
            for y in copylist:
                if Materia.intersection(x.horario, y.horario):
                    crt = False
                    break
                else:
                    pass
            if crt and len(copylist) < num:
               copylist.append(x)

        return copylist

    @classmethod
    def intersection(cls, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

        #Monta a Matriz para resolver a coloracao

    @classmethod
    def montarMatriz(cls):
        Materia.ablelist()
        tam = len(Materia.ablesmat)
        matriz = np.zeros((tam, tam))
        ext, int = 0, 0
        for x, matext in enumerate(Materia.ablesmat):
            for y, matint in enumerate(Materia.ablesmat):
                if Materia.intersection(matext.horario, matint.horario):
                    matriz[x][y] = 1
        return matriz

    #Chama o metodo para construir o grafo
    #e tambem resolver a coloracao
    #m = 5 so para ter um controle, indica o numero maximo
    #de horarios que uma materia pode ter.
    @classmethod
    def montarGrafo(cls):
        matriz = Materia.montarMatriz()

        g = Graph(len(matriz[1]))
        g.graph = matriz
        m = 5
        teste = g.graphColouring(m)


        #Melhorar com ctz
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        for i, mat in enumerate(Materia.ablesmat):
            if teste[i] == 1:
                list1.append(mat)
            elif teste[i] == 2:
                list2.append(mat)
            elif teste[i] == 3:
                list3.append(mat)
            elif teste[i] == 4:
                list4.append(mat)
            elif teste[i] == 5:
                list5.append(mat)


        tamanhos = [len(list1), len(list2), len(list3), len(list4), len(list5)]

        t_max = max(tamanhos)
        t_pos = tamanhos.index(t_max)

        if t_pos == 0:
            return list1
        elif t_pos == 1:
            return list2
        elif t_pos == 2:
            return list3
        elif t_pos == 3:
            return list4
        elif t_pos == 4:
            return list5
