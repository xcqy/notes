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


# 实现一个two sum的检测接口，时间复杂度不限（如：[1,2,3]，找4，返回True，找10，返回False）
def sum(l, num):
	for i in range(len(l)):
		for j in range(len(l)):
			if i != j:
				if l[i] + l[j] == num:
					return True
	return False


# 冒泡排序
def mp_sort(l):
	for i in range(1, len(l)):
		for j in range(len(l) - i):
			if l[j] > l[j+1]:
				l[j] ,l[j+1] = l[j+1], l[j]
	print(l)
	return l


# 给定一个字符串，由6种括号组成，判定字符串是否组成合法的括号序列，合法的如：’{}’/‘{[]}’，不合法的如：’}{‘/‘{[}]’
BRACKET = {'}': '{', ')': '(', ']': '['}
BRACKET_L, BRACKET_R = BRACKET.values(), BRACKET.keys()
def check_bracket(s):
	arr = []
	for i in s:
		if i in BRACKET_L:
			arr.append(i)
		elif i in BRACKET_R:
			if arr and arr[-1] == BRACKET[i]:
				arr.pop()
			else:
				return False
	if len(arr) == 0:
		return True
	return False