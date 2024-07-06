'''

2469. Converter a Temperatura

Você recebe um número de ponto flutuante não negativo, arredondado para duas casas decimais, celsius, que denota a temperatura em Celsius.
Você deve converter Celsius para Kelvin e Fahrenheit e retornar como um array ans = [kelvin, fahrenheit].

Retorne o array ans. Respostas dentro de 10^-5 da resposta real serão aceitas.

Note que:

Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00

'''
class Solution:
    def convertTemperature(self, celsius: float) -> [float, float]:
        # Convert Celsius to Kelvin
        # Converte Celsius para Kelvin
        kelvin = celsius + 273.15
        
        # Convert Celsius to Fahrenheit
        # Converte Celsius para Fahrenheit
        fahrenheit = celsius * 1.80 + 32.00
        
        # Return the result as an array
        # Retorna o resultado como um array
        return [kelvin, fahrenheit]