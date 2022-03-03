//change name
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
let is_logged_in = getCookie('Logged_In')
let username = getCookie('userID')
if (is_logged_in = 'True') {
	document.getElementById("login").textContent=username;
}

function changeMode() {
  alert(1)
}

document.getElementById('main').onclick => {
  alert('clicked')
}