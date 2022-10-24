import {player} from './render.mjs'
import {sun} from './render.mjs'

const scale = 50
const canvas = document.getElementById('canvas')
const ctx = canvas.getContext("2d")
/////////////////////////////////////////////
class Vertex {
    constructor(x, y, z, c) {
        this.x = x
        this.y = y
        this.z = z
				this.cx = x
				this.cy = y
				this.cz = z
        this.c = c
        this.show = true
    }
    
    project() {
        this.prox = (this.cx*scale/(this.cz+scale))*10+250
        this.proy = (this.cy*scale/(this.cz+scale))*10+250
    }

		cull() {
			if (this.z > player.z) {
				this.show = false
			}	else {
				this.show = true
			}
		}

    draw() {
				//this.cull()
        this.project()
        if (this.show) {
            ctx.beginPath()
            ctx.fillStyle = this.c
            ctx.arc(this.prox, this.proy, 2, 0, Math.PI*2)
            ctx.fill()
        }
    }
}
/////////////////////////////////////////////
class Edge {
    constructor(a, b, c) {
        this.a = a
        this.b = b
    }

    draw() {
        if (this.a.show && this.b.show) {
            ctx.beginPath()
            ctx.fillStyle = this.c
            ctx.moveTo(this.a.prox, this.a.proy)
            ctx.lineTo(this.b.prox, this.b.proy)
            ctx.stroke()
        }
        
    }
}
/////////////////////////////////////////////
class Face {
    constructor(v, c) {
        this.v = v
    }
    draw() {
			if (this.cull()) {
        ctx.beginPath()
        ctx.fillStyle = this.shade()
        ctx.moveTo(this.v[0].prox, this.v[0].proy)
        for (let i = 1; i<this.v.length;i++) {
            ctx.lineTo(this.v[i].prox, this.v[i].proy)
        }
        ctx.closePath()
        ctx.fill()
				ctx.fillStyle = '#000000'
			}
    }

		cull() {
			for (let i=0;i<this.v.length;i++) {
				if (!this.v[i].show) {
					return false
				}
			}
			return true
		}
	
		shade() {
			return this.c
		}
}
/////////////////////////////////////////////
class Obj {
    constructor(Verts, Edges, Faces) {
        this.v = Verts
        this.e = Edges
        this.f = Faces
    }

    draw() {
        
        for (let i=0;i<this.e.length;i++) {
            this.e[i].draw()
        }
        for (let i=0;i<this.f.length;i++) {
            this.f[i].draw()
        }
        for (let i=0;i<this.v.length;i++) {
            this.v[i].draw()
        }
    }

    pMove(dx, dy, dz) {
        for (let i=0;i<this.v.length;i++) {
            this.v[i].cx += dx
            this.v[i].cy += dy
            this.v[i].cz += dz
        }
    }

