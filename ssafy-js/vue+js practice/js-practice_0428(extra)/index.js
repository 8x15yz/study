// 코드를 작성해 주세요
const scissorsButton = document.querySelector('#scissors-button')
const rockButton = document.querySelector('#rock-button')
const paperButton = document.querySelector('#paper-button')
const modal = document.querySelector('.modal')
const modalContent = document.querySelector('.modal-content')

modal.addEventListener('click', function () {
  modal.style.display = 'none'
})

let count1 = 0
let count2 = 0

const playGame = (player1, player2) => {
  if (player1 === 'scissors') {
    if (player2 === 'rock') {
      count2 += 1
      return 2
    } else if (player2 === 'paper') {
      count1 += 1
      return 1
    }
  } else if (player1 === 'rock') {
    if (player2 === 'scissors') {
      count1 += 1
      return 1
    } else if (player2 === 'paper') {
      count2 += 1
      return 2
    }
  } else {
    if (player2 === 'scissors') {
      count2 += 1
      return 2
    } else if (player2 === 'rock') {
      count1 += 1
      return 1
    }
  }
  return 0
}
// buttonClickHandler의 리턴이 함수!
// 리턴되는 함수가 콜백 함수로 활용됨!
const buttonClickHandler = choice => event => {
  const cases = ['scissors', 'rock', 'paper']
  const randomIndex = Math.floor(Math.random() * 3)
  
  const playerImg = document.querySelector('#player1-img')
  const computerImg = document.querySelector('#player2-img')
  const winner = playGame(choice, cases[randomIndex])

  playerImg.src = `./img/${choice}.png`
  

  let i = randomIndex
  const timerId = setInterval(() => {
    i = (i + 1) % 3
    computerImg.src = `./img/${cases[i]}.png`
  }, 100)

  setTimeout(() => {
    clearInterval(timerId)
    
    const countA = document.querySelector('.countA')
    const countB = document.querySelector('.countB')

    countA.innerText = count1
    countB.innerText = count2
    computerImg.src = `./img/${cases[randomIndex]}.png`

    modalContent.innerText = winner ? `player${winner}의 승리입니다!` : '무승부 입니다!'
    modal.style.display = 'flex'
  }, 3000)
}

scissorsButton.addEventListener('click', buttonClickHandler('scissors'))
rockButton.addEventListener('click', buttonClickHandler('rock'))
paperButton.addEventListener('click', buttonClickHandler('paper'))
