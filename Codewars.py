#Codewars 1
def array_diff(a,b):
	c=[]
	for i in a:
		flag=0
		for j in b:
			if i==j:
				flag=1
				break
		if flag!=1:
			c.append(i)
	return c

def array_diff(a,b):
	return [x for x in a if x not in b]
	return filter(lambda i:i not in b,a)

#Codewars 2
def likes(names):
	if len(names)==0:
		return "no one likes this"
	elif len(names)==1:
		return ("%s likes this" %(names[0]))
	elif len(names)==2:
		return ("%s and %s like this" %(names[0],names[1]))
	elif len(names)==3:
		return ("%s, %s and %s like this" %(names[0],names[1],names[2]))
	else:
		return ("%s, %s and %d others like this" %(names[0],names[1],len(names)-2))

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
#两者等价，上面的是一种简写，类似switch
def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n,4)].format(*names, others=n-2)

#Codewars 3
def find_it(seq):
	for i in seq:
		count=0
		for j in seq:
			if i==j:
				count+=1
		if count%2==1:
			return i

def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
#如果没有[0]会返回一个数组，因为三个数都满足条件

#Codewars 4
def sum_two_smallest_numbers(numbers):
	numbers.sort()
	return numbers[0]+numbers[1]

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

#Codewars 5
def binary_array_to_number(arr):
	a=[]
	x=0
	arr.reverse()
	for i in range(len(arr)):
		a.append(2**i)
		x+=a[i]*arr[i]
	return x

def binary_array_to_number(arr):
  return int("".join(map(str, arr)), 2)
#join 合并了字符串,而int(a,2)则是把字符串认为是二进制转换为十进制,map的批量处理