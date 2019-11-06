class Fechadura:
    def __init__(self, segredo ):
        self.__chave = segredo
        self.__status =  False
        # False = trancada // True = Trancada

    def trancar(self, segredo):
        if self.__chave == segredo:
            self.__status = True
        
    def destrancar(self, segredo):
        if self.__chave == segredo:
            self.__status = False

    def __str__(self):
        return ("...Chave: "+str(self.__chave)+
        " - Status: "+str(self.veriificaStatus()))
    
    def veriificaStatus(self):
        if self.__status:
            return "Trancada"
        return "Destrancada"

