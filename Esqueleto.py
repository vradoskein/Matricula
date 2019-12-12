from tkinter import *
from Materia import *

#Arquivo para ser importado
filename = "test.txt"

#Inicializa lita com todas materias
all = Materia.allmat(filename)

#Criando Interface Grafica
tentativa = Tk()
tentativa.geometry("900x900")
tentativa.title("Auxilio em matricula")
var = dict()

#variaveis criadas para auxiliar
linhacheck  = 1
columncheck = 1

#Cria grade priorizando as materias com maior peso
def prior():
    gradelist = Materia.prior()
    criagrade(gradelist, 19, 1)
    pass

#criar grade com o maior numero de materias
#Coloracao eh NP completo, entao vamo ver como vai ser...
def maxmat():
    Materia.ablelist()
    gradelist = Materia.montarGrafo()
    criagrade(gradelist, 19, 1)
    pass

#criar grade com o numero N de materias
#N tava rolando deixar o metodo sem parametros. Resolver
def limited():
    pass

#Cria a grade de acordo com a lista recebida
def criagrade(gradelist, linha, coluna):
    for g in gradelist:
        var[x] = IntVar()
        check2 = Button(tentativa, text=g.name, background='green', command=var[x])
        check2.grid(row=linha, column=coluna, sticky=W)

        linha += 1
        if linha == 25:
            coluna += 1
            linha = 19

#Cria opcoes para a pessoa escolher como montar a grade
#N SEI PQ Q N TA DANDO PRA PEGAR
#A VARIAVEL GLOBAL FOI O UNICO JEITO Q EU CONSGUI.....
def createoptions():
    grades = Label(tentativa, text='Selecione estilo:')
    grades.grid(row=17, column=1)

    max = Button(tentativa, text="Grade Priorizando mas Importantes", background='orange', command=prior)
    max.grid(row=18, column=1)

    max = Button(tentativa, text="Grade com mais materias", background = 'orange', command=maxmat)
    max.grid(row=18, column=2)

    max = Button(tentativa, text="Grade com N materias", background='orange', command=limited)
    max.grid(row=18, column=3)

    global vai
    vai = IntVar()
    en = Entry(tentativa, textvariable=vai)
    en.grid(row=18, column=4)


#Verifica quais materias estao able e mostra elas na tela
#Considerando cores para as materias mais importantes
def ablemat(linha, coluna):
    for x in all:
        x.isable()
        if x.able and not x.done:
            var[x]=IntVar()
            if x.peso > 3 :
                check2 = Button(tentativa, text=x.name, background = 'red' ,command=var[x])
                check2.grid(row=linha, column=coluna, sticky=W)
            elif x.peso > 0:
                check2 = Button(tentativa, text = x.name, background = 'yellow', command = var[x])
                check2.grid(row=linha, column = coluna, sticky=W)
            else:
                check2 = Button(tentativa, text=x.name, command=var[x])
                check2.grid(row=linha, column=coluna, sticky=W)
            linha += 1
            if linha == 16:
                coluna += 1
                linha = 10

    createoptions()

#seta pra done as materias ja feitas
def Lecheck(event):
    for x in all:
        if (var[x].get()):
            x.setDone()
    ablemat(10,1)

#Montando grid de check boxes
for x in all:
    var[x]=IntVar()
    check1 = Checkbutton(tentativa, text = x.name,  variable=var[x])
    check1.grid(row=linhacheck, column=columncheck, sticky=W)
    linhacheck = linhacheck+1
    if linhacheck == 7:
        columncheck += 1
        linhacheck = 1


#botão para iniciar o evento de Lecheck
button_concluir = Button(tentativa, text="Concluir materias")
button_concluir.bind("<Button-1>", Lecheck)
button_concluir.grid(row=8, column=1)
label = Label(tentativa, text = 'MATERIAS DISPONIVEIS:')
label.grid(row = 9, column= 1)


tentativa.mainloop()