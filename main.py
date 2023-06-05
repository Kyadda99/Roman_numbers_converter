# Roman to Numbers

num="CMLXXXVIII"
def tran(x): # translation roman to number
    rom=["M","D","C","L","X","V","I"]
    num=[1000,500,100,50,10,5,1]
    return num[rom.index(x)]

def romanConverter(rom):
    score=0
    i=0
    while i<len(rom)-1:
        if tran(rom[i])>=tran(rom[i+1]):
            score=score+tran(rom[i])
            i+=1
        elif tran(rom[i])<tran(rom[i+1]):
            score=score+(tran(rom[i+1])-tran(rom[i]))
            i+=2
    score=score+tran(rom[-1])
    return score

print(romanConverter(num))










