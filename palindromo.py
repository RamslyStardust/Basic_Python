def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

#dejar 2 espacios entre funciones
def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

#dejar 2 espacios entre el entrypoint
if __name__ =="__main__":
    run()