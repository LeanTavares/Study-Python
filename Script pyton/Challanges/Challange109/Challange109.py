import coin
p = float(input('Enter a price: R$'))
print(f'The half is {coin.half(p,True)}')
print(f'The double is {coin.double(p,True)}')
print(f'Increasing the 10% {coin.increase(p, 10, True)}')
