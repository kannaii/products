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


with open('products.csv', 'w', encoding='utf-8') as f: # encoding utf-8為最廣泛使用的編碼,可以讀取中文字
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')