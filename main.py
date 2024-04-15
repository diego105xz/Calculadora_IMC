def main():
    print('Calculadora de IMC')
    altura = verifica_altura()
    peso = verifica_peso()
    calcular_IMC(altura, peso)

def validar_entrada(entrada):
    if entrada.strip() == '':
        return False
    entrada = entrada.replace(',', '.')
    if all(caractere.isdigit() or (caractere == '.' and entrada.count('.') == 1) for caractere in entrada):
        return True
    return False

def verifica_altura():
    while True:
        altura = input("Informe sua altura em metros: ")
        altura = altura.replace(',', '.')
        if validar_entrada(altura):
            return float(altura)
        else:
            print("Por favor, insira apenas números válidos.")

def verifica_peso():
    while True:
        peso = input("Informe seu peso em kg: ")
        peso = peso.replace(',', '.')
        if validar_entrada(peso):
            return float(peso)
        else:
            print("Por favor, insira apenas números válidos.")

def calcular_IMC(altura, peso):
    imc = peso / (altura * altura)
    if imc < 18.5:
        print('Seu índice corporal é {:.2f} e sua classificação é MAGREZA com Nível de obesidade 0.'.format(imc))    
    elif 18.5 <= imc <= 24.9:
        print('Seu índice corporal é {:.2f} e sua classificação é NORMAL com Nível de obesidade 0.'.format(imc))   
    elif 25 <= imc <= 29.9:
        print('Seu índice corporal é {:.2f} e sua classificação é SOBREPESO com Nível de obesidade 1.'.format(imc)) 
    elif 30 <= imc <= 39.9:
        print('Seu índice corporal é {:.2f} e sua classificação é OBESIDADE com Nível de obesidade 2.'.format(imc)) 
    else:
        print('Seu índice corporal é {:.2f} e sua classificação é OBESIDADE GRAVE com Nível de obesidade 3.'.format(imc))

if __name__ == "__main__":
    main()