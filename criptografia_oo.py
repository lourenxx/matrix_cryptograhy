import numpy as np



class Matrizes():
    def __init__(self):
        self.alfabeto = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        
        self.matriz_letras = np.empty((2,2), dtype=str) 
        self.matriz_numeros = np.empty((2,2), dtype=int)
        self.chave = np.array([[5,9], [1,2]], dtype=int )
        
        
    def escrever_matriz(self):
        palavra = input("digite a sua palavra (apenas 4 letras): ")
            
        while len(palavra) > 4:
            palavra = input("palavra maior que 4 letras, tente novamente:")
        return palavra
        

    def preencher_matriz(self, palavra):
        for i,letra in enumerate(palavra):
            linha = i // 2
            coluna = i % 2
            self.matriz_letras[linha, coluna] = letra

            if letra in self.alfabeto:
                indice = self.alfabeto.get(letra, 0)
                linha = i // 2
                coluna = i % 2
                self.matriz_numeros[linha, coluna] = indice


    def criptografa_matriz(self):
        self.matriz_criptografada = self.matriz_numeros * self.chave
        self.palavra_criptografada = ""

        for i in range(self.matriz_criptografada.shape[0]):
            for j in range(self.matriz_criptografada.shape[1]):
                numero = self.matriz_criptografada[i, j]

                if numero <= 26:     
                    letra = [chave for chave, valor in self.alfabeto.items() if valor == numero][0]
                    self.palavra_criptografada += letra

                else:
                    resto = numero % 26
                    letra = [chave for chave, valor in self.alfabeto.items() if valor == resto][0]
                    self.palavra_criptografada += letra
                

    def mostrar_matriz(self):
        print(f"matriz com letras: \n {self.matriz_letras}")
        print(f"\n")
        print(f"matriz com numeros: \n {self.matriz_numeros} ")
        print(f"\n")
        print(f"matriz criptografada: \n {self.matriz_criptografada} ")
        print(f"\n")
        print(f"a sua palavra criptografada é: {self.palavra_criptografada.upper()}")
        

matriz = Matrizes()




    