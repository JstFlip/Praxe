//AOS//
AOS.init();

//Sticky NavBar #Header#//
let header = document.getElementById("header");
let mobileHeader = document.getElementById("mobile-header");
let offset = header.offsetTop;
let width;

function windowResize() {
  width = window.innerWidth;
}
window.addEventListener("resize", windowResize);

function ScrolledNav() {
  if (window.pageYOffset > offset) {
    if (width <= 900) {
      mobileHeader.classList.add("scrolled");
    } else {
      header.classList.add("scrolled");
    }
  } else {
    header.classList.remove("scrolled");
    mobileHeader.classList.remove("scrolled");
  }
}
window.addEventListener("scroll", ScrolledNav);
