"""
2180. Conte números inteiros com soma de dígitos pares
Fácil
Tópicos
Empresas
Dica
Dado um número inteiro positivo num, retorne o número de números inteiros positivos menores ou iguais num cujas somas de dígitos são pares .

A soma dos dígitos de um número inteiro positivo é a soma de todos os seus dígitos.

 

Exemplo 1:

Entrada: num = 4
 Saída: 2
 Explicação:
Os únicos números inteiros menores ou iguais a 4 cujas somas de dígitos são pares são 2 e 4.    
Exemplo 2:

Entrada: num = 30
 Saída: 14
 Explicação:
Os 14 números inteiros menores ou iguais a 30 cujas somas de dígitos são pares são
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26 e 28.
"""

class Solution:
    def countEven(self, num: int) -> int:
        # Inicializa o contador de números com soma de dígitos pares
        count = 0
        # Itera através dos números de 1 até num (inclusive)
        for i in range(1, num + 1):
            # Converte o número atual em uma string para iterar através de seus dígitos
            s = str(i)
            # Inicializa uma variável para armazenar a soma dos dígitos do número atual
            t = 0
            # Itera através de cada dígito do número atual
            for j in s:
                # Converte o dígito para o seu valor inteiro e adiciona à soma total
                t += (ord(j) - ord("0"))
            
            # Verifica se a soma dos dígitos é par
            if t % 2 == 0:
                # Se a soma dos dígitos é par, incrementa o contador
                count += 1
        # Retorna o número total de números com soma de dígitos pares
        return count