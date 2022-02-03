import * as THREE from 'https://cdn.skypack.dev/three@0.135.0/build/three.module.js'
import { OrbitControls } from 'https://cdn.skypack.dev/three@0.135.0/examples/jsm/controls/OrbitControls'
import Stats from 'https://cdn.skypack.dev/three@0.135.0/examples/jsm/libs/stats.module.js'

const scene = new THREE.Scene()
scene.add(new THREE.AxesHelper(5))

const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
)
camera.position.z = 2

const renderer = new THREE.WebGLRenderer()

renderer.setSize(window.innerWidth, window.innerHeight)
document.body.appendChild(renderer.domElement)

const controls = new OrbitControls(camera, renderer.domElement)

controls.listenToKeyEvents(document.body)

var geometry = new THREE.BoxGeometry()
var material = new THREE.MeshBasicMaterial({
    color: 0x00ff00,
    wireframe: true,
})

var cube = new THREE.Mesh(geometry, material)
scene.add(cube)

geometry = new THREE.PlaneGeometry( 1, 1 );
material = new THREE.MeshBasicMaterial( {color: 0xffff00, side: THREE.DoubleSide} );
var plane = new THREE.Mesh( geometry, material );
scene.add( plane );

geometry = new THREE.TorusKnotGeometry( 10, 3, 100, 16 );
material = new THREE.MeshBasicMaterial( { color: 0xffff00, side: THREE.DoubleSide} );
var torusKnot = new THREE.Mesh( geometry, material );
scene.add( torusKnot );

geometry = new THREE.TorusKnotGeometry( 10, 3, 100, 16 );
material = new THREE.MeshBasicMaterial( { color: 0x0000ff, wireframe: true } );
torusKnot = new THREE.Mesh( geometry, material );
scene.add( torusKnot );

window.addEventListener('resize', onWindowResize, false)
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
    render()
}

const stats = Stats()
document.body.appendChild(stats.dom)

function animate() {
    requestAnimationFrame(animate)

    // controls.update()

    render()

    stats.update()
}

function render() {
    renderer.render(scene, camera)
}

animate()