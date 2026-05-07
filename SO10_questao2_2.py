import platform
import subprocess

def obter_so():
    return platform.system()

def exec_com(com):
    codigo: str = []

    codigo = com.split(' ')
    try:
        subprocess.run(codigo)
    except Exception:
        "Algo deu errado com o comando! :P"
    
def main():
    os: str = ''
    opcao: str = ''
    proc: str = ''
    
    os = obter_so()
    while True:
        print (f"SO: {os}")
        print ("1 - Listar processos")
        print ("2 - Matar processo por PID")
        print ("3 - Matar processo por nome")
        print ("9 - Encerrar aplicação")
        opcao = input("Insira uma opção: ")
        if (opcao == '1'):
            if (os == 'Linux'):   
                exec_com('ps -ef')
            elif (os == 'Windows'):
                exec_com('TASKLIST /FO TABLE')
            print("")
        elif (opcao == '2'):
            proc = input("Insira o PID do processo: ")
            if (os == 'Linux'):
                exec_com(f'kill -9 {proc}')
            elif (os == 'Windows'):
                exec_com(f'TASKKILL /PID {proc}')
        elif (opcao == '3'):
            proc = input("Insira o nome do processo: ")
            if (os == 'Linux'):
                exec_com(f'pkill -f {proc}')
            elif (os == 'Windows'):
                exec_com(f'TASKKILL /F /IM {proc}')
        elif (opcao == '9'):
            print ("Encerrando aplicação.")
            break
        else:
            print ("Opção inválida!")

if __name__ == '__main__':
    main()