"""
1392. Prefixo feliz mais longo
Uma string é chamada de prefixo feliz se for um prefixo não vazio que também é um sufixo (excluindo a si mesmo).

Dada uma string s, retorne o prefixo feliz mais longo de s . Retorne uma string vazia ""se tal prefixo não existir.

 

Exemplo 1:

Entrada: s = "nível"
 Saída: "l"
 Explicação: s contém 4 prefixos excluindo a si mesmo ("l", "le", "lev", "leve") e sufixo ("l", "el", " nível", "nível"). O maior prefixo que também é sufixo é dado por “l”.
Exemplo 2:

Entrada: s = "ababab"
 Saída: "abab"
 Explicação: "abab" é o maior prefixo que também é sufixo. Eles podem se sobrepor na string original.
 

Restrições:

1 <= s.length <= 105
scontém apenas letras minúsculas em inglês.
"""


class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(len(s)-1):
            if s[:-1-i] == s[1+i:]:
                return s[1+i:]
        return ''