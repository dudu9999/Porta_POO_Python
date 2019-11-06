import fechadura
    
###################################################
class Porta:
    def __init__(self, altura , largura=100,status = False):
        self.__altura   = altura
        self.__largura  = largura
        self.__cor      = None
        self.__status      = status
        self.__fechadura     = None

    def instalar(self,fechadura ):
        self.__fechadura = fechadura 

    def getAltura(self):
        return self.__altura
    
    def getLargura(self):
        return self.__largura
    
    def getCor(self):
        return self.__cor
    
    def getStatus(self):
        if self.__status:
            return 'Aberta'
        return 'Fechada'
        
    def getFechadura(self):
        return  self.__fechadura 

 
    def setCor(self,cor):
        self.__cor = cor
    def abrir(self):
        self.__status = True
        
    def fechar(self):
        self.__status = False

    def __str__(self):
        retorno =  "\n-------altura:   "+str(self.__altura)
        retorno +=  "\n-------largura: "+str(self.__largura)
        retorno +=  "\n-------cor:      "+str(self.__cor)
        retorno +=  "\n-------Status: "+str(self.getStatus())
        retorno +=  "\n-------Fechadura "+str(self.getFechadura())
        return retorno

