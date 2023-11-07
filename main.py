from tkinter import Label, Tk, Button

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry(None)

# Configuración pantalla de salida 
pantalla = Label(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=0)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)
boton_1.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_1["text"]))
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)
boton_2.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_2["text"]))
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)
boton_3.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_3["text"]))
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)
boton_4.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_4["text"]))
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)
boton_5.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_5["text"]))
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)
boton_6.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_6["text"]))
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)
boton_7.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_7["text"]))
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)
boton_8.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_8["text"]))
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)
boton_9.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_9["text"]))

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
def evento_igual(e):
    array = []
    operaciones = ["+","-","*","/",]
    operacion = ""
    for op in operaciones:
        array = pantalla["text"].split(op) if op in pantalla["text"] else []
        if(len(array) > 0):
            operacion = op
            break
    if operacion == "+":
        resultado = float(array[0]) + float(array[1])
    elif operacion == "-":
        resultado = float(array[0]) - float(array[1])
    elif operacion == "*":
        resultado = float(array[0]) * float(array[1])
    elif operacion == "/":
        resultado = float(array[0]) / float(array[1])
    pantalla.config(text = resultado.__str__())
    operacion = ""
boton_igual.bind("<Button-1>", evento_igual)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)
boton_punto.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_punto["text"]))

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)
boton_mas.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_mas["text"]))

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)
boton_menos.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_menos["text"]))

boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)
boton_multiplicacion.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_multiplicacion["text"]))

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)
boton_division.bind("<Button-1>", lambda e: pantalla.configure(text = pantalla["text"] + boton_division["text"]))

root.mainloop()