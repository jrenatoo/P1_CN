def ConvertePara(num, base):
    "Função que coinverte a base de maneira semelhante à trabalhada em sala,"
    "faz divisões(inteiras) e utiliza os valores do resto de maneira DownUp(de baixo para cima)"
    "e assim é representado o número na base nova"
    
    digitos = []
    "Cria a lista que receberá os valores"
    while num > 0:
        "Esse processo vai realizando sucessivas divisões enquanto o número for maior que 0"
        resto = num % base
        "Calcula o resto de divisão do número pela base"
        if resto > 9:
            digitos.append(chr(resto - 10 + ord('A')))
            "Caso o resto do número seja maior que 9,ou seja, em base maior que 10."
            "Isso converte-o para uma letra correspondente e logo após adiciona à lista."
        else:
            digitos.append(str(resto))
            "Adiciona o valor à lista."
        num = num // base
        "Faz a divisão do numero pela base, maneira semelhante à trabalhada em sala"
        "Quando chegar a 0 o laço de repetição while é encerrado"
    return ''.join(digitos[::-1])
    "Realiza 3 funções:O [::-1] inverte a lista.(pois por se tratar de inteiro é utilizado DownUP);"
    "                  O .join transforma a lista de digitos em um só digito,basicamente juntando-os" 
    "                  return -> Retorna o valor obtido."


def ConverteDe(num_str, base):
    """Converte uma string representando um número em uma base específica para um inteiro."""
    num = 0
    for digito in num_str:
        "Realiza uma varredura de todos os termos do número(lido como string)"
        if '0' <= digito <= '9':
            valor = int(digito)
            "Transforma stirng em inteiro e atribui a valor"
        else:
            valor = ord(digito.upper()) - ord('A') + 10
            "Caso o termo não seja um 'número', a letra é associado ao seu valor na tabela ASCII"
            "A subtração e soma servem para que a contagem ocorra apartir de 10, logo: A = 10, B = 2, etc..."
        num = num * base + valor
        "Calcula o valor acumulado do número processado."
    return num

"As operações funcionam de maneira a chamar as outras funções, realizar a soma/multiplicação e retornar o valor"

def soma(num1, base1, num2, base2):
    int_num1 = ConverteDe(num1, base1)
    int_num2 = ConverteDe(num2, base2)
    sum_result = int_num1 + int_num2
    maiorbase = max(base1, base2)
    return ConvertePara(sum_result, maiorbase)


def multiplicacao(num1, base1, num2, base2):
    int_num1 = ConverteDe(num1, base1)
    int_num2 = ConverteDe(num2, base2)
    product_result = int_num1 * int_num2
    maiorbase = max(base1, base2)
    return ConvertePara(product_result, maiorbase)


def main():
    num1 = input("Digite o primeiro número: ")
    base1 = int(input("Digite a base do primeiro número: "))
    num2 = input("Digite o segundo número: ")
    base2 = int(input("Digite a base do segundo número: "))
    operacao = input("Escolha a operação: + para soma ou * para multiplicação.")

    if operacao == '+':
        resultado = soma(num1, base1, num2, base2)
    elif operacao == '*':
        resultado = multiplicacao(num1, base1, num2, base2)

    print(f"O resultado é: {resultado} na base {max(base1, base2)}")


if __name__ == "__main__":
    main()