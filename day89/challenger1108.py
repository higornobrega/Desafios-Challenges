'''

1108.Desfazer um Endereço IP
Dado um endereço IP (IPv4) válido, retorne uma versão "desfendida" desse endereço IP.
Um endereço IP "desfendido" substitui cada ponto "." por "[.]".
'''


class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Change dot for bracket with dot
        # Mudar pónto por colchete com ponto
        return address.replace('.', '[.]')
