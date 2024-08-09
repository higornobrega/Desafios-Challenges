'''
2327. Número de Pessoas que Sabem de um Segredo

Você recebe um inteiro delay, que significa que cada pessoa compartilhará o segredo com uma nova pessoa a cada dia, começando a partir de delay dias após descobrir o segredo. Você também recebe um inteiro forget, que significa que cada pessoa esquecerá o segredo forget dias após descobri-lo. Uma pessoa não pode compartilhar o segredo no mesmo dia em que o esqueceu, nem em qualquer dia posterior.

Dado um inteiro n, retorne o número de pessoas que sabem o segredo no final do dia n. Como a resposta pode ser muito grande, retorne-a módulo 10^9 + 7.

'''

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # Constants
        MOD = 10**9 + 7  # The result needs to be returned modulo 10^9 + 7
        # Constante: O resultado precisa ser retornado módulo 10^9 + 7
        
        dp = [0] * (n + 1)  # Array to store the number of people who learn the secret each day
        # Array dp para armazenar o número de pessoas que aprendem o segredo a cada dia
        
        dp[1] = 1  # On the first day, only one person knows the secret
        # No primeiro dia, apenas uma pessoa sabe o segredo
        
        people_sharing = 0  # Variable to track how many people are sharing the secret
        # Variável para rastrear quantas pessoas estão compartilhando o segredo
        
        for i in range(2, n + 1):
            # People who can start sharing today are the ones who learned the secret 'delay' days ago
            # Pessoas que podem começar a compartilhar hoje são aquelas que aprenderam o segredo há 'delay' dias
            if i - delay >= 1:
                people_sharing += dp[i - delay]
                people_sharing %= MOD  # Apply modulo to avoid overflow
                # Aplica o módulo para evitar estouro de memória
            
            # People who forget the secret today are the ones who learned the secret 'forget' days ago
            # Pessoas que esquecem o segredo hoje são aquelas que aprenderam o segredo há 'forget' dias
            if i - forget >= 1:
                people_sharing -= dp[i - forget]
                people_sharing %= MOD  # Apply modulo to ensure the value is positive
                # Aplica o módulo para garantir que o valor seja positivo
            
            dp[i] = people_sharing  # Store the number of people who learned the secret today
            # Armazena o número de pessoas que aprenderam o segredo hoje
        
        # The total number of people aware of the secret at the end is the sum of the people who learned it in the last 'forget' days
        # O número total de pessoas que sabem o segredo no final é a soma das pessoas que o aprenderam nos últimos 'forget' dias
        result = sum(dp[max(1, n - forget + 1):]) % MOD
        # Soma os últimos dias e aplica o módulo
        
        return result
        # Retorna o resultado
