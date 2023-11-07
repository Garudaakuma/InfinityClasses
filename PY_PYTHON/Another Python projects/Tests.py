class Car():
    def __init__(self,marc,mode,ano,peso):
        self.marc = marc
        self.mode = mode
        self.ano = ano
        self.peso = peso
        
    def ligar(self):
        return f'O {self.mode} Está ligado'
    
celta = Car('chev','Celta','2006',1200)

print(celta.mode)
print(celta.ligar())