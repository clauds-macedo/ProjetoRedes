from tkinter import *
from tkinter import messagebox
import os
import client
from time import sleep

caminho = os.getcwd()

def openAndExecuteCrypto():
    client.inicio(1)
    criptografar()

def openAndExecuteDecrypto():
    client.inicio(2)
    descriptografar()

def enviarMensagemParaCriptografar(msg):
    client.enviar_mensagem_encriptada(msg)

def enviarMensagemParaDescriptografar(msg):
    client.enviar_mensagem_desencriptar(msg)

def criptografar():
    
    def getCriptoInput():
        
        encrypted = encryptInput.get(1.0, "end-1c")
        messagebox.showinfo(title=None, message=f'A mensagem "{encrypted}" foi criptografada com sucesso.\nA chave para descriptografá-la foi copiada para a área de transferência.')
        enviarMensagemParaCriptografar(encrypted)
    
    newWindow = Toplevel()
    newWindow.geometry("596x361")
    newWindow.configure(bg = "#ffffff")
    canvas = Canvas(
        newWindow,
        bg = "#ffffff",
        height = 361,
        width = 596,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    buttonImg = PhotoImage(file = f"{caminho}\\telas\\assets\\criptografia\\arrow-left.png")
    arrowb = Button(
        newWindow,
        image = buttonImg,
        borderwidth = 0,
        background="#fff",  
        highlightthickness = 0,
        command= lambda:newWindow.destroy(),
        relief = "flat").place(
            width=25, height=25,
            x = 10, y = 10
    )

    img0 = PhotoImage(file = f"{caminho}\\telas\\assets\\criptografia\\img0.png")
    b0 = Button(
        newWindow,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command=getCriptoInput,
        relief = "flat")

    b0.place(
        x = 389, y = 203,
        width = 33,
        height = 29)

    background_img = PhotoImage(file = f"{caminho}\\telas\\assets\\criptografia\\background.png")
    background = canvas.create_image(
        297.5, 114.5,
        image=background_img)

    entry0_img = PhotoImage(file = f"{caminho}\\telas\\assets\\criptografia\\img_textBox0.png")
    entry0_bg = canvas.create_image(
        272.5, 217.5,
        image = entry0_img)

    encryptInput = Text(
        newWindow,
        bd = 0,
        bg = "#C4C4C4",
        highlightthickness = 0,)

    encryptInput.place(
        x = 194.0, y = 208,
        width = 157.0,
        height = 25)
    
    newWindow.resizable(False, False)
    newWindow.mainloop()

def descriptografar():

    def getDecryptoInput():
            decrypted = decrypt.get(1.0, "end-1c")
            enviarMensagemParaDescriptografar(decrypted)
            sleep(1.5)
            showMsg = client.receber_msg_descriptografada()
            enviarMensagemParaCriptografar(showMsg)
            messagebox.showinfo(title=None, message=f'A chave descriptografada é: "{showMsg}".') 

    newWindow = Toplevel()
    newWindow.geometry("596x361")
    newWindow.configure(bg = "#ffffff")
    canvas = Canvas(
        newWindow,
        bg = "#ffffff",
        height = 361,
        width = 596,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")

    canvas.place(x = 0, y = 0)

    buttonImg = PhotoImage(file = f"{caminho}\\telas\\assets\\criptografia\\arrow-left.png")
    arrowb = Button(
        newWindow,
        image = buttonImg,
        borderwidth = 0,
        background="#fff",  
        highlightthickness = 0,
        command= lambda:newWindow.destroy(),
        relief = "flat").place(
            width=25, height=25,
            x = 10, y = 10
    )

    img0 = PhotoImage(file = f"{caminho}\\telas\\assets\\descriptografar\\img0.png")
    b0 = Button(
        newWindow,
        image = img0,
        borderwidth = 0,
        command=getDecryptoInput,
        highlightthickness = 0,
        relief = "flat")

    b0.place(
        x = 389, y = 203,
        width = 33,
        height = 29)

    background_img = PhotoImage(file = f"{caminho}\\telas\\assets\\descriptografar\\background.png")
    background = canvas.create_image(
        297.5, 114.5,
        image=background_img)

    decrypt_img = PhotoImage(file = f"{caminho}\\telas\\assets\\descriptografar\\img_textBox0.png")
    decrypt_bg = canvas.create_image(
        272.5, 217.5,
        image = decrypt_img)

    decrypt = Text(
        newWindow,
        bd = 0,
        bg = "#C4C4C4",
        highlightthickness = 0,)

    decrypt.place(
        x = 194.0, y = 208,
        width = 157.0,
        height = 25)

    newWindow.resizable(False, False)
    newWindow.mainloop()


def exit_program():
    window.destroy()
    client.fechar_servidor()


window = Tk()
window.title("Tela de Opções")
window.geometry("596x361")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 361,
    width = 596,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"{caminho}\\telas\\assets\\tela_principal\\background.png")
background = canvas.create_image(
    277.0, 180.5,
    image=background_img)

img0 = PhotoImage(file = f"{caminho}\\telas\\assets\\tela_principal\\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = openAndExecuteCrypto,
    relief = "flat")

b0.place(
    x = 357, y = 185,
    width = 197,
    height = 29)

img1 = PhotoImage(file = f"{caminho}\\telas\\assets\\tela_principal\\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = openAndExecuteDecrypto,
    relief = "flat")

b1.place(
    x = 357, y = 228,
    width = 197,
    height = 29)

img2 = PhotoImage(file = f"{caminho}\\telas\\assets\\tela_principal\\img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = exit_program,
    relief = "flat")

b2.place(
    x = 357, y = 271,
    width = 197,
    height = 29)

window.resizable(False, False)
window.mainloop()
