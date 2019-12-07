from tkinter import *
from Materia import *
from Inter import *

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

#seta pra done as materias ja feitas
def Lecheck(event):
    for x in allmat:
        if (var[x].get()):
            x.setDone()
    for a in allmat:
        print(a.name, a.reqs, a.done)

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


tentativa.mainloop()