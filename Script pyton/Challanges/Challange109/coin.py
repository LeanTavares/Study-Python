def increase(price=0, tax=0, formate=False):
    res = price + (price * tax/100)
    return res if not formate else coin(res)

def decrease(price=0, tax=0, formate=False):
    res = price - (price * tax/100)
    return res if not formate else coin(res)

def double(price=0, formate=False):
    res = price*2
    return res if not formate else coin(res)

def half(price=0, formate=False):
    res = price/2
    return res if not formate else coin(res)
    
def coin (price=0, coin='R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')