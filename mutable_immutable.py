# 파이썬의 변수 (강한 타입, Immutable vs Mutable, Class vs Instance) - 조인석 - PyCon.KR 2019
# https://www.youtube.com/watch?v=su9LkSogAMc



# 클래스 변수란?
class Programmer:
	lang = []							# 클래스 변수

	def __init__(self, name):
		self.name = name

	def add_lang(self, lang):
		self.lang.append(lang)

chris = Programmer('Chris')
chris.add_lang('python')
chris.add_lang('java')
print(chris.lang)						# ['python', 'java']


anna = Programmer('Anna')
print(anna.lang)						# ['python', 'java']

#****************************************
# <결론> class 변수는 instance간 공통
#****************************************



# 문제1.
class BookReader:
	country = 'Korea'

	def __init__(self, name):
		self.name = name 

	def read_book(self):
		print(self.name + ' is reading in ' + self.country)

chris = BookReader('Chris')
anna = BookReader('Anna')

chris.country = 'USA'					# country는 immutable하기 때문에 'USA'로 변경 = 새로운 country변수가 chris인스턴스에 할당됨!!

chris.read_book()						# USA		==> chris.country 변경 후에 "새로운 chris.country 변수"가 생성 (단, chris 인스턴스는 그대로)
anna.read_book()						# Korea
print(BookReader.country)				# Korea

#****************************************
# <결론> class 변수라는 사실보다
# mutable 변수라는 python 특성이 더 우선한다.
#****************************************




# 문제2.
BookReader.country = 'Italy'			# class변수 country 또한 immutable변수이므로 'Italy'를 담은 새로운 변수가 할당됨

chris.read_book()						# Chris is reading in USA		==> 이미 새로 할당된 country변수에 'USA'가 할당되었으므로 영향받지 않는다.
anna.read_book()						# Anna is reading in Italy		==> class 변수가 새로운 변수로 할당되었으므로 영향 받는다.

sean = BookReader('Sean')				# class변수 변경 후에 새로 생성한 sean 인스턴스에는 과연 이전 country 변수값인 'Korea'가 있을까? X
sean.read_book()						# Sean is reading in Italy


#****************************************
# <결론> class 변수 자체가 변경되면
# 그 변수를 참조하는 모든 인스턴스가 영향을 받지만
# 이미 이전에 class 변수가 변경된 인스턴스에는 영향주지 않는다.
#****************************************





# 해결법: 문제1, 문제2에 대한
class SKBookReader:														# 클래스명에 country를 명기
	_COUNTRY = 'Korea'													# 내부용으로 쓰일 변수는 _로 시작 + 대문자(상수임을 명기)

	def __init__(self, name):
		self.name = name 

	def read_book(self):
		print(self.name + ' is reading in ' + SKBookReader._COUNTRY)	# (중요) 인스턴스 변수인 self.country가 아니라 항상 클래스 변수 참조하도록


insuk = SKBookReader('Insuk')
insuk.read_book()						# Insuk is reading in Korea

insuk._COUNTRY = 'UK'					# 꼭 하지말라는데도 변경하는 놈 있다. 이제 insuk 인스턴스의 _COUNTRY 변수는 다른 클래스변수와 전혀다른값

insuk.read_book()						# 결과는? Insuk is reading in Korea



#****************************************
# <최종결론> 
# 1. class 변수는 객체가 인스턴스화되는 시점에 모두 "같은 변수"를 참조/조회하기 위한 목적으로 사용
# => class 변수는 mutable한 것이 좋고, 
# => 만약 immutable한데다 & class 변수값을 변경해야만 한다면 ==> 인스턴스로 접근(self.변수) 절대 금지
# 2. class 변수에 접근할 때는 무조건 클래스이름.변수로 접근할 것
#****************************************