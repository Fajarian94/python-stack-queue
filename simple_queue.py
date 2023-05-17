from collections import deque

queue = deque([1,2,3,4,5])
print('antrian sekarang : ',queue)

queue.append(6)
print('antirian masuk : ',6)
print('antrian sekarang : ',queue)

queue.append(7)
print('antirian masuk : ',7)
print('antrian sekarang : ',queue)

out = queue.popleft()
print('antirian keluar : ',out)
print('antrian sekarang : ',queue)