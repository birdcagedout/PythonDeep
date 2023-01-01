# 함수에 yield를 사용하여 generator를 정의하면 **쉽게** iterator를 구현할 수 있다.(generator는 iterator의 일종)

# <generator와 iterator의 차이>
# 1. iterator는 class 정의 + 특별한 메소드 재정의가 필요하다. generator는 함수 정의만으로 구현 가능하다.
# 2. iterator는 __next__함수 내에서 return으로 값을 보내지만, generator는 별도 class객체 없이, 별도 메소드 없이 yield만으로 같은 효과
# 3. iterator는 소진시 직접 StopIteration을 raise해야하지만, generator는 함수의 끝에 도달하면 자동으로 StopIteration 발생

# <generator를 구현하는 2가지 방법>
# 1. 함수(내부에 yield)
# 2. 표현식(괄호 컴프리헨션)


# 1. generator 함수
def gen123():
	print("1st num")
	yield 1
	print("2nd num")
	yield 2
	print("3rd num")
	yield 3


def genfor():
	for i in [1, 2, 3, 4]:
		yield i


gen = genfor()						# type(gen) ==> <class 'generator'>
next(gen)							# next(gen)은 gen.__next__()와 동일
next(gen)
next(gen)
next(gen)





# 2. generator 표현식
def show_all(s):
	for i in s:
		print(i, end=' ')

h = ( 2 * i for i in range(1, 10))	# type(gen) ==> <class 'generator'>
# show_all(h)






# 3. generator를 사용해서 range를 구현해보자
def myRange(stop):
	n = 0
	while n < stop:
		yield n
		n += 1

for i in myRange(10):
	print(i)





# 4. generator로 문자열을 대문자로 바꾸기
def myUpper(s):										# str형 리스트(컬렉션타입)를 전달받아서
	for item in s:
		yield item.upper()							# 각 str을 대문자로 바꾼  것을 yield

fruits = ['apple', 'banana', 'orange']

f = myUpper(fruits)
next(f)
next(f)




# 5. yield from 반복가능객체/이터레이터/제너레이터
def getFrom(s):
	yield from s

f1 = getFrom(fruits)
next(f1)
next(f1)