window.addEventListener("scroll", HeaderScrl);
let header = document.getElementById("header");
let subheader = document.getElementById("subheader");
let section = document.getElementById("sec1");
let scrld = header.offsetTop;
let width = window.innerWidth;
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

/*
$(function() {
  $.scrollify({
    section: "section"
  });
});*/
