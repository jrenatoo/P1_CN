def ConvertePara(num, base):
    """Converte um número (inteiro ou float) para a base desejada."""
    # Parte inteira
    parte_inteira = int(num)
    digitos = []
    while parte_inteira > 0:
        resto = parte_inteira % base
        if resto > 9:
            digitos.append(chr(resto - 10 + ord('A')))
        else:
            digitos.append(str(resto))
        parte_inteira = parte_inteira // base

    # Parte decimal
    parte_decimal = num - int(num)
    digitos_decimal = []
    while parte_decimal > 0 and len(digitos_decimal) < 10:  # Limita a 10 casas decimais
        parte_decimal *= base
        digito = int(parte_decimal)
        if digito > 9:
            digitos_decimal.append(chr(digito - 10 + ord('A')))
        else:
            digitos_decimal.append(str(digito))
        parte_decimal -= digito

    # Juntando as partes
    return ''.join(digitos[::-1]) + '.' + ''.join(digitos_decimal)


def ConverteDe(num_str, base):
    """Converte uma string representando um número (com ponto flutuante) para um inteiro."""
    if '.' in num_str:
        parte_inteira_str, parte_decimal_str = num_str.split('.')
    else:
        parte_inteira_str, parte_decimal_str = num_str, ''

    # Parte inteira
    num = 0
    for digito in parte_inteira_str:
        if '0' <= digito <= '9':
            valor = int(digito)
        else:
            valor = ord(digito.upper()) - ord('A') + 10
        num = num * base + valor

    # Parte decimal
    decimal = 0
    for i, digito in enumerate(parte_decimal_str):
        if '0' <= digito <= '9':
            valor = int(digito)
        else:
            valor = ord(digito.upper()) - ord('A') + 10
        decimal += valor / (base ** (i + 1))

    return num + decimal


def soma(num1, base1, num2, base2):
    int_num1 = ConverteDe(num1, base1)
    int_num2 = ConverteDe(num2, base2)
    sum_result = int_num1 + int_num2
    maiorbase = max(base1, base2)
    print(f"Primeiro número ({num1}) na base {maiorbase}: {ConvertePara(int_num1, maiorbase)}")
    print(f"Segundo número ({num2}) na base {maiorbase}: {ConvertePara(int_num2, maiorbase)}")
    return ConvertePara(sum_result, maiorbase)


def multiplicacao(num1, base1, num2, base2):
    int_num1 = ConverteDe(num1, base1)
    int_num2 = ConverteDe(num2, base2)
    product_result = int_num1 * int_num2
    maiorbase = max(base1, base2)
    print(f"Primeiro número ({num1}) na base {maiorbase}: {ConvertePara(int_num1, maiorbase)}")
    print(f"Segundo número ({num2}) na base {maiorbase}: {ConvertePara(int_num2, maiorbase)}")
    return ConvertePara(product_result, maiorbase)


def main():
    num1 = input("Digite o primeiro número (pode ser float): ")
    base1 = int(input("Digite a base do primeiro número: "))
    num2 = input("Digite o segundo número (pode ser float): ")
    base2 = int(input("Digite a base do segundo número: "))
    operacao = input("Escolha a operação: + para soma ou * para multiplicação: ")

    if operacao == '+':
        resultado = soma(num1, base1, num2, base2)
    elif operacao == '*':
        resultado = multiplicacao(num1, base1, num2, base2)

    print(f"O resultado é: {resultado} na base {max(base1, base2)}")


if __name__ == "__main__":
    main()
