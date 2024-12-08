  // Draw a circle in the center with
  // a width of 100.
  circle(200, 200, 100);

function setup() {
  createCanvas(400, 400);
   background("papayawhip");
}
function draw() {
  //when mouse button is pressed, circles turn black
  if (mouseIsPressed === true) {
    fill("aqua");
  } else {
    fill("s55");
  }

  //white circles drawn at mouse position
  circle(mouseX, mouseY, 100);
}
