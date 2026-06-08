class Procedimento:
    def __init__(self, descricao, custo, profissional):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional = profissional

    @property
    def descricao(self): 
        return self.__descricao
    
    @property
    def custo(self): 
        return self.__custo
    
    @property
    def profissional(self): 
        return self.__profissional