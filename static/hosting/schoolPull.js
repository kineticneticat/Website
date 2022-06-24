function Setup() {
  buttons = [
    document.createElement('button'),
    document.createElement('button'),
    document.createElement('button'),
    document.createElement('button'),
    document.createElement('button')
  ]
  buttons[0].setAttribute('onclick', 'name()')
  buttons[1].setAttribute('onclick', 'ht()')
  buttons[2].setAttribute('onclick', 'email()')
  buttons[3].setAttribute('onclick', 'phone()')
  buttons[4].setAttribute('onclick', 'address()')
  for (let i = 0; i < buttons.length; i++) {
    console.log(buttons[i])
  }
}