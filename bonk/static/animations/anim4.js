var W = window.innerWidth, H = window.innerHeight

var mouse = { x: -1, y: -1 }
$(window).on('mousemove', (e) => { mouse.x = e.clientX; mouse.y = e.clientY; })
$(window).on('mouseleave', () => { mouse.x = -1, mouse.y = -1 })

var ctx, canvas = $(`<canvas width=${W} height=${H}></canvas>`)
canvas.css({ 'position': 'absolute', 'top': '0', 'left': '0', 'z-index': '-1' })

$('body').append(canvas)
ctx = canvas[0].getContext('2d')

const randInt = (l, h) => Math.floor( l + Math.random() * (h - l) )

ctx.strokeStyle = '#b7c3f3'
ctx.fillStyle = 'rgba(183, 195, 243, 0.4)'
ctx.lineWidth = 1

class point {
  constructor(x, y, z) {
    this.x = x, this.y = y, this.z = z
  }
  proj(D) {
    let sf = D / (D - this.z)
    return new point(this.x * sf, this.y * sf, 0)
  }
}

const res = 50, depth = 2000
const D = 1000

function p(x, y, z) {
  let sf = D / (D - z)
  // return [ x * sf + W/2, H + ( z * (H/2 - y) / (D - z)) ]
  return [ W/2 + x * sf, H - y * sf ]
}

ctx.beginPath()
ctx.moveTo(...p(-W/2, 0, 0))
ctx.lineTo(...p(-W/2, 100, -depth))
ctx.lineTo(...p(W/2, 100, -depth))
ctx.lineTo(...p(W/2, 0, 0))
ctx.closePath()
ctx.stroke()

// ctx.beginPath()
// ctx.moveTo(...p(-W/2, 0, 0))
// for (let z=0; z > -depth; z--) {
//   ctx.lineTo(...p(-W/2, 1000*Math.sin(z/100), z))
// }
// ctx.stroke()

// ctx.beginPath()
// ctx.moveTo(...p(-W/2, 0, -depth))
// for (let x=-W/2; x < W/2; x++) {
//   ctx.lineTo(...p(x, 1000*Math.sin(x/100), -depth))
// }
// ctx.stroke()

function animate() {
  requestAnimationFrame(animate)
  ctx.clearRect(0, 0, W, H)

}

// animate()