let score = 0;
let timeLeft = 60;
let gameInterval;
let bubbleInterval;
let isGameRunning = false;
let highScore = 0;
let currentUsername = null;

const gameArea = document.getElementById('game-area');
const scoreDisplay = document.getElementById('score');
const timerDisplay = document.getElementById('timer');
const startButton = document.getElementById('start-button');
const newUserButton = document.getElementById('new-user-button');
const highScoreDisplay = document.getElementById('high-score');
const usernameDisplay = document.getElementById('username');

// Bubble colors
const bubbleColors = [
    '#FF6B6B', // Red
    '#4ECDC4', // Turquoise
    '#45B7D1', // Blue
    '#96CEB4', // Green
    '#FFEEAD', // Yellow
    '#D4A5A5', // Pink
    '#9B59B6', // Purple
    '#E67E22', // Orange
    '#2ECC71', // Emerald
    '#F1C40F'  // Gold
];

async function registerNewUser() {
    const username = prompt('Enter your username:');
    if (!username) return;

    try {
        const response = await fetch('http://localhost:8000/api/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username: username })
        });

        const data = await response.json();
        if (data.status === 'success') {
            currentUsername = username;
            usernameDisplay.textContent = username;
            highScore = data.player.highscore;
            highScoreDisplay.textContent = highScore;
            
            // Enable the start button after successful registration
            startButton.disabled = false;
            startButton.textContent = 'Start Game';
            
            // Reset game state
            score = 0;
            scoreDisplay.textContent = score;
            timeLeft = 60;
            timerDisplay.textContent = timeLeft;
        } else {
            alert('Error registering user. Please try again.');
        }
    } catch (error) {
        console.error('Error registering user:', error);
        alert('Error registering user. Please try again.');
    }
}

async function updateHighScore() {
    if (!currentUsername) return;

    try {
        const response = await fetch('http://localhost:8000/api/update-highscore/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: currentUsername,
                score: score
            })
        });

        const data = await response.json();
        if (data.status === 'success') {
            highScore = data.player.highscore;
            highScoreDisplay.textContent = highScore;
        }
    } catch (error) {
        console.error('Error updating high score:', error);
    }
}

function createBubble() {
    const bubble = document.createElement('div');
    const size = 30 + Math.random() * 30; // Random size between 30 and 60
    bubble.style.width = `${size}px`;
    bubble.style.height = `${size}px`;
    bubble.style.backgroundColor = bubbleColors[Math.floor(Math.random() * bubbleColors.length)];
    bubble.style.borderRadius = '50%';
    bubble.style.position = 'absolute';
    bubble.style.left = Math.random() * (gameArea.offsetWidth - size) + 'px';
    bubble.style.top = gameArea.offsetHeight + 'px';
    bubble.style.boxShadow = '0 0 10px rgba(255, 255, 255, 0.5)';
    bubble.style.transition = 'transform 0.1s ease';
    gameArea.appendChild(bubble);

    let speed = 2 + Math.random() * 2;
    let position = gameArea.offsetHeight;

    function moveBubble() {
        position -= speed;
        bubble.style.top = position + 'px';

        if (position < -size) {
            bubble.remove();
        }
    }

    bubble.addEventListener('click', () => {
        bubble.remove();
        score += 1;
        scoreDisplay.textContent = score;
    });

    const moveInterval = setInterval(moveBubble, 16);
    bubble.dataset.interval = moveInterval;
}

function startGame() {
    if (!currentUsername) {
        alert('Please register a username first!');
        return;
    }

    if (isGameRunning) return;

    isGameRunning = true;
    score = 0;
    scoreDisplay.textContent = score;
    timeLeft = 60;
    timerDisplay.textContent = timeLeft;
    startButton.textContent = 'Game in Progress';
    startButton.disabled = true;
    newUserButton.disabled = true;

    gameInterval = setInterval(updateTimer, 1000);
    bubbleInterval = setInterval(createBubble, 1000);
}

function updateTimer() {
    timeLeft--;
    timerDisplay.textContent = timeLeft;

    if (timeLeft <= 0) {
        endGame();
    }
}

async function endGame() {
    clearInterval(gameInterval);
    clearInterval(bubbleInterval);
    isGameRunning = false;

    // Remove all bubbles
    const bubbles = gameArea.getElementsByTagName('div');
    while (bubbles.length > 0) {
        bubbles[0].remove();
    }

    // Update high score
    await updateHighScore();

    // Reset game state
    startButton.textContent = 'Play Again';
    startButton.disabled = false;
    newUserButton.disabled = false;
}

// Event Listeners
startButton.addEventListener('click', () => {
    if (isGameRunning) return;
    startGame();
});

newUserButton.addEventListener('click', () => {
    if (isGameRunning) {
        alert('Please wait for the current game to end!');
        return;
    }
    registerNewUser();
});


