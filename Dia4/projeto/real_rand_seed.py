import sys
import subprocess

# Instalar as bibliotecas necessárias
try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'beautifulsoup4'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    print("Erro ao instalar as bibliotecas. Por favor, instale manualmente.")

# Importar as bibliotecas após a instalação
import requests
from bs4 import BeautifulSoup
import random

def real_rand_seed():
    '''
    Entrar em um site que mede a temperatura atual na cidade de Viena, Áustria.
    O site é https://www.timeanddate.com/weather/austria/vienna
    A temperatura é um número inteiro entre 0 e 40. 
    '''
    url = "https://www.timeanddate.com/weather/austria/vienna"
    
    # Realiza a solicitação HTTP
    response = requests.get(url)
    
    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analisa o HTML da página
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Encontra o elemento que contém a temperatura
        temp_element = soup.find("div", class_="h2").text
        
        # Extrai a temperatura como um número inteiro
        temperature = int(temp_element.split()[0])
        
        # Retorna a temperatura como a semente para o gerador de números aleatórios
        return temperature
    else:
        return None

# Testando a função
print(real_rand_seed())


#pylint: disable-all