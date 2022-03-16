# 1. 큐 구현하기

## 1.1. 선형큐

```python 
a = [1, 2, 3]

queue = []
front = 0
rear = 0
# 큐 삽입 과정
while rear != len(a):
    queue.append(a[rear])
    rear += 1
    print(queue)
# 큐 삭제과정
while front != len(a):
    queue.pop(0)
    front += 1
    print(queue)
```



## 1.2. 원형큐