const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const tileSize = 20;
const rows = canvas.height / tileSize;
const cols = canvas.width / tileSize;

const pacman = {
    x: 1,
    y: 1,
    direction: 'right',
    draw() {
        ctx.fillStyle = 'yellow';
        ctx.beginPath();
        ctx.arc(this.x * tileSize + tileSize / 2, this.y * tileSize + tileSize / 2, tileSize / 2, 0.2 * Math.PI, 1.8 * Math.PI);
        ctx.lineTo(this.x * tileSize + tileSize / 2, this.y * tileSize + tileSize / 2);
        ctx.fill();
    },
    move() {
        if (this.direction === 'right' && this.x < cols - 1) this.x++;
        if (this.direction === 'left' && this.x > 0) this.x--;
        if (this.direction === 'up' && this.y > 0) this.y--;
        if (this.direction === 'down' && this.y < rows - 1) this.y++;
    }
};

const walls = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
];

function drawWalls() {
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (walls[row][col] === 1) {
                ctx.fillStyle = 'blue';
                ctx.fillRect(col * tileSize, row * tileSize, tileSize, tileSize);
            }
        }
    }
}

function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawWalls();
    pacman.move();
    pacman.draw();
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight') pacman.direction = 'right';
    if (event.key === 'ArrowLeft') pacman.direction = 'left';
    if (event.key === 'ArrowUp') pacman.direction = 'up';
    if (event.key === 'ArrowDown') pacman.direction = 'down';
});

setInterval(update, 200);
