// general canvas functions // setup for animations //

var W = window.innerWidth, H = window.innerHeight

var mouse = { x: -1, y: -1 }
$(window).on('mousemove', (e) => { mouse.x = e.clientX; mouse.y = e.clientY; })
$(window).on('mouseleave', () => { mouse.x = -1, mouse.y = -1 })

var ctx, canvas = $(`<canvas width=${W} height=${H}></canvas>`)
canvas.css({ 'position': 'absolute', 'top': '0', 'left': '0', 'z-index': '-1' })

$(document).ready( function() {
  $('body').append(canvas)
  ctx = canvas[0].getContext('2d')
})

const randInt = (l, h) => Math.floor( l + Math.random() * (h - l) )
