import platform
import subprocess

def obter_so():
    return platform.system()

def main():
    so: str = ''
    com: str = ''
    comvet: str = []*5
    saida: str = ''
    proc: str = ''
    procvet: str = []

    so = obter_so()
    if (so == 'Windows'):
        com = 'ping -4 -n 10 www.google.com.br'
        comvet = com.split(' ')
    elif (so == 'Linux'):
        com = 'ping -4 -c 10 www.google.com.br'
        comvet = com.split(' ')
    try:
        if (so == 'Windows'):
            proc = subprocess.run(comvet, capture_output=True, text=True)
            saida = proc.stdout
            procvet = saida.split(' ')
            procvet = procvet[-1].strip()
            procvet = procvet.split('m')
            print (f"Média = {procvet[0]} ms")
        elif (so == 'Linux'):
            proc = subprocess.run(comvet, capture_output=True, text=True)
            saida = proc.stdout
            procvet = saida.split('/')
            print (f"Média = {procvet[-3]} ms")
    except Exception:
        print ("Algo deu errado! :P")
    

if __name__ == '__main__':
    main()