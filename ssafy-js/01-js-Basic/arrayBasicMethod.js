// // 1. reverse
// // 원본 배열의 요소를 반대로 정렬
// const numbers = [1, 2, 3, 4, 5]
// numbers.reverse()
// console.log(numbers)


// // 2. push & pop
// // push : 배열 뒤에 요소추가
// // pop : 배열의 마지막 요소 제거
// const numbers = [1, 2, 3, 4, 5]
// numbers.push (9)
// console.log(numbers)
// numbers.pop()
// console.log(numbers)


// // 3. unshift & shift
// // unshift : 배열의 앞에 요소추가
// // shift : 배열의 첫번째  요소 제거
// const numbers = [1, 2, 3, 4, 5]
// numbers.unshift(9)
// console.log(numbers)
// numbers.shift()
// console.log(numbers)


// // 4. includes
// // 배열에 특정 값이 존재하는지 판별 후 
// // 참 또는 거짓 반환
// const numbers = [1, 2, 3, 4, 5]
// console.log(numbers.includes(2))
// console.log(numbers.includes(8))


// // 5. indexOf
// // 배열에 특정 값이 존재하는지 찾고 
// // 가장 첫번째로 찾은 요소의 인덱스를 반환함
// // 해당값이 없으면 -1 반환
// const numbers = [1, 2, 3, 4, 5]
// let result
// result = numbers.indexOf(3)
// console.log(result)
// result = numbers.indexOf(8)
// console.log(result)


// // 6. join : array.join([separator])
// // 배열의 모든 요소를 연결하여 반환
// // separator 구분자는 선택적으로 지정하고 
// // 선택자를 생략하면 기본값이 쉼표임
// const numbers = [1, 2, 3, 4, 5]
// let result
// result = numbers.join()
// console.log(result)
// console.log(numbers.join(''))
// console.log(numbers.join(' '))
// console.log(numbers.join('-'))

// 7. spread operator
// spread operator (...)
const array = [1, 2, 3]
const newArray = [7, ...array, 10]
console.log(newArray)

