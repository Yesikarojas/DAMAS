import tkinter as tk
import order
from tkinter.font import Font
from tkinter import messagebox
import sys
##### VENTANA DEL PROGRAMA #####

imagenes = {}

ventana = tk.Tk()
ventana.title("Juego de damas")
ventana.iconbitmap("damas.ico")
ventana.geometry('840x576')
ventana.config(background="#FFFFFF")
ventana.resizable(0,0)
gs= order.Order()

imgBoton=tk.PhotoImage(file="./Imagenes/fb.png")
btnList=[]
pixelVirtual = tk.PhotoImage(width=70, height=70)
##### BOTONESINICIO #####


##### FUNCIONES #####

moves = []
contW=12
contB=12
    
# metodo para mostrar los movimientos validos de una ficha sabiendo su posicion
second_click = True
first_move = []
def on_clic():
    global second_click, first_move, moves
    row, col = 0, 0
    # print(row, col)
    x = ventana.winfo_pointerx() - ventana.winfo_rootx()
    y = ventana.winfo_pointery() - ventana.winfo_rooty()
    z = ventana.grid_location(x , y)
    
    if second_click:
        row, col = z[1], z[0]
        first_move = [row, col]

        # calcular los movimientos validos
        if gs.piece[row][col] == "fb":
            if row > 0:
                if col < 7:
                    if gs.piece[row-1][col+1] == "fn" or gs.piece[row-1][col+1] == "rn":
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2])
                    if gs.piece[row-1][col+1] == "--":
                        moves.append([row-1, col+1])
                if col > 0:
                    if gs.piece[row-1][col-1] == "fn"or gs.piece[row-1][col-1] == "rn":
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2])
                    if gs.piece[row-1][col-1] == "--":
                        moves.append([row-1, col-1])
        elif gs.piece[row][col] == "fn":
            if row < 7:
                if col < 7:
                    if gs.piece[row+1][col+1] == "fb" or gs.piece[row+1][col+1] == "rb":
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2])
                    if gs.piece[row+1][col+1] == "--":
                        moves.append([row+1, col+1])
                if col > 0:
                    if gs.piece[row+1][col-1] == "fb" or gs.piece[row+1][col-1] == "rb":
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2])
                    if gs.piece[row+1][col-1] == "--":
                        moves.append([row+1, col-1])
        elif gs.piece[row][col] == "rb":
            if row > 0:
                if col < 7:
                    if gs.piece[row-1][col+1] == "fn" or gs.piece[row-1][col+1] == "rn":
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2])
                    if gs.piece[row-1][col+1] == "--":
                        moves.append([row-1, col+1])
                if col > 0:
                    if gs.piece[row-1][col-1] == "fn"or gs.piece[row-1][col-1] == "rn":
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2])
                    if gs.piece[row-1][col-1] == "--":
                        moves.append([row-1, col-1])
            if row < 7:
                if col < 7:
                    if gs.piece[row+1][col+1] == "fn" or gs.piece[row+1][col+1] == "rn":
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2])
                    if gs.piece[row+1][col+1] == "--":
                        moves.append([row+1, col+1])
                if col > 0:
                    if gs.piece[row+1][col-1] == "fn" or gs.piece[row+1][col-1] == "rn":
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2])
                    if gs.piece[row+1][col-1] == "--":
                        moves.append([row+1, col-1])
        elif gs.piece[row][col] == "rn":
            if row > 0:
                if col < 7:
                    if gs.piece[row-1][col+1] == "fb" or gs.piece[row-1][col+1] == "rb":
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2])
                    if gs.piece[row-1][col+1] == "--":
                        moves.append([row-1, col+1])
                if col > 0:
                    if gs.piece[row-1][col-1] == "fb" or gs.piece[row-1][col-1] == "rb":
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2])
                    if gs.piece[row-1][col-1] == "--":
                        moves.append([row-1, col-1])
            if row < 7:
                if col < 7:
                    if gs.piece[row+1][col+1] == "fb" or gs.piece[row+1][col+1] == "rb":
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2])
                    if gs.piece[row+1][col+1] == "--":
                        moves.append([row+1, col+1])
                if col > 0:
                    if gs.piece[row+1][col-1] == "fb" or gs.piece[row+1][col-1] == "rb":
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2])
                    if gs.piece[row+1][col-1] == "--":
                        moves.append([row+1, col-1])
        # pintar los movimientos validos
        for move in moves:
            print(move[0],move[1], "psibles movimientos")
            btnList[move[0]][move[1]].config(background="#1DA5AC")
        second_click = not second_click
    else:
        #print("segundo click")
        second_click = not second_click
        # mover la ficha si el movimiento es valido
        row2, col2 = z[1], z[0]
        if (row2==first_move[0] and col2==first_move[1]):
            for move in moves:
                btnList[move[0]][move[1]].config(background="#2B2A2A")
        else:
            move_piece(first_move[0], first_move[1], row2, col2)
        moves.clear()

