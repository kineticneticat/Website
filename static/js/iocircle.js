function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
window.onload = startup;

function startup() {
  loop();
}

function loop() {
  go();
  requestAnimationFrame(loop);
}

async function go(){
    // debugger;
  
  
  var canvas = document.getElementById("iocircle");
  var ctx = canvas.getContext("2d");
  
  ctx.clearRect(0, 0, 1000, 1000);
    let list = [...Array(22).keys()];
    for (let index = 0; index < list.length; index++) {
      if (index % 2 == 0) {
        continue
      }
        let angle = index * 6;
        ctx.beginPath();
        ctx.arc(Math.sin(angle)*60+499, Math.cos(angle)*60+499, 5, 0, 2 * Math.PI);
        ctx.stroke();
    }


  await sleep(100)
  requestAnimationFrame(loop);
}