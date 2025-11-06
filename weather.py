weather = (1, 0, 1, 1, 0, 1, 0)
rainy = 0 
sunny = 0
for i in range (7):
    if weather [i] == 1:
        sunny = sunny+1
    else:
        rainy = rainy + 1
if sunny > rainy :
    print ("You Had A Good Weather")
else:
    print("faltu mausam")