# metodo para mover una ficha si el movimiento es valido
def move_piece(row, col, row2, col2):
    global moves, contB, contW
    print("oreigen:",row, col," destino: ", row2, col2)
    if [row2, col2] in moves:
        
        gs.piece[row2][col2] = gs.piece[row][col]
        gs.piece[row][col] = "--"
        # pintar la nueva posicion de la ficha
        btnList[row2][col2].config(image=imagenes[gs.piece[row2][col2]])
        # limpiar la posicion anterior de la ficha
        btnList[row][col].config(image=pixelVirtual)
        
        # limpiar los movimientos validos anteriores
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    btnList[i][j].config(background="#767272")
                else:
                    btnList[i][j].config(background="#2B2A2A")
        print("se movio una pieza")
    else:
        messagebox.showerror("Juego de Damas","Movimiento inválido")
        for move in moves:
                btnList[move[0]][move[1]].config(background="#2B2A2A")
    contW-=1
    contBlancas.config(text=contW)
    contNegras.config(text=contB)

def cargarFichas():
    global contW, contB
    for indice_i, i in enumerate(gs.piece):
        for indice_j, j in enumerate(i):
            btnList[indice_i][indice_j].config(state='normal')
            if j != "--":
                btnList[indice_i][indice_j].config(image=imagenes[j])
            else:
                btnList[indice_i][indice_j].config(image=pixelVirtual)

    btnInicio.config(state='disabled')
    contBlancas.config(text=contW)
    contNegras.config(text=contB)

def pieces():
        pieces = ["fb", "fn", "rb", "rn"]
        for piece in pieces:
            imagenes[piece] = tk.PhotoImage(file="./Imagenes/" + piece + ".png")

def salir():
    sys.exit()
    
def createTable():
    row=0
    col=0
    cuadro=0
    for i in range(8):
        btnList.append([])
        if(col>7):
            col=0
        if(row>7):
            row=0
        for j in range(8):
            if(i+j)%2==0:
                btn=tk.Button(ventana,background="#767272", text="", borderwidth=0, image=pixelVirtual, command=on_clic)
                btn.grid(row=row, column=col)
                btn.config(state='disabled')
                btnList[i].append(btn)
            else:
                btn=tk.Button(ventana, background="#2B2A2A",text="", command=on_clic, borderwidth=0, image=pixelVirtual)
                btn.grid(row=row, column=col)
                btn.config(state='disabled')
                btnList[i].append(btn)
                
                
            col+=1
            cuadro+=1
        row+=1

fontStyle = Font(family="Lucida Grande", size=20)

fontStyle1 = Font(family="Lucida Grande", size=16)

btnInicio=tk.Button(ventana, background="#142463", text="Jugar", command=cargarFichas, relief="raised", font=fontStyle, anchor="center",padx=30,pady=5, foreground="white", borderwidth=0)
btnInicio.grid(row=3, column=9)
btnFin=tk.Button(ventana, background="#A41C0B", text="Terminar",command=salir, relief="raised", font=fontStyle, anchor="center",padx=20,pady=5, foreground="white", borderwidth=0)
btnFin.grid(row=4, column=9)

btnEspacio=tk.Button(ventana, background="#FFFFFF", anchor="center",padx=20,pady=5, foreground="white", borderwidth=0, state='disabled')
btnEspacio.grid(row=4, column=8)

negras=tk.Label(ventana, background="#FFFFFF",anchor="center", text="Fichas moradas:", font=fontStyle1)
negras.grid(row=0, column=9)
contNegras=tk.Label(ventana, background="#FFFFFF",anchor="center", text="", font=fontStyle)
contNegras.grid(row=1, column=9)
blancas=tk.Label(ventana, background="#FFFFFF",anchor="center", text="Fichas rojas:", font=fontStyle1)
blancas.grid(row=6, column=9)
contBlancas=tk.Label(ventana, background="#FFFFFF",anchor="center", text="", font=fontStyle)
contBlancas.grid(row=7, column=9)
##### BUCLE PRINCIPAL PROGRAMA #####
pieces()
createTable()
ventana.mainloop()