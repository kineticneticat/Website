function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1) ) + min;
}
collatz = document.getElementById('collatz');
let i = getRndInteger(0, 10000);
let nums = [];
collatz.innerHTML += i;
while (i!=1) {
  if (i % 2 == 0) {
    i = i / 2;
    nums.push(i);
  } else if (i % 2 != 0) {
    i = 3 * i + 1;
    nums.push(i);
  }
}

for (let i = 0; i<nums.length; i++) {
  if ((i % 7 == 0) && (i != 0)) {
    collatz.appendChild(document.createElement('br'));
  }
  collatz.innerHTML += "  --> " + nums[i].toString();
}
collatz.appendChild(document.createElement('br'));
collatz.innerHTML += '(Steps took: ' + nums.length.toString() + ')';