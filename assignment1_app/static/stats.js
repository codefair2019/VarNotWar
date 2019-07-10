function myFunction () {

  document.body.style.overflowY = 'hidden'
  document.querySelector('#myModal').style.opacity = '1'
  document.querySelector('.sticky-top').style.opacity = '0'
  setTimeout(() => {
    window.location.href = './abs'
  }, 3000)
}

// function refresh () {
//   setTimeout(() => {
//     document.querySelector('#myModal').style.opacity = '1'
//     document.querySelector('.sticky-top').style.opacity = '0'
//   }, 200)
// }

//   console.log('worked')
//   document.body.style.overflowY = 'hidden'
//   document.querySelector('.sticky-top').style.opacity = '0'
//   document.querySelector('#myModal').style.opacity = '1'
// }

// function load () {
//   setTimeout(() => {
//     document.querySelector('#myModal').style.opacity = '0'
//     document.querySelector('.sticky-top').style.opacity = '1'
//   }, 3000)
// }
