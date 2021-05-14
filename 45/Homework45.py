def Months1():
    Months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    Days = [31,28,31,30,31,30,31,31,30,31,30,31]
    for m, d in zip(Months, Days):
        print(m, d)

Months1()

def Months2():
    Months2 = ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
    Days2 = (31,28,31,30,31,30,31,31,30,31,30,31)
    for m, d in zip(Months2, Days2):
        print(m, d)

Months2()


def Months3():
    months3={'Jan': 31,
        'Feb': 28,
        'Mar': 31,
        'Apr': 30,
        'May': 31,
        'Jun': 30  
                        }
    for k in months3:
        print(k,months3[k]) 
    
Months3() 
