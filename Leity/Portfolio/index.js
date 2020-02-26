//Sticky NavBar #Header#//
let header = document.getElementById("header");
let mobileHeader = document.getElementById("mobile-header");
let pointer = document.querySelector(".pointer");
let offset = header.offsetTop;
let width = window.innerWidth;

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
    pointer.style.opacity = "0";
  } else {
    header.classList.remove("scrolled");
    mobileHeader.classList.remove("scrolled");
    pointer.style.opacity = "1";
  }
}
window.addEventListener("scroll", ScrolledNav);

//AOS//
AOS.init({});

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

(function() {
  const options = {
    threshold: [0.5]
  };
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.intersectionRatio >= 0.5) {
        setCurrent(entry.target);
      }
    });
  }, options);

  const setCurrent = section => {
    document.querySelectorAll(".active").forEach(el => el.classList.remove("active"));
    section.classList.add("active");
    document.querySelector(`.nav li a[href="#${section.id}"]`).classList.add("active");
  };
  const sections = document.querySelectorAll("section");
  sections.forEach(section => observer.observe(section));
})();
