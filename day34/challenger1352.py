'''

1352. Produto dos Últimos K Números
Desenhe um algoritmo que aceita um fluxo de inteiros e recupera o produto dos últimos k inteiros do fluxo.

Implemente a classe ProductOfNumbers:

ProductOfNumbers() Inicializa o objeto com um fluxo vazio.
void add(int num) Adiciona o inteiro num ao fluxo.
int getProduct(int k) Retorna o produto dos últimos k números na lista atual. Você pode assumir que a lista atual sempre terá pelo menos k números.
Os casos de teste são gerados para que, a qualquer momento, o produto de qualquer sequência contígua de números caiba em um único inteiro de 32 bits sem transbordamento.

'''
class ProductOfNumbers:

    def __init__(self):
        # Initialize the list to store the stream of numbers
        # Inicializa a lista para armazenar o fluxo de números
        self.nums = []
        # Initialize a list to store the prefix products
        # Inicializa uma lista para armazenar os produtos prefixados
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        # If the number is zero, reset the prefix products list
        # Se o número for zero, reinicia a lista de produtos prefixados
        if num == 0:
            self.nums = []
            self.prefix_products = [1]
        else:
            # Add the number to the stream
            # Adiciona o número ao fluxo
            self.nums.append(num)
            # Add the new product to the prefix products list
            # Adiciona o novo produto à lista de produtos prefixados
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is larger than the number of elements, return 0 because of a previous zero
        # Se k for maior que o número de elementos, retorna 0 por causa de um zero anterior
        if k > len(self.nums):
            return 0
        # Compute the product of the last k numbers using prefix products
        # Calcula o produto dos últimos k números usando os produtos prefixados
        return self.prefix_products[-1] // self.prefix_products[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)