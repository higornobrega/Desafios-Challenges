'''

2162. Custo Mínimo para Configurar o Tempo de Cozimento

Um micro-ondas genérico suporta tempos de cozimento de:

Pelo menos 1 segundo.
No máximo 99 minutos e 99 segundos.
Para configurar o tempo de cozimento, você pressiona no máximo quatro dígitos. O micro-ondas normaliza o que você pressiona como quatro dígitos, adicionando zeros à esquerda. Ele interpreta os dois primeiros dígitos como os minutos e os dois últimos dígitos como os segundos. Em seguida, soma-os como o tempo de cozimento. Por exemplo:

Você pressiona 9 5 4 (três dígitos). Ele é normalizado como 0954 e interpretado como 9 minutos e 54 segundos.
Você pressiona 0 0 0 8 (quatro dígitos). Ele é interpretado como 0 minutos e 8 segundos.
Você pressiona 8 0 9 0. Ele é interpretado como 80 minutos e 90 segundos.
Você pressiona 8 1 3 0. Ele é interpretado como 81 minutos e 30 segundos.
Você recebe os inteiros startAt, moveCost, pushCost e targetSeconds. Inicialmente, seu dedo está sobre o dígito startAt. Mover o dedo acima de qualquer dígito específico custa moveCost unidades de fadiga. Pressionar o dígito abaixo do dedo uma vez custa pushCost unidades de fadiga.

Podem existir várias maneiras de configurar o micro-ondas para cozinhar por targetSeconds segundos, mas você está interessado na maneira com o menor custo.

Retorne o custo mínimo para configurar targetSeconds segundos de tempo de cozimento.

Lembre-se de que um minuto consiste em 60 segundos.

'''


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # Convert targetSeconds into minutes and seconds
        # Converte targetSeconds em minutos e segundos
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60

        # Initialize the minimum cost to a large value
        # Inicializa o custo mínimo com um valor grande
        min_cost = float('inf')

        # Helper function to calculate the cost for a given time setting
        # Função auxiliar para calcular o custo para uma configuração de tempo dada
        def calculate_cost(startAt, time_str):
            cost = 0
            current_pos = startAt

            for ch in time_str:
                digit = int(ch)
                # If the finger needs to move to a new digit
                # Se o dedo precisar se mover para um novo dígito
                if digit != current_pos:
                    cost += moveCost  # Add move cost
                    current_pos = digit  # Update current position
                cost += pushCost  # Add push cost
            return cost

        # Consider two possible time settings
        # Considera duas possíveis configurações de tempo
        for m, s in [(minutes, seconds), (minutes - 1, seconds + 60)]:
            # Check if the configuration is valid (i.e., minutes and seconds are within bounds)
            # Verifica se a configuração é válida (ou seja, minutos e segundos estão dentro dos limites)
            if 0 <= m < 100 and 0 <= s < 100:
                # Create a string representation of the time, omitting leading zeros
                # Cria uma representação em string do tempo, omitindo zeros à esquerda
                time_str = f"{m:02}{s:02}".lstrip('0')
                if time_str == "":
                    time_str = "0"

                # Calculate the cost for this time setting
                # Calcula o custo para esta configuração de tempo
                cost = calculate_cost(startAt, time_str)

                # Update the minimum cost
                # Atualiza o custo mínimo
                min_cost = min(min_cost, cost)

        return min_cost
