//AOS//
AOS.init();
/*
window.addEventListener("scroll", HeaderScrl);
window.addEventListener("resize", BrowerResized);
let header = document.getElementById("header");
let subheader = document.getElementById("subheader");
let section = document.getElementById("sec1");
let scrld = header.offsetTop;
let width;

function HeaderScrl() {
  if (window.pageYOffset > scrld) {
    if (width >= 811) {
      header.classList.add("scrolled");
      section.classList.remove("higherheight");
      section.classList.add("lowerheight");
    } else {
      header.classList.add("scrolled");
      subheader.classList.add("scrolled-sub");
      section.classList.remove("higherheight");
      section.classList.add("lowerheight");
    }
  } else {
    header.classList.remove("scrolled");
    subheader.classList.remove("scrolled-sub");
    section.classList.remove("lowerheight");
    section.classList.add("higherheight");
  }
}
function BrowerResized() {
  width = window.innerWidth;
}*/

window.addEventListener("scroll", ScrolledNav);
let header = document.getElementById("header");
let offset = header.offsetTop;

function ScrolledNav() {
  if (window.pageYOffset > offset) {
    header.classList.add("scrolled");
  } else {
    header.classList.remove("scrolled");
  }
}
