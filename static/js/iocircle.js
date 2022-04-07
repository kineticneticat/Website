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

    //console.log(new Date('April 17, 2022, 00:00:00 UTC') - new Date());
    ms = new Date('April 17, 2022, 00:00:00 UTC') - new Date();
    let month = 'apr';
    var canvas = document.getElementById("iocircle");
    var ctx = canvas.getContext("2d");
    
    ctx.clearRect(0, 0, 1000, 1000);
    ctx.strokeStyle = "white";

    fullDays = Math.floor((((ms/1000)/60)/60)/24)
    fullHours = Math.floor(((ms/1000)/60)/60)
    fullMinutes = Math.floor((ms/1000)/60)
    fullSeconds = Math.floor(ms/1000)
  
    finalDays = fullDays
    finalHours = fullHours - fullDays * 24
    finalMinutes = fullMinutes - fullHours * 60
    finalSeconds = fullSeconds - fullMinutes * 60


  
  // debugger;
  //seconds
    ctx.fillStyle = '#23232e';
    console.log(finalSeconds)
    for (let index = 0; index < 60; index++) {
        if (index % finalSeconds == 0) {
          continue
        }
        let angle = (index * 6) * (Math.PI / 180);
        ctx.beginPath();
        ctx.arc(Math.sin(angle)*110+499, Math.cos(angle)*110+499, 3, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
    }

  // debugger;
  //minuits
    ctx.fillStyle = 'white';
    for (let index = 0; index < 60; index++) {
        if (index % finalMinutes == 0) {
          continue
        }
        let angle = (index * 6) * (Math.PI / 180);
        ctx.beginPath();
        ctx.arc(Math.sin(angle)*160+499, Math.cos(angle)*160+499, 3, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
    }

  // debugger;
  //hours
    ctx.fillStyle = '#23232e';
    for (let index = 0; index < 24; index++) {
        if (index % finalHours == 0) {
          continue
        }
        let angle = (index * (360/24)) * (Math.PI / 180);
        ctx.beginPath();
        ctx.arc(Math.sin(angle)*210+499, Math.cos(angle)*210+499, 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
    }

  // debugger;
  //days
    ctx.fillStyle = 'white';
    if (['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec'].includes(month)) {
      amt = 31;
      θ = 360/31;
    } else if (['apr', 'jun', 'sep', 'nov'].includes(month)) {
      amt = 30;
      θ = 360/30;
    } else if (month == 'feb') {
      amt = 28;
      θ = 360/28;
    }
    
    for (let index = 0; index < amt; index++) {
        if (index % finalDays == 0) {
          continue
        }
        let angle = (index * θ) * (Math.PI / 180);
        ctx.beginPath();
        ctx.arc(Math.sin(angle)*260+499, Math.cos(angle)*260+499, 10, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
    }

  requestAnimationFrame(loop);
}