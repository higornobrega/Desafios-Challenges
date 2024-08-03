'''

405. Converter um Número para Hexadecimal
Dado um número inteiro num, retorne uma string representando sua representação hexadecimal. Para números inteiros negativos, o método de complemento de dois é usado.

Todas as letras na string de resposta devem ser caracteres minúsculos, e não deve haver zeros à esquerda na resposta, exceto o próprio zero.

Nota: Não é permitido usar nenhum método de biblioteca embutido para resolver diretamente este problema.
'''


class Solution:
    def toHex(self, num: int) -> str:
        # Check for the case when num is zero
        # Verifique o caso quando num é zero
        if num == 0:
            return "0"
        
        # Create a string for the hexadecimal characters
        # Crie uma string para os caracteres hexadecimais
        hex_chars = "0123456789abcdef"
        
        # Prepare a list to collect hexadecimal digits
        # Prepare uma lista para coletar os dígitos hexadecimais
        hex_result = []
        
        # If the number is negative, convert it to its two's complement representation
        # Se o número for negativo, converta-o para sua representação em complemento de dois
        if num < 0:
            num += 2 ** 32
        
        # Convert the number to hexadecimal
        # Converta o número para hexadecimal
        while num > 0:
            # Get the last 4 bits of the number (equivalent to one hexadecimal digit)
            # Obtenha os últimos 4 bits do número (equivalente a um dígito hexadecimal)
            hex_digit = num & 15
            # Append the corresponding hexadecimal character to the result list
            # Adicione o caractere hexadecimal correspondente à lista de resultados
            hex_result.append(hex_chars[hex_digit])
            # Right shift the number by 4 bits to process the next digit
            # Desloque o número 4 bits para a direita para processar o próximo dígito
            num >>= 4
        
        # Reverse the list of hexadecimal digits and join them into a string
        # Inverta a lista de dígitos hexadecimais e junte-os em uma string
        return ''.join(reversed(hex_result))