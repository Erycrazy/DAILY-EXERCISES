class Node:
    valor = 0; 
    proximo = None; 
      
    def __init__(self, proxNodeParam, valorParam):
        self.proxNodeParam = proxNodeParam; 
        self.valorParam = valorParam; 
        
class stack: 
    topo = None; 
    tamanho = 0; 
    
    def __init__(self):
        self.topo = None; 
        self.tamanho = 0; 
        
    def push(self, valorParam):
        novoNo = Node(valorParam, None); 
        novoNo.proximo = self.topo; 
        self.topo = novoNo; 
        self.tamanho += 1; 
        
    def pop(self):
        if (self.isEmpty()):
            print("Pilha vazia"); 
            return None; 
        
        else:
            valorDoTopo = self.topo.valor; 
            self.topo = self.topo.proximo; 
            self.tamanho -= 1; 
            
            return valorDoTopo; 
        
    def peek(self):
        if (self.isEmpty()):
            print("Pilha vazia!"); 
            return None; 
        else:
            self.topo.valor; 
        
    def isEmpty(self):
        if (self.topo == None):
            return True; 
        else:
            return False; 
    
    
    
        