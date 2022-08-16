def increase(price=0, tax=0, formate=False):
    res = price + (price * tax/100)
    return res

def decrease(price=0, tax=0):
    res = price - (price * tax/100)
    return res

def double(price=0):
    res = price*2
    return res

def half(price=0):
    res = price/2
    return res 
def coin (price=0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')