# 파이썬의 변수 (강한 타입, Immutable vs Mutable, Class vs Instance) - 조인석 - PyCon.KR 2019
#  https://youtu.be/su9LkSogAMc?t=1074




def scope_test():

	def do_local():
		spam = 'local spam'
	
	def do_nonlocal():
		nonlocal spam
		spam = 'nonlocal spam'

	def do_global():
		global spam
		spam = 'global spam'

	spam = 'free'

	do_local()
	print('After do_local: ', spam)

	do_nonlocal()
	print('After do_nonlocal: ', spam)

	do_global()
	print('After do_global: ', spam)


scope_test()
print("In global scope: ", spam)


# After do_local:  free
# After do_nonlocal:  nonlocal spam
# After do_global:  nonlocal spam
# In global scope:  global spam