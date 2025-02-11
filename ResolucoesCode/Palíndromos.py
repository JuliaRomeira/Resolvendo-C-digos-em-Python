def verificar_palindromo(texto):
    texto = texto.replace(" ", "").lower() 
    return texto == texto[::-1]  

entrada = input("Digite uma palavra ou frase: ")
if verificar_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
