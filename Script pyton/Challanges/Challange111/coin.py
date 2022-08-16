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

def resume (price=0, taxi=10, taxd=5):
    print('*' * 30)
    print('Value Resume'.center(30))
    print('*' * 30)
    print(f'Value: \t{coin(price)}')
    print(f'Double: \t{double(price, True)}')
    print(f'Half: \t{half(price, True)}')
    print(f'{taxi}% of Increasing: \t{increase(price, True)}')
    print(f'{taxd}% of Decrease: \t{decrease(price, True)}')
    print('*' * 30)
    