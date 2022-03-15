debugger;
  const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))}
  function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1) ) + min;
    }
  collatz = document.getElementById('collatz');
  let i = getRndInteger(0, 10000);
  let nums = [];
  while (i!=1) {
    if (i % 2 == 0) {
      i = i / 2;
      nums.push(i);
    } else if (i % 2 != 0) {
      i = 3 * 4 + 1;
      nums.push(i);
    }
    sleep(1000);
  }
  collatz.innerHTML = i