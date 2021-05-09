# 不定参数的函数定义，在参数前面的*表示输入的参数都存放在money中
def cost(*money):
	all = 0
	for one in money:
		all+=one
	return all

day1Spend = cost(10, 20, 10, 3, 3)		# 5个参数
day2Spend = cost(8, 12, 8, 2, 20, 10)	# 6个参数
print('第一天花费了%d' % day1Spend)
print('第二天花费了%d' % day2Spend)