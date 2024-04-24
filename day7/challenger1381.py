'''
1381. Projete uma pilha com operação de incremento
Projete uma pilha que suporte operações de incremento em seus elementos.

Implemente a CustomStackclasse:

CustomStack(int maxSize)Inicializa o objeto com maxSizeo número máximo de elementos na pilha.
void push(int x)Adicionado xao topo da pilha se a pilha não tiver atingido o maxSize.
int pop()Abre e retorna o topo da pilha ou -1se a pilha estiver vazia.
void inc(int k, int val)Aumenta os kelementos inferiores da pilha em val. Se houver menos de kelementos na pilha, incremente todos os elementos na pilha.
 

Exemplo 1:

Entrada
["CustomStack","push","push","pop","push","push","push","incremento","incremento","pop","pop","pop"," pop"]
[[3],[1],[2],[],[2],[3],[4],[5.100],[2.100],[],[],[],[]]
Saída
[nulo,nulo,nulo,2,nulo,nulo,nulo,nulo,nulo,103.202.201,-1]
Explicação
CustomStack stk = novo CustomStack(3); // A pilha está vazia []
stk.push(1); // pilha se torna [1]
stk.push(2); // a pilha se torna [1, 2]
stk.pop(); // retorna 2 --> Retorna o topo da pilha 2, a pilha se torna [1]
stk.push(2); // a pilha se torna [1, 2]
stk.push(3); // a pilha se torna [1, 2, 3]
stk.push(4); // empilha ainda [1, 2, 3], Não adicione outros elementos, pois o tamanho é 4
stk.incremento(5, 100); // a pilha se torna [101, 102, 103]
stk.incremento(2, 100); // a pilha se torna [201, 202, 103]
stk.pop(); // retorna 103 --> Retorna o topo da pilha 103, a pilha se torna [201, 202]
stk.pop(); // retorna 202 --> Retorna o topo da pilha 202, a pilha se torna [201]
stk.pop(); // retorna 201 --> Retorna o topo da pilha 201, a pilha se torna []
stk.pop(); // return -1 --> A pilha está vazia return -1.

'''

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[-1]*maxSize
        
    def push(self, x: int) -> None:
        if self.stack[-1]==-1:
            k=0
            i=0
            while k!=1:
                if self.stack[i]==-1:
                    self.stack[i]=x
                    k=1
                else:
                    i+=1               

    def pop(self) -> int:
        if self.stack[0]==-1:
            return -1
        else:
            k=0
            i=0
            while k!=1:
                if (i+1)<=len(self.stack)-1 and self.stack[i+1]==-1:
                    pop=self.stack[i]
                    self.stack[i]=-1
                    k=1
                    if pop==-1:
                        return -1
                    else:    
                      return pop
                elif (i+1)==len(self.stack) and self.stack[i]!=-1:
                    pop=self.stack[i]
                    self.stack[i]=-1
                    return pop
                else:
                    i+=1   
                if i>len(self.stack):
                    k=1 
                    return -1      

    def increment(self, k: int, val: int) -> None:
        if k>len(self.stack):
            i=0
            while k!=0:
                if self.stack[i]!=-1:
                 self.stack[i]+=val
                i+=1
                k-=1
                if i>len(self.stack)-1:
                    k=0

        else:
            for j in range(0,len(self.stack)):
                if self.stack[j]!=-1:
                  self.stack[j]+=val       
                k-=1
                if k==0:
                    break           
                        