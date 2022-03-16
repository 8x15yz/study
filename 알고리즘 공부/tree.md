# 1. tree 순회 3가지 구현하기

`0316 updated!`

```python
## 1. 전위순회
def preorder(n):
    if n <= N:
        print(tree[n], end=" ")
        preorder(n*2)
        preorder(n*2+1)


## 2. 중위순회
def inorder(n):
    if n <= N:
        inorder(n*2)
        print(tree[n], end=" ")
        inorder(n*2+1)

## 3. 후위순회
def postorder(n):
    if n <= N:
        postorder(n*2)
        postorder(n*2+1)
        print(tree[n], end=" ")

N = 8
tree = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print('1. preorder: ',end="")
preorder(1)
print()
print('2. inorder: ',end="")
inorder(1)
print()
print('3. postorder: ',end="")
postorder(1)
```

```
## 결과
1. preorder: 1 2 4 8 5 3 6 7 
2. inorder: 8 4 2 5 1 6 3 7 
3, postorder: 8 4 5 2 6 7 3 1 
```



# 2. 트리 표현하기

```python 
```

