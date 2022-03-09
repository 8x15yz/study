# 1. DP

## 1.1. 피보나치 재귀로 구현하기

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

## 1.2. 피보나치 DP로 구현하기

`v(0307 updated!)`

```python
# DP로 구현하기 (메모이제이션으로)
fib = [0, 1]
for i in range(N-2):
    fib.append(fib[-1]+fib[-2])
print(fib)
```

## 1.3.  DP 문제 - swea 2005 파스칼 삼각형

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

# 2. DFS 

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

## 2.1. swea 4871 그래프경로 

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

## 2.2. swea 1219 길찾기

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

# 3. backtracking

## 3.1. swea 4875 미로 

`v(0309 updated!)`

```python
# import sys
# sys.stdin = open('4875.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    padding = [1]*(N+2)
    maze = [padding]+[[1]+list(map(int, input()))+[1] for _ in range(N)]+[padding]

    for i in range(N+2):                       # 행렬을 하나씩 조회하면서
        if 2 in maze[i]:                       # 2를 먼저 찾기 -> 시작노드로 지정
            start = [i, maze[i].index(2)]
        elif 3 in maze[i]:                     # 3도 같이 찾고 여기는 끝노드로 지정
            end = [i, maze[i].index(3)]


    stack = [start]                            # DFS 적용하는데 이번에는 방문노드가 아니라 방문좌표를 스택에 저장
    visited = []
    ans = 0
    while stack:
        v = stack[-1]                          # 스택 top의 좌표를 현재 조회노드로 지정하고
        if v not in visited:
            visited.append(v)
            ud = [-1, 1, 0, 0]
            lr = [0, 0, -1, 1]
            for i in range(4):
                track = [v[0]+ud[i], v[1]+lr[i]]  # 델타 사용해서 값이 0 혹은 3인 길을 탐색하고
                if maze[track[0]][track[1]] != 1 and track not in visited:
                    stack.append(track)           # 방문예정 좌표들을 stack에 push
        else:
            stack.pop()                           # 현재 방문한 좌표 기준으로 길이 없으면 pop해서 돌아가기
        if visited[-1] == end:                    # 이 문제에서 중요한 것 **
            ans = 1                               # 3을 발견하게 되면 그 즉시 멈추기 (나름의 가지치기라고 생각함 .. ㅎ)
            break

    print('#{} {}'.format(tc, ans))
```

`comment` : 이거뭘까 .. 일단 DFS로 접근해서 풀었는데 시간초과가 나서 줄일방법을 열심히 생각했는데 아무래도 이게 백트래킹 관련 문제다 보니 가지치기ㅡㄹ 해야 되지 않을까 싶어서 그쪽으로 아이디어를 생각해봤다 (나머지 가능성이 남아있는 상태에서 먼저 답을 찾아버리면 그냥 while을 빠져나오도록 작성)

이것도 나름의 가지치기라고 생각한다. .. ㅎㅎ 내 코드가 정답이 아닌것같긴 하지만 결론적으로는 pass!! 거의 10번의 시도만에 받은 pass인듯 하다

## 3.2. swea 2806 Nqueen 풀이 

```python
```

