const playerElement = document.querySelector('.player');
const tubusElement = document.querySelector('.tubus');
const scoreElement = document.querySelector('.score');
const restartGameElement = document.querySelector('.restart-game');
const gameConteinerElement = document.querySelector('.game-conteiner');

const TUBUS_SIZE = ['s', 'm', 'l'];
const speed = 3000;


function addJumpListener() {
    document.addEventListener('keydown', event => {
        if(event.key === ' ' || event.key === 'ArrowUp') {
            jump();
        }
    })
}

let jumping = false;
function jump() {
    if(jumping) {
        return;
    }

    jumping = true;
    playerElement.classList.add('jump');
    setTimeout(() => {
        playerElement.classList.remove('jump');
        jumping = false;
    }, 1200)
}

let collisionInterval;
function monitorCollision() {
    collisionInterval = setInterval(() => {
        if(isCollision()) {
            stopGame();
            score = 0;
        }
    }, 10);
}

function isCollision() {
    const playerClientReact = playerElement.getBoundingClientRect();
    const playerR = playerClientReact.right;
    const playerL = playerClientReact.left;
    const playerB = playerClientReact.bottom;

    const tubusClientReact = tubusElement.getBoundingClientRect();
    const tubusR = tubusClientReact.right;
    const tubusL = tubusClientReact.left;
    const tubusT = tubusClientReact.top;

    const xCollision = tubusR > playerL && tubusL < playerR;
    const yCollision = playerB > tubusT;

    return xCollision && yCollision;
}

let score = 0;
function setScore(newScore) {
    scoreElement.innerHTML = score = newScore;

}

let scoreInterval;
function countScore() {
    scoreInterval = setInterval(() => {
        setScore(score + 1);
    }, 500);
}

function getRandomTubusSize() {
    const index = Math.floor(Math.random() * (TUBUS_SIZE.length));
    return TUBUS_SIZE[index];
}

let changeTubusInterval;
function randomTubus() {
    changeTubusInterval = setInterval(() => {
        const tubusSize = getRandomTubusSize();
        tubusElement.className = 'tubus tubus-' + tubusSize;
    }, speed);
}

function stopGame() {
    clearInterval(collisionInterval);
    clearInterval(scoreInterval);
    clearInterval(changeTubusInterval);
    restartGameElement.classList.add('show');
    gameConteinerElement.classList.add('stop');
    tubusElement.classList.add('stop');
    playerElement.classList.add('stop');
}

function restart() {
    location.reload();
}

function main() {
    monitorCollision();
    addJumpListener();
    countScore();
    randomTubus();
}

main();