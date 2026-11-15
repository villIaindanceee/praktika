var burger = document.getElementById('burger');
var nav = document.getElementById('nav');

burger.addEventListener('click', function () {
  nav.classList.toggle('otkr');
});

nav.querySelectorAll('a').forEach(function (a) {
  a.addEventListener('click', function () {
    nav.classList.remove('otkr');
  });
});