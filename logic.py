from pymongo import MongoClient
from pymongo.database import Database
from pymongo.cursor import Cursor

class GST():
    cont = MongoClient()
    db = cont['routs']
    def __init__(self) -> None:
        # self.cont = MongoClient() 
        # self.db = self.cont['routs']
        pass
    
    def Ajouter(self,tb) -> None:
        self.db.rout.insert_one(tb)
    
    def __str__(self) -> str:
        res = self.db.rout.find({})
        for X in res[:]:
            print(f"""
                  Nome : {X['nom']} 
                  Distance : {X['dist']}
                  Vile D : {X['viled']} 
                  Vile A : {X['vileA']}""") 
    
    
    def rechercher(self,viled) -> str:
        res = self.db.rout.find({"viled":viled},{})
        for X in res[:]:
            return f"""
                  Nome : {X['nom']} 
                  Distance : {int(X['dist'])}
                  Vile D : {X['viled']} 
                  Vile A : {X['vileA']}"""
                  
    def suprimer(self,nom) -> str:
        self.db.rout.delete_one({"nom":nom})
        return f""" Done !!! """

    def Sauvgarder(self,nom) -> str:
        res = self.db.rout.find({"nom":nom},{})
        for X in res[:]:
            return f"""
                  Nome : {X['nom']} 
                  Distance : {int(X['dist'])}
                  Vile D : {X['viled']} 
                  Vile A : {X['vileA']}""" 

    def sof(self,nom):
        with open(f"{nom}.txt", 'w') as f:
            f.write(str(GST.Sauvgarder(self,nom)))
    
    
    def ShortRout(self):
        minr = 1
        resM = self.db.rout.aggregate([{"$group":{"_id": "$null","mind": { "$min": "$dist" }}}])
        
        for X in resM:
            minr= X['mind']
        res = self.db.rout.find({"dist":minr},{})
        for io in res[:]:
            return f"""
                  Nome : {io['nom']} 
                  Distance : {int(io['dist'])}
                  Vile D : {io['viled']} 
                  Vile A : {io['vileA']}"""

                  
        


