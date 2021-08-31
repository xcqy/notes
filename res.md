第一题

	```
	# 实现一个string的单词内部倒序输出接口（如：‘abc def’ -> ‘cba fed’）
	def str_reversel(s):
		a = s.split(' ')
		res = ''
		num = 0
		for i in a:
			num += 1
			res += i[::-1]
			if num < len(a):
				res += ' '
		print(res)
		return res

	str_reversel('abc def')
	```

第二题
