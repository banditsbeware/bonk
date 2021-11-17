$('html').css('cursor', 'none')

var W = window.innerWidth
var H = window.innerHeight

var A, A0 = 20, k = 1/100, f = 3
var step = 5

var Mx = -1, My = -1

var canvas = $(`<canvas width=${W} height=${H}></canvas>`)
canvas.css({ 'position': 'absolute', 'top': '0', 'left': '0', 'z-index': '-1' })
$('body').append(canvas)

var ctx = canvas[0].getContext('2d')

ctx.strokeStyle = '#b7c3f3'
ctx.lineWidth = 1

let t, t0 = new Date()

function animate() {
  requestAnimationFrame(animate)

  ctx.clearRect(0, 0, W, H)

  if (Mx >=0 && My >= 0) {
    t = (new Date() - t0) / 1000

    A = A0 + (A0)*Math.sin(t)

    ctx.beginPath()
    ctx.ellipse(Mx, My, A, A, 0, 0, 2*Math.PI)
    ctx.moveTo(Mx, My)
    for (let x=Mx; x<=W; x += step) ctx.lineTo(x, My + (A * Math.sin(k*x - (t*f)) ))
    ctx.moveTo(Mx, My)
    for (let x=Mx; x>=0; x -= step) ctx.lineTo(x, My + (A * Math.sin(k*x - (t*f)) ))
    ctx.moveTo(Mx, My)
    for (let y=My; y<=H; y += step) ctx.lineTo(Mx + (A * Math.sin(k*y - (t*f)) ), y) 
    ctx.moveTo(Mx, My)
    for (let y=My; y>=0; y -= step) ctx.lineTo(Mx + (A * Math.sin(k*y - (t*f)) ), y) 
    ctx.stroke()
  }
}

animate()

$(window).on('mousemove', (e) => { Mx = e.clientX; My = e.clientY; })
$(window).on('mouseleave', () => { Mx = -1, My = -1 })