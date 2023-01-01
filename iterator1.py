# iterator 객체 만들기
# iterable객체와 iterator는 다르다: iterable객체.__iter__()가 반환하는 것이 iterator
# 필수: __iter__(), __next__() 메소드를 구현한다.
# 인덱스로 접근시: __getitem__() 메소드만 구현해도 됨(__iter__, __next__ 생략 가능)


# __iter__(), __next__()만 구현
class Counter:
	def __init__(self, stop):
		self.current = 0
		self.stop = stop
	
	def __iter__(self):
		return self						# 현재 객체가 iterable객체이면서 iterator이므로 iterator는 자기자신
	
	def __next__(self):
		if self.current < self.stop:
			r = self.current
			self.current += 1
			return r
		else:
			raise StopIteration

# c = Counter(5)
# for i in c:
# 	print(i)


# __getitem__()만 구현
class Counter2:
	def __init__(self, stop):
		self.current = 0
		self.stop = stop

	def __getitem__(self, index):
		if index < self.stop:
			return index
		else:
			raise IndexError

c2 = Counter2(3)
print(c2[0], c2[1], c2[2])		# 이렇게도 접근 가능

for i in c2:					# 이건 원래 가능
	print(i)

