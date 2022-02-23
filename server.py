import socket
import threading
from cryptography.fernet import Fernet

ip_server = "127.0.1.1"
port = 10022
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip_server , port))

conexoes = []

def encriptar (conn,address,mensagem_separados):

    global conexoes
    
    for conexao in conexoes:
        if conexao["conn"] == conn:
            f = Fernet(conexao["key"])
    print(f"Enviando encriptada para o endereço {address} ")        
    token = f.encrypt(mensagem_separados.encode())
    print(token)
    conn.sendall(token)


def desencriptar (conn,address,token):

    global conexoes
    
    for conexao in conexoes:
        if conexao["conn"] == conn:
            f = Fernet(conexao["key"])
    
    print(f"Enviando desencriptar para o endereço {address} ")        
    mensagem = f.decrypt(token.encode())
    print(mensagem )
    conn.sendall(mensagem)

def cliente(conn, address):

    print(f"NOVO CLIENTE CONECTADO PELO ENDEREÇO  {address}")
    while True:
        mensagem = conn.recv(1024).decode()
        if (mensagem.startswith("encriptar=")):
            mensagem_separados = mensagem.split("=")
            encriptar (conn,address,mensagem_separados[1])
            
        elif (mensagem.startswith("desencriptar=")):
            mensagem_separados = mensagem.split("====")
            desencriptar (conn,address,mensagem_separados[1])
        
        
        

def start():
    global conexoes
    print(f"iniciando socket no Endereço {ip_server}")
    servidor.listen()
    while True :
        conn , address = servidor.accept()
        
        key = Fernet.generate_key()
        esqueleto_conexao =({"conn" : conn ,
                            "address" :address ,
                            "key":key})
        conexoes.append(esqueleto_conexao)
        
        thread = threading.Thread(target=cliente , args =(conn,address) )
        thread.start()
        
        
start()