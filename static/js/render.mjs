import {Cre} from "./objects.mjs"
import {data} from './things.mjs'
Create = new Cre()

const canvas = document.getElementById('canvas')
const ctx = canvas.getContext("2d")
canvas.width = 500
canvas.height = 500

let focused = true

export let settings = {
	near:10,
	far:100
}
export let player = {
    x: 0,
    y: 0,
    z: -50,
		rx:0,
		ry:0,
		rz:0
}
export let sun = {
	x: 50,
	y: 50,
	z: 50
}
let aaa = -51
let obj = []


for (let i=0;i<data.length;i++) {
	switch (data[i].type) {
		case 'cube' :
			obj.push(Create.Cube(
				data[i]['pos'][0], -data[i]['pos'][1], data[i]['pos'][2], 
				data[i]['size'][0], data[i]['size'][1], data[i]['size'][2], 
				data[i]['rot'][0], data[i]['rot'][1], data[i]['rot'][2], 
				data[i]['colour']
			))
		case 'point':
			obj.push(Create.Point(
				data[i]['pos'][0],
				-data[i]['pos'][1],
				data[i]['pos'][2],
			))
		// case 'custom':
		// 	obj.push(Create.Custom(data[i]['Vertices'], data[i]['Edges'], data[i]['Faces'], data[i]['colour']))
			
	}
}	


//sun
// obj.push(Create.Cube(sun.x, -sun.y, sun.z, 0, 0, 0, '#000000'))

//foor
for (let i=0;i<10; i++) {
	obj.push(Create.Line(50, 20, (i-5)*10, 
											 -50, 20, (i-5)*10))
	obj.push(Create.Line((i-5)*10, 20, 50, 
											 (i-5)*10, 20, -50))
}

console.log(obj)
let keyW, keyA, keyS, keyD, keySp, keySh, keyRi, keyLe, keyUp, keyDo = false
window.onload = () => {
    
    // 
    loop()
}

window.addEventListener("keydown", () => {
    var keyCode = event.keyCode;
    console.log(keyCode)
    switch (keyCode) {
        case 68: //d
            keyD = true
            break
        case 83: //s
            keyS = true
            break
        case 65: //a
            keyA = true
            break
        case 87: //w
            keyW = true
            break
        case 32: //space
            keySp = true
            break
        case 16: //shift
            keySh = true
            break
				case 39: // right
						keyRi = true
						break
				case 37: // left
						keyLe = true
						break
				case 38: // up
						keyUp = true
						break
				case 40: // down
						keyDo = true
						break
				
        
    }
})
window.addEventListener("keyup", () => {
    var keyCode = event.keyCode;
    switch (keyCode) {
        case 68: //d
            keyD = false;
            break;
        case 83: //s
            keyS = false;
            break;
        case 65: //a
            keyA = false;
            break;
        case 87: //w
            keyW = false;
            break;
        case 32: //space
            keySp = false;
            break;
        case 16: //shift
            keySh = false;
            break;
				case 39: // right
						keyRi = false
						break
				case 37: // left
						keyLe = false
						break
				case 38: // up
						keyUp = false
						break
				case 40: // down
						keyDo = false
						break
    }
})



function loop() {
    // console.log(keyRi, keyLe)
		// console.log(player)
		document.getElementById('stuff').innerHTML = JSON.stringify(obj)
		document.getElementById('out').innerHTML = JSON.stringify(player)
    ctx.clearRect(0, 0, canvas.width, canvas.height)
		if (true) {
    	for (let i=0;i<obj.length;i++) {
        obj[i].draw()
        if (keyW) {
					obj[i].pMove(0, 0, -1)
        }
        if (keyA) {
					obj[i].pMove(1, 0, 0)
	        }
	        if (keyS) {
						obj[i].pMove(0, 0, 1)
	        }
	        if (keyD) {
						obj[i].pMove(-1, 0, 0)
	        }
	        if (keySp) {
						obj[i].pMove(0, 1, 0)
	        }
	        if (keySh) {
						obj[i].pMove(0, -1, 0)
	        }
					if (keyRi) {
						obj[i].pTurn(1, 0)
					}
					if (keyLe) {
						obj[i].pTurn(-1, 0)
					}
					if (keyUp) {
						obj[i].pTurn(0, -1)
					}
					if (keyDo) {
						obj[i].pTurn(0, 1)
					}
	    }
		}
    requestAnimationFrame(loop)
}