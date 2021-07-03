import queue
data_queue = queue.Queue()

# 일반적인 큐
data_queue.put("hello world")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print("\n")
#LIFO 큐
data_queue2 = queue.LifoQueue()
data_queue2.put("hello_world")
data_queue2.put(1)

print(data_queue2.qsize())
print(data_queue2.get())
print(data_queue2.qsize())
print(data_queue2.get())
print("\n")

data_queue3 = queue.PriorityQueue()
data_queue3.put((10,"hello_world"))
data_queue3.put((5,1))
data_queue3.put((15,"china"))

print(data_queue3.qsize())
print(data_queue3.get())
print(data_queue3.qsize())
print(data_queue3.get())
print(data_queue3.qsize())
print(data_queue3.get())
print("\n")

