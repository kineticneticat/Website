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

function cookie_accept() {
    document.cookie = 'cookies_accepted=True'
    document.getElementById('cookie-div').className = 'popdown'
}

window.onload = function() {
  
  if (getCookie('cookies_accepted') == '') {
    document.getElementById('cookie-div').className = 'popup'
  } else {
    document.getElementById('cookie-div').className = 'popdown'
  }
};