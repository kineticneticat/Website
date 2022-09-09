canvas = document.getElementById('canvas')
ctx = canvas.getContext('2d')

canvas.width = 500
canvas.height = 500
debugger
class Cell {
	constructor(x, y) {
		this.x = x
		this.y = y
		this.cl = '#ffffff'
		this.cf = '#e0e0e0'
		this.state = null
	}

	draw() {
		ctx.beginPath()
		ctx.fillStyle = this.cf
		ctx.strokeStyle = this.cl
		ctx.rect(this.x, this.y, this.x+10, this.y+10)
		ctx.fill()
		ctx.stroke()
	}

	colour() {
		switch (this.state) {
			case null:
				return '#e0e0e0'
			case 'tobe':
				return '#d0d000'
			case 'open':
				return '#eeee00'
			case 'start':
				return '#00ee00'
		}
	}
	
}

let stateChecker = (state) => {
	switch (state) {
		case null:
			return 'tobe'
		case 'tobe':
			return 'tobe'
		case 'open':
			return 'open'
	}
}

grid = [
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

function redraw() {
	for (let i=0; i<50; i++) {
		for (let j=0; j<50; j++) {
			grid[i][j].draw()
		}
	}
}

for (let i=0; i<50; i++) {
	for (let j=0; j<50; j++) {
		grid[i].push(new Cell(i*10, j*10))
		grid[i][j].draw()
	}
}

grid[10][10].cf = '#00ee00'
grid[10][10].state = 'start'
grid[40][40].cf = '#ee0000'

//redraw()

// while (!grid[40][40].state) {
// 	for (let i=0; i<50; i++) {
// 		for (let j=0; j<50; j++) {

// 			if (grid[i][j].state == 'open' || grid[i][j].state == 'start') {
// 				grid[i][j+1].state = stateChecker(grid[i][j+1].state)
// 				grid[i][j-1].state = stateChecker(grid[i][j-1].state)
// 				grid[i+1][j].state = stateChecker(grid[i+1][j].state)
// 				grid[i-1][j].state = stateChecker(grid[i-1][j].state)
// 			}
			
// 		}
// 	}
// }

console.log(grid[20][20])