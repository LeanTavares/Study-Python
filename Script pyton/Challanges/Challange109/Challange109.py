import coin
p = float(input('Enter a price: R$'))
print(f'The half is {coin.coin(coin.half(p,True))}')
print(f'The double is {coin.coin(coin.double(p))}')
print(f'Increasing the 10% {coin.coin(coin.increase(p, 10))}')
