from tkinter import *
from Materia import Materia

#Arquivo para ser importado
filename = "test.txt"

#Inicializa lita com todas materias
allmat = Materia.allmat(filename)

#Criando Interface Grafica
tentativa = Tk()
tentativa.geometry("900x900")
tentativa.title("Auxilio em matricula")
var = dict()

#variaveis criadas para auxiliar
linhacheck = 1
columncheck =1

#criar grade com o maior numero de materias
def Maxmat(event):
    pass

#criar grade com o numero N de materias
def onButtonClick():
    pass


#Cria opcoes para a pessoa escolher como montar a grade
#N SEI PQ Q N TA DANDO PRA PEGAR
#A VARIAVEL GLOBAL FOI O UNICO JEITO Q EU CONSGUI.....
def createoptions():
    grades = Label(tentativa, text='Selecione estilo:')
    grades.grid(row=17, column=1)

    max = Button(tentativa, text="Grade com mais materias", background = 'orange')
    max.bind("<Button-1>", Maxmat)
    max.grid(row=18, column=1)

    max = Button(tentativa, text="Grade com N materias", background='orange', command=onButtonClick)
    max.grid(row=18, column=2)

    global vai
    vai = IntVar()
    en = Entry(tentativa, textvariable=vai)
    en.grid(row=18, column=3)


#Verifica quais materias estao able e mostra elas na tela
def ablemat(linha, coluna):
    for x in allmat:
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
    for x in allmat:
        if (var[x].get()):
            x.setDone()
    ablemat(10,1)

#Montando grid de check boxes
for x in allmat:
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