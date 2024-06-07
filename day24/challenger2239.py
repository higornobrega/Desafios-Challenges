'''
2239. Encontre o número mais próximo de zero

Dada uma matriz inteira nums de size n, retorne o número com o valor mais próximo de 0 in nums. Se houver múltiplas respostas, retorne o número com o maior valor .

'''
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Initialize the closest number to the first element
        # Inicializa o número mais próximo com o primeiro elemento
        closest = nums[0]

        for num in nums:
            # Check if the current number is closer to zero than the closest
            # Verifica se o número atual está mais próximo de zero do que o mais próximo
            if abs(num) < abs(closest):
                closest = num
            # If the current number has the same distance to zero but is larger, update closest
            # Se o número atual tem a mesma distância para zero, mas é maior, atualiza o mais próximo
            elif abs(num) == abs(closest) and num > closest:
                closest = num

        return closest