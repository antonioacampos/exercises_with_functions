def primeira_letra(string, letra):
    achou = False #define a variável que indica se a letra já foi encontrada pela 1ª vez
    i = 0
    while i < len(string) and achou == False:
        if letra == string[i]:
            new_string = string[:i] + string[i+1:] #cria a string a ser impressa sem a primeira ocorrencia da letra
            achou = True #define que a letra definida já foi achada pela primeira vez e por isso o loop pode parar
        i += 1
    print(new_string)

def todas_letras(string, letra):
    i = 0
    new_string = string
    while i < len(new_string):
        if letra == new_string[i]: #verifica se o elemento i na string é igual à letra
            new_string = new_string[:i] + new_string[i+1:] #remove o elemento i da string nova
        i += 1
    print(new_string)

def string_igual(string1, string2):
    iguais = False
    letra = 0
    if len(string1) == len(string2): #verifica se as duas strings são do mesmo tamanho
        while letra < len(string1): #verifica as strings letra por letra para saber se são iguais
            if string1[letra] == string2[letra]:
                iguais = True
            else:
                iguais = False
            letra += 1
    if iguais == True: #imprime de acordo com a igualdade das strings e o comprimento delas
        print("As duas strings são iguais!")
        print("Ambas strings possuem", len(string1), "caracteres")
    else:
        print("As duas strings não são iguais.")
        print("A string 1 possui", len(string1), "carateres e a string 2 possui", len(string2), "caracteres")

def palindromo(string):
    i = 1
    new_string = '' #cria uma nova string vazia
    palindromo = False
    while i <= len(string): 
        inverso = string[-i] #adquire letra por letra da string original no sentido inverso
        new_string = new_string + inverso #adiciona essa letra à string vazia, escrevendo a string original ao contrário
        i += 1
    if new_string == string: #verifica se a string escrita ao contrário é igual à string original
        palindromo = True
    else:
        palindromo = False
    print(palindromo)

def contar_palavras(string):
    palavras = string.count(' ') + 1 #conta os espaços entre as palavras, que é sempre um a menos que a quantidade de palavras
    print('Sua frase tem', palavras, 'palavras')
  
def nome(nome):
    i = 0
    while i <= len(nome):
        print(nome[:i]) #escreve apenas os elementos antes ou na posição i
        i += 1

def nome_modificado(nome):
    nome_mod = ''
    i = 1
    while i <= len(nome):
        inverso = nome[-i] #adquire letra por letra do nome no sentido inverso
        nome_mod = nome_mod + inverso #adiciona essa letra à string vazia, escrevendo o nome ao contrário
        i += 1
    print(nome_mod.upper()) #escreve o nome ao contrário em caixa alta

def contar_espaco_vogal(string):
    espacos = string.count(' ') #conta os espaços
    a = string.count('a')
    e = string.count('e')
    i = string.count('i')
    o = string.count('o')
    u = string.count('u')
    A = string.count('A')
    E = string.count('E')
    I  = string.count('I')
    O = string.count('O')
    U = string.count('U')
    vogais = a+e+i+o+u+A+E+I+O+U #soma todas as vogais que foram contadas, maiusculas ou minusculas
    print(f"Sua string tem {vogais} vogais e {espacos} espaços")

def normal_upper_lower(string1, string2):
    i = 0
    i2 = 0
    igual = True
    while i < len(string2) and igual == True: #percorre a segunda string apenas se os elementos estejam sendo correspondentes na outra
        while i2 < string2.count(string2[i]): #verifica quantas vezes o elemento i se repete e garante a correspondencia na mesma quantidade
            if string1[i] not in string2: #verifica se o elemento i está presente na string com formatação normal
                igual = False
                if string1[i] not in string2.upper(): #verifica se o elemento i está presente na string toda em maiúsculas
                    igual = False
                    if string1[i] not in string2.lower(): #verifica se o elemento i está presente na string toda em minúsculas
                        igual = False                        
            else:
                igual = True
            i2 += 1
        i+=1
def anagrama(word1, word2):
    string1 = word1.replace(' ', '') #retira os espaços das strings criando novas strings
    string2 = word2.replace(' ', '')
    igual = True
    if len(string1) != len(string2): #verifica se o comprimento das strings são iguais após remover espaços
        igual = False
    else:
        normal_upper_lower(string1, string2) #chama a função para fazer a verificação dos elementos nas strings
    if igual == True:
        print("True")
    else:
        print("False")

def algarismos(num):
    carac = str(num) #transforma o número em uma string
    print(f"Seu número possui {len(carac)} caracteres") #imprime o tamanho da string

def main():
    repeat = 0
    while repeat == 0:
        print("Menu de exercícios - strings")
        print("1. Remover a primeira letra igual")
        print("2. Remover todas letras iguais")
        print("3. Verificar strings iguais")
        print("4. Verificar palíndromo")
        print("5. Contar palavras")
        print("6. Nome em escada")
        print("7. Nome invertido e caixa alta")
        print("8. Contar vogais e espaços")
        print("9. Verificar anagrama")
        print("10. Contar algarismos")
        print()
        option = int(input("Digite o exercício desejado: ")) #chama a função com respectivo numero
        if option == 1 or option == 2: #entrada em comum para as funções 1 e 2
            string = input("Digite a sua string: ")
            letra = input("Digite a letra que você quer remover: ")
            print()
            if option == 1:
                primeira_letra(string, letra)
            else:
                todas_letras(string, letra)
        elif option == 3 or option == 9: #entrada em comum para as funções 3 e 9
            string1 = input("Digite uma string: ")
            string2 = input("Digite outra string: ")
            print()
            if option == 3:
                string_igual(string1, string2)
            elif option == 9:
                anagrama(string1, string2)
        elif option == 4 or option == 5 or option == 6 or option == 7 or option == 8: #entrada em comum para as funções 4, 5, 6, 7 e 8
            string = input("Digite a sua string: ")
            print()
            if option == 4:
                palindromo(string)
            elif option == 5:
                contar_palavras(string)
            elif option == 6:
                nome(string)
            elif option == 7:
                nome_modificado(string)
            elif option == 8:
                contar_espaco_vogal(string)
        elif option == 10:
            input1 = int(input("Digite um número: "))
            print()
            algarismos(input1)
        else:
            print("Exercício indisponível no momento")
        print()
        print("----------------------------------------------------------")
        print()
#---------------------------------------------------------------------------------------------------#
main()#chama a função principal
                      