		pTurn(lr, ud) {
			if (true) {
				lr *= Math.PI/180
				ud *= Math.PI/180
				for (let i=0;i<this.v.length;i++) {
					
					player.ry += lr
					// Y
					let x = this.v[i].cx
					let z = this.v[i].cz

					x -= player.x
					z -= player.z

					let xPrime = x*Math.cos(lr) - z*Math.sin(lr)
					let zPrime = x*Math.sin(lr) + z*Math.cos(lr)
					
					this.v[i].cx = xPrime + player.x
					this.v[i].cz = zPrime + player.z
				}
			}
			
			for (let i=0;i<this.v.length;i++) {
				player.rx += ud
				// X
          	let y = this.v[i].cy
          	let z = this.v[i].cz

						y -= player.y
						z -= player.z

						let yPrime = y*Math.cos(ud) - z*Math.sin(ud)
						let zPrime = y*Math.sin(ud) + z*Math.cos(ud)

						this.v[i].cy = yPrime + player.y
            this.v[i].cz = zPrime + player.z
			}
		}
}
/////////////////////////////////////////////
class Tri {
	constructor(a, b, c) {
		this.a = a
		this.b = b
		this.c = c
	}
}
/////////////////////////////////////////////
export class Cre {
    Cube(x, y, z, wx, wy, wz, rx, ry, rz, c) {

				let beforeRot = [
					[x,    y,    z],
					[x+wx, y,    z],
					[x,    y+wy, z],
					[x+wx, y+wy, z],
					[x,    y,    z+wz],
					[x+wx, y,    z+wz],
					[x,    y+wy, z+wz],
					[x+wx, y+wy, z+wz]
				]
			
        let v = []

				for (let i=0;i<beforeRot.length;i++) {
					let R = beforeRot[i]
					let Rx = helper.Rx(R[0], R[1], R[2], rx)
					let Rxy = helper.Ry(Rx[0], Rx[1], Rx[2], ry)
					let Rxyz = helper.Rz(Rxy[0], Rxy[1], Rxy[2], rz)
					v.push(new Vertex(Rxyz[0], Rxyz[1], Rxyz[2], c))
				}
				console.log(v)
			
				let e =[
            new Edge(v[0], v[1]), new Edge(v[1], v[3]), new Edge(v[3], v[2]), new Edge(v[2], v[0]), new Edge(v[4], v[5]), new Edge(v[5], v[7]), new Edge(v[7], v[6]), new Edge(v[6], v[4]), new Edge(v[0], v[4]), new Edge(v[1], v[5]), new Edge(v[2], v[6]), new Edge(v[3], v[7])
        ]
        let f = [
            new Face([v[0], v[1], v[3], v[2]])
        ]
    
        return new Obj(v, e, f)
    }
	/////////////////////////////////////////////////////
    Point(x, y, z) {
        return new Obj([new Vertex(x, y, z)], [], [])
    }
	/////////////////////////////////////////////////////
    Line(x1, y1, z1, x2, y2, z2) {
        let v = [new Vertex(x1, y1, z1), new Vertex(x2, y2, z2)]
        let e = [new Edge(v[0], v[1])]
        let f = []
        return new Obj(v, e, f)
    }
	////////////////////////////////////////////////////////
		Prism(cx, cy, cz, l, s, r, c) {
			let v = []
			let e = []
			let f = []
			//base
			let basePoints = []
			let div = 360/s
			for (let i=0; i<s; i++) {
				basePoints.push(new Vertex(Math.cos(div*i)*r, cy, Math.sin(div*i)*r))
			}
			v = basePoints
			return new Obj(v, e, f)
		}
	//////////////////////////////////////////////////////
		Custom(v, e, f, c) {
			newV = []
			for (let i=0; i<v.length; i++) {
				newV.push(new Vertex(v[i][0], v[i][1], v[i][2]))
			}
			newE = []
			for (let i=0; i<e.length; i++) {
				newE.push(new Edge(newV[e[i][0]], newV[e[i][1]]))
			}
			newV = []
			// for (let i=0; i<v.length; i++) {
			// 	newV.push(new Vertex(v[i][0], v[i][1], v[i][2]))
			// }
			
			return new Obj(newV, newE, newF)
		}
}

window.Create = new Cre
////////////////////////////////////////////
class Help {
	Rx(x, y, z, theta) {
		return [
			1*x + 0*y + 0*z,
			0*x + Math.cos(theta)*y - Math.sin(theta)*z,
			0*x + Math.sin(theta)*y + Math.cos(theta)*z
		]
	}
	Ry(x, y, z, theta) {
		return [
			Math.cos(theta)*x + 0*y + Math.sin(theta)*z,
			0*x + 1*y + 0*z,
			-Math.sin(theta)*x + 0*y + Math.cos(theta)*z
		]
	}
	Rz(x, y, z, theta) {
		return [
			Math.cos(theta)*x + -Math.sin(theta)*y + 0*z,
			Math.sin(theta)*x + Math.cos(theta)*y + 0*z,
			0*x + 0*y + 1*z
		]
	}
	multiply(a, b) {
	  var aNumRows = a.length, aNumCols = a[0].length,
	      bNumRows = b.length, bNumCols = b[0].length,
	      m = new Array(aNumRows);
	  for (var r = 0; r < aNumRows; ++r) {
	    m[r] = new Array(bNumCols);
	    for (var c = 0; c < bNumCols; ++c) {
	      m[r][c] = 0;
	      for (var i = 0; i < aNumCols; ++i) {
	        m[r][c] += a[r][i] * b[i][c];
	      }
	    }
	  }
	  return m;
	}

}
let helper = new Help