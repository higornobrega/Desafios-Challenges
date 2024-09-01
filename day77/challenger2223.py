'''

2223. Soma das Pontuações das Strings Construídas

Você está construindo uma string s de comprimento n, um caractere de cada vez, colocando cada novo caractere na frente da string. As strings são rotuladas de 1 a n, onde a string de comprimento i é rotulada como si.

Por exemplo, para s = "abaca", s1 == "a", s2 == "ca", s3 == "aca", etc.
A pontuação de si é o comprimento do maior prefixo comum entre si e sn (note que s == sn).

Dada a string final s, retorne a soma das pontuações de cada si.

'''


class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)

        # We will store the length of the longest common prefix of s and each si in the z array
        # Vamos armazenar o comprimento do prefixo comum mais longo de s e cada si no array z
        z = [0] * n

        # Initialize left and right pointers for the Z-algorithm
        # Inicialize os ponteiros esquerdo e direito para o algoritmo Z
        l, r = 0, 0

        # Iterate over the string to calculate the Z array
        # Itere sobre a string para calcular o array Z
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])

            # Attempt to extend the Z-box by comparing characters
            # Tente estender a Z-box comparando caracteres
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1

            # Update the Z-box boundaries if we've extended beyond the current right boundary
            # Atualize os limites da Z-box se tivermos estendido além do limite direito atual
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        # The sum of all values in the Z array plus the length of the string (for s1)
        # A soma de todos os valores no array Z mais o comprimento da string (para s1)
        return sum(z) + n
