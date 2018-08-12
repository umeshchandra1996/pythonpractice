import random
class Pound:
    def __init__(self,rare):
        self.rare=rare
        if self.rare:
            self.value=1.25
        self.value=1.00
        self.color="Gold"
        self.num_edges=1
        self.diameter=22.5#mm
        self.thickness=3.15#mm
        self.heads=True
        
    def __del__(self):
        print("Coin Spent!")
    
    def rust(self):
        self.color="Red"
        
    def clean(self):
        self.color="Gold"
    
    def flip(self):
        heads_option=[True,False]
        choice=random.choice(heads_option)
        self.heads=choice
        
    
coin1 = Pound(rare=False)
print(coin1.value )
print(coin1.color)
print(coin1.diameter)
print(coin1.thickness)
print(coin1.heads)

coin1.flip()
print(coin1.heads)

coin2=Pound(True)
print(coin2.value)
print(coin2.color)
print(coin2.rust())
print(coin2.diameter)
print(coin2.thickness)
print(coin2.heads)

coin2.flip()
print(coin2.heads)

coin2.clean()
print(coin2.color)
    
