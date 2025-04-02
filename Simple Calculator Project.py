from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("570x680+100+200")
root.resizable(False,False)
root.config(bg="#17161b")

image_icon = PhotoImage(file="C:\\Users\\emily\\OneDrive\\Pictures\\Wapp_stuff\\calculator.png")
root.iconphoto(False,image_icon)


equation = ""

def show(value):
    global equation
    equation+=value
    top_design.config(text=equation)

def clear():
    global equation
    equation=""
    top_design.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result = "error"
            equation = ""
    top_design.config(text=result)


top_design = Label(root, width=25, height=2, text="", font=("arial",30))
top_design.pack()

Button(root, text="C", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=125)
Button(root, text="/", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("/")).place(x=150, y=125)
Button(root, text="%", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("%")).place(x=290, y=125)
Button(root, text="*", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("*")).place(x=430, y=125)

Button(root, text="7", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("7")).place(x=10, y=235)
Button(root, text="8", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("8")).place(x=150, y=235)
Button(root, text="9", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("9")).place(x=290, y=235)
Button(root, text="-", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("-")).place(x=430, y=235)

Button(root, text="4", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("4")).place(x=10, y=345)
Button(root, text="5", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("5")).place(x=150, y=345)
Button(root, text="6", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("6")).place(x=290, y=345)
Button(root, text="+", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("+")).place(x=430, y=345)

Button(root, text="1", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("1")).place(x=10, y=455)
Button(root, text="2", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda:show("2")).place(x=150, y=455)
Button(root, text="3", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=455)


Button(root, text="0", width=9, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=565)
Button(root, text=".", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=565)



Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=430, y=455)


root.mainloop()


