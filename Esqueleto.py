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

linhacheck = 1
columncheck =1

#Verifica quais materias estao able e mostra elas na tela
def ablemat(linha, coluna):
    for x in allmat:
        if x.able and not x.done:
            var[x]=IntVar()
            check2 = Button(tentativa, text = x.name, command = var[x])
            check2.grid(row=linha, column = coluna, sticky=W)
            linha += 1
            if linha == 16:
                coluna += 2
                linha = 10

#seta pra done as materias ja feitas
def Lecheck(event):
    for x in allmat:
        if (var[x].get()):
            x.setDone()
    ablemat(10,1)

#Montando grid de check boxes
for x in allmat:
    print(x.name,x.reqs, x.peso)
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
label = Label(tentativa, text = 'MATERIAS DISPONIVEIS')
label.grid(row = 9, column= 1)


tentativa.mainloop()