// // 1. includes
// // 특정 문자열의 존재여부를 참거짓으로 반환
// const str = 'a santa at nasa'
// console.log(str.includes('santa'))
// console.log(str.includes('asan'))


// // 2. split
// // 문자열을 토큰 기준으로 나눈 배열 반환
// const str = 'a cup'
// console.log(str.split()) // value 가 없는 경우 기존 문자열을 배열에 담아 반환함
// console.log(str.split('')) // 한 문자단위씩 쪼갬
// console.log(str.split(' '))


// // 3. replace : string.replace(from, to)
// // 해당 문자열을 대상 문자열로 교체하여 반환
// // replace는 찾은 from값 하나만 바꾸는데 
// // replacAll은 찾은 from값을 다 변환시킴
// const str = 'a b c d'
// console.log(str.replace(' ', '-'))
// console.log(str.replaceAll(' ', '-'))


// 4. trim
// 문자열의 좌우 공백 제거하여 반환
// trim은 모든 공백문자
// trimStart는 문자열 시작의 공백문자
// trimEnd는 문자열 끝의 공백문자
const str = '    hello    '
console.log(str.trim())
console.log(str.trimStart())
console.log(str.trimEnd())

