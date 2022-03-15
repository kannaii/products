# 檢查檔案是否存在+讀取檔案
import os # operating system

products = []
if os.path.isfile('products.csv'):
	print('yeah! 找到檔案了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 如果商品價錢在line裡面的話，我就跳到下一回
			name, price = line.strip().split(',') #去掉換行,讀到逗點就分割
			products.append([name, price])
	print(products)
else:
	print('找不到檔案....')

# 讀取檔案
# products = []
# with open('products.csv', 'r', encoding='utf-8') as f:
	# for line in f:
		# if '商品,價格' in line:
			# continue # 如果商品價錢在line裡面的話，我就跳到下一回
		# name, price = line.strip().split(',') #去掉換行,讀到逗點就分割
		# products.append([name, price])
# print(products)

# 讓使用者輸入
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

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: # encoding utf-8為最廣泛使用的編碼,可以讀取中文字
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')