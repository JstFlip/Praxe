let particles = [];
let b1, b2;
const Y_AXIS = 1;
const X_AXIS = 2;
function setup() {
  frameRate(60);
  var canvas = createCanvas(window.innerWidth, window.innerHeight);
  canvas.parent("particleCanvas");
  /*setInterval(function() {
    canvas.clear();
  }, 1000 / 60);
  /*
  b2 = color("#000");
  b1 = color("#17022a");*/
  for (let i = 0; i < Math.floor(window.innerWidth / 14); i++) {
    particles.push(new Particle());
  }
}

function draw() {
  clear();
  //setGradient(0, 0, width, height, b2, b1, X_AXIS);
  //background("rgba(0,0,0,0.1)");
  particles.forEach((p, index) => {
    p.move();
    p.draw();
    p.checkParticles(particles.slice(index));
    //p.mouseCollision(particles);
  });
}

/*function setGradient(x, y, w, h, c1, c2, axis) {
  noFill();
  if (axis === Y_AXIS) {
    // Top to bottom gradient
    for (let i = y; i <= y + h; i++) {
      let inter = map(i, y, y + h, 0, 1);
      let c = lerpColor(c1, c2, inter);
      stroke(c);
      line(x, i, x + w, i);
    }
  } else if (axis === X_AXIS) {
    // Left to right gradient
    for (let i = x; i <= x + w; i++) {
      let inter = map(i, x, x + w, 0, 1);
      let c = lerpColor(c1, c2, inter);
      stroke(c);
      line(i, y, i, y + h);
    }
  }
}*/

class Particle {
  constructor() {
    this.position = createVector(
      random(window.innerWidth),
      random(window.innerHeight)
    );
    this.size = 10;
    this.velocity = createVector(random(-2, 2), random(-2, 2));
    this.color = "rgba(255,255,255,0.25)";
  }

  draw() {
    noStroke();
    fill(this.color);
    circle(this.position.x, this.position.y, this.size, this.size);
    this.detectEdges();
  }

  move() {
    this.position.add(this.velocity);
  }

  detectEdges() {
    if (this.position.x < 5 || this.position.x > window.innerWidth - 5) {
      this.velocity.x *= -1;
    }
    if (this.position.y < 5 || this.position.y > window.innerHeight - 5) {
      this.velocity.y *= -1;
    }
  }

  checkParticles(particles) {
    let opacity = 0.25;
    particles.forEach(particle => {
      const distance = dist(
        this.position.x,
        this.position.y,
        particle.position.x,
        particle.position.y
      );
      if (distance < 120) {
        stroke(`rgba(255,255,255,${opacity})`);
        line(
          this.position.x,
          this.position.y,
          particle.position.x,
          particle.position.y
        );
      }
    });
  }

  mouseCollision(particles) {
    var r1, r2, r3;
    r1 = Math.floor(random(0, 50));
    r2 = Math.floor(random(0, 150));
    r3 = Math.floor(random(0, 120));
    particles.forEach(() => {
      const d = dist(this.position.x, this.position.y, mouseX, mouseY);
      if (d < 100) {
        this.color = `rgb(${r1},${r2},${r3})`;
      } else {
        this.color = "rgba(255,255,255,0.25)";
      }
    });
  }
}
