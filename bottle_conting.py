
for qaunt in range(50,0,-1):
    if qaunt>1:
        print(qaunt,"Bottel of beer on the wall"  ,qaunt,"Bottel of beer")
        if qaunt>2:
            suffix=str(qaunt) + "bottel of beer the wall"
        else:
            suffix="1 bottel of on the wall"
            
    elif qaunt == 1:
        print("1 bottel of beer on the wall, 1 bottel of beer")
        suffix="No more beer on the wall"

    print("Take one down and pass it arround", suffix)
    print("----")
