# 1. 피보나치 재귀로 구현하기

`v(0307 updated!)`

```python
# 재귀함수로 표현
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

N = int(input())
for i in range(1, N):
    print(fibo(i), end=' ')
```

# 2. 피보나치 DP로 구현하기

`v(0307 updated!)`

```python
# DP로 구현하기 (메모이제이션으로)
fib = [0, 1]
for i in range(N-2):
    fib.append(fib[-1]+fib[-2])
print(fib)
```

# 2.1.  DP 복습 - 0221 hws (swea 2005)

`v(0308 updated!)`

```python
# import sys
# sys.stdin = open('2005.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = []
    for i in range(1, N+1):
        pascal.append([1])     # 삼각형의 꼭지부분 생성
        for j in range(i-1):   # 윗부분에서 1을 뺀 값 (2개씩 묶어서 계산하니까)만큼 반복하고
            pascal[-1].append(sum(pascal[-2][j:j+2])) # 파스칼 리스트 밑부분에 바로 윗부분의 계산결과를 순서대로 삽입
    print('#{}'.format(tc))    # 파스칼 삼각형 출력하기
    for i in pascal:
        print(*i)
```

`comment` : 0221 때 제출한 코드는 삼각형의 꼭지부분과 두번째줄까지 출력했는데 이번에 코드 짰을때는 처음부터 출력할수 있엇음 !!! 뿌듯하다

# 3. DFS 구현하기

`v(0309 updated!)`

 ```python
 # 1. 시작노드에서 갈 수 있는 하위노드를 정해 모두 stack에 넣고 시작노드를 stack[-1]으로 변경
 # 2. 이것을 반복하면서 방문한 노드는 항상 visit에 넣다가
 # 3. 하위노드가 없으면 stack에서 노드를 pop하고 pop 한 값이 시작노드 변수에 할당되어 다시 1과 2를 반복하면 될듯?
 # 여기서 중요한게 - 조회하고 있는 노드가 방문노드리스트에 있는지를 먼저 검사하는것 : 이게 완전중요
 
 stack = [시작노드]
 visited = []
 
 while stack:
     v = stack[-1]
     if v not in visited:
         visited.append(v)
         for node in nodes[v]:
             stack.append(node)
     else:
         stack.pop()
 ```

# 3.1. swea 4871 그래프경로 풀이 

`v(0309 updated!)`

```python
#import sys
#sys.stdin = open('4871.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = []
    for i in range(51):
        nodes.append([])

    for e in range(E):
        front, back = map(int, input().split())
        nodes[front].append(back)
    S, G = map(int, input().split())

    # print(nodes)
    stack = [S]     # 방문할 예정인 정점을 임시누적하는 곳, 시작노드 S가 명시되어있기 때문에 미리 넣어둠
    visited = []   # 방문한 정점을 누적

    while stack:
        v = stack[-1]              # 시작노드를 stack[-1]으로
        if v not in visited:       # 지금 조회하고 있는 노드가 방문한 노드에 없으면 
            visited.append(v)      # 방문한 노드에 출석체크
            for node in nodes[v]:  # 조회하는 노드의 하위노드들을 
                stack.append(node) # 다 스택에 넣기
        else:
            stack.pop()            # 방문한 노드에 있으면 pop하기

    if G in visited:               # DFS를 마치고 방문한 노드들 최종본에 G가 있으면
        ans = 1                    # 1을 반환함
    else:
        ans = 0
    print('#{} {}'.format(tc, ans))
```

# 3.2. swea 1219 길찾기 풀이

`v(0309 updated!)`

```python
# import sys
# sys.stdin = open('1219.txt', 'r')

for tc in range(10):
    T, edge = map(int, input().split())
    pair = list(map(int, input().split()))
    nodes = []
    for i in range(100):
        nodes.append([])

    for i in range(0, edge*2-1, 2):
        nodes[pair[i]].append(pair[i+1])

    stack = [0]
    visited = []

    while stack:
        v = stack[-1]
        if v not in visited:
            visited.append(v)
            for node in nodes[v]:
                stack.append(node)
        else:
            stack.pop()

    if 99 in visited:
        ans = 1
    else:
        ans = 0
    print('#{} {}'.format(T, ans))
```

