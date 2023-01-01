# coroutine = cooperative routine

# 코루틴은 generator의 특별한 형태
# 제너레이터는 yield명령까지 실행하지만, 코루틴은 yield를 만나면 대기상태로 실행중지 후 원래루틴으로 돌아옴

# 따라서 한번에 코드가 끝나지 않고, 여러번 실행 가능(다음번 yield 전까지 실행)
# 이때 (끝난 것이 아니라면) 실행 후에도 내부 정보가 유지됨
# 코루틴은 entry point가 여러개인 함수



# 1. <코루틴에 값 보내기>
# 보내기: 코루틴객체.send(값)
# 받기: (코루틴 내부에서) 변수 = (yield)
def num_coroutine():
	while True:				# 코루틴을 계속 유지하기 위해(끝나지 않도록)
		x = yield			# 코루틴 밖에서 값을 받아옴, 반드시 괄호
		print(x)

co = num_coroutine()
# next(co)

co.send(10)					# x는 10, print 후에 다음번 yield를 만나므로 실행중지
co.send(20)
co.send(30)



# 2. <코루틴에서 외부로 값 전달하기>
# 외부에서 값을 넣으면서 + 외부로 yield도 하는 방법
# 외부값저장변수 = (yield 외부로내보낼값변수)

def mySum():
	total = 0
	while True:
		x = (yield total)
		total += x

c = mySum()
print(next(c))