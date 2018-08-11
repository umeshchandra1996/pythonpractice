for quant in range(50,0,-1):
    if quant>1:
        print(quant,"Bottel of beer on the wall"  ,quant,"Bottel of beer")
        
        if quant>2:
            suffix=str(quant) + "bottel of beer the wall"
        else:
            suffix="1 bottel of on the wall"
            
    elif quant == 1:
        print("1 bottel of beer on the wall, 1 bottel of beer")
        suffix="No more beer on the wall"

    print("Take one down and pass it arround", suffix)
    print("----")
