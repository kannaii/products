products = []

while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	# p = [] # 要同時把商品跟價格放進一個清單中, 先創一個清單p
	# p.append(name)
	# p.append(price)
	# p = [name, price] # 上面3行快寫成這一行
	products.append([name, price]) #products.append(p) 再把小清單p放進大清單products # 上面4行快寫成這一行
print(products)

for p in products:
	print(p[0], '的價格是', p[1])