# 672. Comutador de Lâmpadas II
# Há uma sala com nlâmpadas marcadas com 1a nque estão todas ligadas inicialmente e quatro botões na parede. Cada um dos quatro botões possui uma funcionalidade diferente onde:

# Botão 1: Inverte o status de todas as lâmpadas.
# Botão 2: Inverte o status de todas as lâmpadas com rótulos pares (ou seja, 2, 4, ...).
# Botão 3: Inverte o status de todas as lâmpadas com rótulos ímpares (ou seja, 1, 3, ...).
# Botão 4: Inverte o status de todas as lâmpadas com um rótulo j = 3k + 1onde k = 0, 1, 2, ...(ou seja, 1, 4, 7, 10, ...).
# Você deve pressionar exatamente presses os botões no total. Para cada pressionamento, você pode escolher qualquer um dos quatro botões para pressionar.

# Dados os dois inteiros ne presses, retorne o número de diferentes status possíveis após realizar todos pressesos pressionamentos de botão .

 

# Exemplo 1:

# Entrada: n = 1, pressiona = 1
#  Saída: 2
#  Explicação: O status pode ser:
# - [desligar] pressionando o botão 1
# - [ligado] pressionando o botão 2
# Exemplo 2:

# Entrada: n = 2, pressiona = 1
#  Saída: 3
#  Explicação: O status pode ser:
# - [desligar, desligar] pressionando o botão 1
# - [ligar, desligar] pressionando o botão 2
# - [desligar, ligar] pressionando o botão 3
# Exemplo 3:

# Entrada: n = 3, pressiona = 1
#  Saída: 4
#  Explicação: O status pode ser:
# - [desligar, desligar, desligar] pressionando o botão 1
# - [desligar, ligar, desligar] pressionando o botão 2
# - [ligar, desligar, ligar] pressionando o botão 3
# - [desligar, ligar, ligar] pressionando o botão 4

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0: 
            return 1
        if n == 1: 
            return 2
        elif n == 2: 
            if presses == 1:
                return 3
            else: 
                return 4
        elif presses == 1: 
            return 4
        elif presses == 2: 
            return 7
        else: 
            return 8