//Sticky NavBar//
let header = document.getElementById("header");
let mobileHeader = document.getElementById("mobile-header");
let pointer = document.getElementsByClassName("pointer");
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
    pointer[0].style.opacity = "0";
  } else {
    header.classList.remove("scrolled");
    mobileHeader.classList.remove("scrolled");
    pointer[0].style.opacity = "1";
  }
}
window.addEventListener("scroll", ScrolledNav);

//AOS//
AOS.init({});

//Swiper Projects//
var Swiper = new Swiper(".swiper-container", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 25,
    stretch: 0,
    depth: 50,
    modifier: 1,
    slideShadows: true
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev"
  }
});
