// // 1. forEach
// const fr = ['a', 'b', 'c', 'd']

// fr.forEach((f, index) => {
//     console.log(f, index)
// })


// // 2. map
// const numbers = [1, 2, 3, 4, 5]

// const square = numbers.map(num => {
//     return num**2
// })

// console.log(square)


// // 3. filter
// const numbers = [1, 2, 3, 4, 5, [], 0]

// const oddNums = numbers.filter((num, index) => {
//     return !num
// })
// console.log(oddNums)


// 4. reduce
// const numbers = [1, 2, 3]

// const result = numbers.reduce((acc, num) => {
//     return acc + num
// }, 0)
// console.log(result)


// // 5. find
// const avg = [
//     {name: 'tony', age: 45},
//     {name: 'steve', age: 32},
//     {name: 'thor', age: 40},
// ]

// const result = avg.find(a => {
//     return a.name === 'thor'
// })

// console.log(result)


// // 6. some
// const numbers = [1, 3, 5, 7, 9]

// const hasEvenNumber = numbers.some(num => {
//     return num % 2 === 0
// })
// console.log(hasEvenNumber)

// const hasOddNumber = numbers.some(num => {
//     return num % 2 // === 1
// })
// console.log(hasOddNumber)


// // 7. every
// const numbers = [1, 3, 5, 7, 8]
// const hasEvenNumber = numbers.every(num => {
//     return num % 2
// })
// console.log(hasEvenNumber)