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

# 4. powerset 구하기

## 4.1. bitwise

`v(0313 updated!)`

https://08hyun15.tistory.com/entry/powerset-%EA%B5%AC%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-2%EA%B0%80%EC%A7%80-%EB%B9%84%ED%8A%B8%EC%97%B0%EC%82%B0%EC%9E%90DFS 

내 블로그에 설명 올림

```python 
arr = [1, 2, 3]
n = len(arr)
for i in range(1 << n):            
    track = []
    for j in range(n):
        print(bin(i))
        if i & (1 << j):
            track.append(j)
    print(track)
```

## 4.2. DFS

`v(0313 updated!)`

```python 
def powerset(i, N, K):
    global cnt                    # 전역변수 사용해서 함수 호출횟수 셈
    cnt += 1
    if i == N:
        sumsubset = 0             # 부분집합의 합을 만들기 위해 변수를 선언
        for j in range(N):
            if bit[j]:
                sumsubset+= a[j]  # 부분집합 합 구하기
        if sumsubset == K:        # 이때 합이 K와 동일하면
            for j in range(N):
                if bit[j]:        # 부분집합 원소를 출력하기
                    print(a[j], end=' ')
            print()
    else:
        bit[i] = 1                # DFS 탐색과정 코드
        powerset(i+1, N, K)
        bit[i] = 0
        powerset(i + 1, N, K)
    return

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*10
cnt = 0
powerset(0, 10, 10)
print(cnt)
```

## 4.3. backtraking

`v(0313 updated!)`

```python 
# 백트래킹으로 탐색 횟수 줄이기 (가지치기)
def powerset(i, N, s, K):
    global cnt
    cnt += 1
    if s == K:               # 부분집합 합이 K가 된다면 원소 출력하기
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()
    elif i == N:             # 더이상 고려할 원소가 없으면 멈춤
        return
    elif s > K:              # 부분집합 합이 K를 넘어도 멈춤
        return
    else:
        bit[i] = 1
        powerset(i+1, N, s+a[i], K)
        bit[i] = 0
        powerset(i + 1, N, s, K)
    return



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
cnt = 0
powerset(0, 10, 0, 10)
print(cnt)
```

```python
# 백트래킹 요소 하나 더 추가 : 남은 원소 rs를 다 더할때 K보다 작으면 멈춤
def powerset(i, N, s, K, rs):
    global cnt
    cnt += 1
    if s == K:
        for j in range(N):
            if bit[j]:
                print(a[j], end=' ')
        print()
    elif i == N:
        return
    elif s > K:
        return
    elif s+rs < K:
        return
    else:
        bit[i] = 1
        powerset(i+1, N, s+a[i], K, rs-a[i])
        bit[i] = 0
        powerset(i + 1, N, s, K, rs-a[i])
    return



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
cnt = 0
powerset(0, 10, 0, 55, sum(a))
print(cnt)
```

`comment`  : 물론 가지치기 중요하지만 일단 우리 수준에서는 모든 경우를 다 만들어 보는게 중요함

DFS 먼저 잘 익히도록 하자..



# 5. permutation 구하기 (종종 다시 생각이 필요)

`v(0314 updated!)`

## 기본구조 (수도코드)

```
def permutation():
	노드가 끝 부분에 도착했다면:
		리스트를 출력
	else:
		모아야 되는 리스트 크기만큼 반복:
			노드를 리스트에 추가
			permutation 호출
			노드 리스트에서 빼기
```

```
이 구조가 지금 순열을 트리로 표현할 때 모든 요소에 대해서 순서대로 조합한 것을 나타낸 것인데 
그림으로 보면 쉽다 예를 들어서 [1, 2, 3]의 순열을 구해야 된다면

                                     [ ]                                      단계 0
                             /        |          \
                       [1]           [2]            [3]                       단계 1
                   /      |         /    \         \      \
              [1, 2]    [1, 3]   [2, 1]  [2, 3]    [3, 1]  [3, 2]             단계 2
              /         /         |        |          |          \
     [1, 2, 3]   [1, 3, 2]   [2, 1, 3]  [2, 3, 1]    [3, 1, 2]    [3, 2, 1]   단계 3
   
이렇게 트리로 나타내고 0단계부터 DFS를 시작하는거임 3단계까지.. 이거를 재귀함수로 구현을 한 게 위의 코드
```

##  5.1. 코드1 (원소의 자리를 변경하는 식)

```python 
def f(i, N, s):
    if i == N:
        print(p, '  끝', ' 단계=', s)
        print()
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            print(p, i, j, '  단계=',s)
            f(i+1, N, s+1)
            p[i], p[j] = p[j], p[i]
            print(p, i, j,'*','단계=', s)


p = [1, 2, 3]
N = len(p)
f(0, N, 0)
```

## 5.2. 코드2 (원소를 추가하고 빼는 식)

```python 
def f(p, n, s):
    if s == t_cnt:
        print(p, '  끝', ' 단계=', s)
        print()
    else:
        for i in range(n):
            if not i in p:
                p.append(i)
                print(p, '  단계=',s)
                f(p, n, s+1)
                p.pop()
                print(p,'*','단계=', s)

t_cnt = 3
f([], 3, 0)
```

`comment`  : 이게 재귀함수로 구현해서 그렇지 왠지 반복문으로 돌리면 DFS 적용해서 만들어볼 수도 있을것 같다 ..

나중에 또 도전해보기

재귀함수에 익숙해져있지 않아서 지금 사실 트리 단계가 어떻게 뿌리 노드로 돌아갈 수 있는지도 도저히 감이 안 잡힘 ... ㅠㅠ 재귀함수를 많이 써보고 나서 알게 될것 같은 기분이다

