'''

2320.Há uma rua com n * 2 terrenos, onde há n terrenos de cada lado da rua. Os terrenos de cada lado são numerados de 1 a n. Em cada terreno, uma casa pode ser colocada.

Retorne o número de maneiras em que as casas podem ser colocadas de modo que nenhuma casa seja adjacente a outra na mesma calçada da rua. Como a resposta pode ser muito grande, retorne o resultado módulo 10^9 + 7.

Note que, se uma casa for colocada no i-ésimo terreno de um lado da rua, uma casa também pode ser colocada no i-ésimo terreno do outro lado da rua.

'''


class Solution:
    def countHousePlacements(self, n: int) -> int:
        # Modulo value to prevent overflow / Valor do módulo para evitar estouro
        MOD = 10**9 + 7

        # Base cases for the first plot / Casos base para o primeiro terreno
        prev = 1  # Number of ways to place houses for 0 plots / Número de maneiras de colocar casas para 0 terrenos
        curr = 2  # Number of ways to place houses for 1 plot / Número de maneiras de colocar casas para 1 terreno

        # Dynamic programming to find the number of ways for n plots / Programação dinâmica para encontrar o número de maneiras para n terrenos
        for i in range(2, n + 1):
            # Transition relation / Relação de transição
            next_val = (prev + curr) % MOD
            prev = curr  # Update prev for next iteration / Atualiza prev para a próxima iteração
            curr = next_val  # Update curr for next iteration / Atualiza curr para a próxima iteração

        # The answer is (curr * curr) because the arrangement on each side of the street is independent /
        # A resposta é (curr * curr) porque a disposição em cada lado da rua é independente
        return (curr * curr) % MOD
