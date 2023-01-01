
# 0. 동시성 처리를 전혀 사용하지 않은 경우
# import time

# start = time.time()

# def sync_func():
#     for i in range(10):
#         time.sleep(0.5)
#         print(i)
# sync_func()
# end = time.time()
# print(f"Time elapsed: {end - start}")         # Time elapsed: 5.005761623382568



# 1. 동시성 처리를 사용한 경우: 비동기 함수를 1번만 실행시킨 경우에는 동시성 처리를 전혀 하지 않은 것과 결론적으로 같은 결과
# import asyncio
# import time

# start = time.time()
# async def myFunc():
#     for i in range(10):
#         await asyncio.sleep(0.5)            # 이벤트 루프를 블록하지 않음
#         print(i)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(myFunc())
# loop.close()
# end = time.time()
# print(f"Time elapsed: {end - start}")       # Time elapsed: 5.0039849281311035



# 2. 동시성 처리를 전혀 사용하지 않고 여러번 호출하는 경우
# import time

# start = time.time()

# def sync_func():
#     for i in range(10):
#         time.sleep(0.5)
#         print(i)

# sync_func()
# sync_func()
# sync_func()

# end = time.time()
# print(f"Time elapsed: {end - start}")         # Time elapsed: 15.0193510055542




# 3. 동시성 처리를 사용 + 여러번 호출하는 경우: 비로소 동시성 처리가 의미있는 결과
import asyncio
import time

start = time.time()
async def myFunc():
	for i in range(10):
		await asyncio.sleep(0.5)            # 이벤트 루프를 블록하지 않음
		print(i)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(myFunc(), myFunc(), myFunc()))
loop.close()
end = time.time()
print(f"Time elapsed: {end - start}")       # Time elapsed: 5.005816698074341





# 4. 동시성 처리를 사용 + 여러번 호출하는 경우: future객체 사용
# import asyncio
# import time

# start = time.time()
# async def myFunc():
#     for i in range(10):
#         await asyncio.sleep(0.5)            # 이벤트 루프를 블록하지 않음
#     return "Test"

# # loop = asyncio.get_event_loop()
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)

# asyncio.run(asyncio.gather(
#     asyncio.ensure_future(myFunc()),
#     asyncio.ensure_future(myFunc()),
#     asyncio.ensure_future(myFunc()),
# ))
# loop.close()
# end = time.time()
# print(f"Time elapsed: {end - start}")       # Time elapsed: 5.005816698074341