export let data = [
	//pillar
	{'type': 'cube', 'pos': [15,0,0], 'size': [5,1,5], 'rot': [0,0,0], 'colour': '#000000', 'change': (tick) => {}},
	{'type': 'cube', 'pos': [-15,0,0], 'size': [5,1,5], 'rot': [0,0,0], 'colour': '#000000'},
	{'type': 'cube', 'pos': [15,20,0], 'size': [5,1,5], 'rot': [0,0,0], 'colour': '#000000'},
	{'type': 'cube', 'pos': [-15,20,0], 'size': [5,1,5], 'rot': [0,0,0], 'colour': '#000000'},
	{'type': 'cube', 'pos': [15,0,0], 'size': [5,1,5], 'rot': [0,0,0], 'colour': '#000000'},
	{'type': 'cube', 'pos': [-15,0,0], 'size': [5,1,5], 'rot': [0,0,0], 'colour': '#000000'},
	{'type': 'point', 'pos': [35, 35, 20]},
	{'type': 'point', 'pos': [35, -35, 20]},
	{'type': 'point', 'pos': [-35, 35, 20]},
	{'type': 'point', 'pos': [-35, -35, 20]},
	{'type': 'cube', 'pos': [0, 0, 0], 'size': [10, 10, 10], 'rot': [45, 45, 45], 'colour': '#000000'}
]

class Vector3 {
	constructor(x, y, z) {
		this.x = x
		this.y = y
		this.z = z
	}
}

class Transform {
	constructor(transform, rotate, scale, colour, origin, space) {
		this.transform = transform
		this.rotate = roatate
		this.scale = scale
		this.colour = colour
		this.origin = origin
		this.space = space
	}
}