import socket
import threading
import  pyperclip

ip_server = "127.0.1.1"
port  = 10022

cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ip_server , port))


def administrar_mensagemns():
    while (True):
        global msg
        msg = cliente.recv(1024).decode()
        pyperclip.copy(msg)
        #print(msg)

def receber_msg_descriptografada():
    print(msg)
    if msg[-1] != "=": return msg

def enviar(mensagem):
    cliente.send(mensagem.encode())

def enviar_mensagem_desencriptar(mensagem):
    msg = mensagem
    enviar("desencriptar====" + msg)

def enviar_mensagem_encriptada(mensagem):
    msg = mensagem
    enviar("encriptar=" + msg)

def fechar_servidor():
    cliente.close()

def inicio(choose):
    thread1 = threading.Thread(target= administrar_mensagemns)
    if choose == 1:
        thread2 = threading.Thread(target= enviar_mensagem_encriptada)
    elif choose == 2: thread2 = threading.Thread(target= enviar_mensagem_desencriptar)
    thread1.start()
    thread2.start()