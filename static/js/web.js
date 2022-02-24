    let margin = 100
    function getRndInteger(min, max) {
      return Math.floor(Math.random() * (max - min + 1) ) + min;
    function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
    }
    const ballPositions = [
      //[x, y, vx, vy]
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0], 
      [0, 0, 0, 0],
      [0, 0, 0, 0], 
      [0, 0, 0, 0], 
      [0, 0, 0, 0],
      [0, 0, 0, 0], 
      [0, 0, 0, 0], 
      [0, 0, 0, 0], 
      [0, 0, 0, 0]
    ]
    for (i in ballPositions) {
      ballPositions[i][0] = getRndInteger(0, window.innerWidth - margin);
      ballPositions[i][1] = getRndInteger(0, 1000 - margin);
      ballPositions[i][2] = getRndInteger(-1, 1);
      ballPositions[i][3] = getRndInteger(-1, 1);
    }
    window.onload = startup;

    function startup() {

      for (let ball of ballPositions) {
        console.log(ball);
      }
      var canvas = document.getElementById("metaballCanvas");
      var ctx = canvas.getContext("2d");
      loop(ballPositions);
    }

    //use `requestAnimationFrame` for the game loop
    //so you stay sync with the browsers rendering
    //makes it a smoother animation
    
    function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
    async function loop(ballPositions){
      
      
      
      var canvas = document.getElementById("metaballCanvas");
      var ctx = canvas.getContext("2d");
      
      ctx.clearRect(0, 0, 1000, 1000);
      
      for (let ball = 0; ball < ballPositions.length; ball++) {

      
        ctx.beginPath();
        ctx.arc(ballPositions[ball][0], ballPositions[ball][1], 5, 0, 2 * Math.PI);
        ball[0] += 69;
        ctx.fillStyle = "white";
        ctx.fill();
        ctx.lineWidth = 0;
        ctx.strokeStyle = "white";
        ctx.stroke();
        if (ballPositions[ball] == ballPositions[ballPositions.length-1]) {
          break;
        }
      } 
      debugger;
      for (ball=0;ball<ballPositions.length;ball++) {
        ballPositions[ball][0] += ballPositions[ball][2]
        ballPositions[ball][1] += ballPositions[ball][3]
      }
      await sleep(100)
      requestAnimationFrame(loop);
    }