ns = [('Yoon', 33), ('Lee', 12), ('Park', 29), ('Kim', 22)]


# 1. 나이를 기준으로
def age(t):
	return t[1]

ns.sort(key=age)					# 오름차순
print(ns)

ns.sort(key=age, reverse=True)		# 내림차순
print(ns)



# 2. 이름을 기준으로
def name(t):
	return t[0]

ns.sort(key=name)
print(ns)							# 오름차순

ns.sort(key=name, reverse=True)		# 내림차순
print(ns)



# 3. 나이를 기준으로 + 람다식
ns.sort(key=lambda x: x[1])
print(ns)



# 4. 이름을 기준으로 + 람다식
ns.sort(key=lambda x: x[0])
print(ns)



# 5. 문자열의 길이를 기준으로
names = ['Jullia', 'Yoon', 'Silverstone', 'Kim']

names.sort(key=len)
print(names)



# 6. 튜플의 두수의 합 기준으로
nums = [(3,1), (2,9), (0,5), (1,1)]

nums.sort(key=sum)
print(nums) 



# 7. sorted()는 객체를 직접 바꾸지 않고, 정렬된 사본을 리턴한다.
org = [('Yoon', 33), ('Lee', 12), ('Park', 29), ('Kim', 22)]
cpy1 = sorted(org, key=lambda x: x[0])
cpy2 = sorted(org, key=lambda x: x[0], reverse=True)
print(org)
print(cpy1)
print(cpy2)



# 8. sorted(): 문자열로 표현된 숫자들의 정렬
org = ['321', '214', '1970', '44', '1']

cpy = sorted(org, key=int)
print(cpy)

