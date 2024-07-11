'''

981. Armazenamento de Chave-Valor Baseado em Tempo
Desenvolva uma estrutura de dados de chave-valor baseada em tempo que possa armazenar múltiplos valores para a mesma chave em diferentes timestamps e recuperar o valor da chave em um determinado timestamp.

Implemente a classe TimeMap:

TimeMap() Inicializa o objeto da estrutura de dados.
void set(String key, String value, int timestamp) Armazena a chave key com o valor value no timestamp fornecido.
String get(String key, int timestamp) Retorna um valor tal que set foi chamado anteriormente, com timestamp_prev <= timestamp. Se houver múltiplos desses valores, ele retorna o valor associado com o maior timestamp_prev. Se não houver valores, retorna "".

'''

class TimeMap:

    def __init__(self):
        # Initialize the data structure
        # Inicializa a estrutura de dados
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Store the key with the value and timestamp
        # Armazena a chave com o valor e o timestamp
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Retrieve the value with the largest timestamp_prev <= timestamp
        # Recupera o valor com o maior timestamp_prev <= timestamp
        if key not in self.store:
            return ""
        
        values = self.store[key]
        left, right = 0, len(values) - 1
        result = ""
        
        # Binary search for the largest timestamp_prev <= timestamp
        # Busca binária para o maior timestamp_prev <= timestamp
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result