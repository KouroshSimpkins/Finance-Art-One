/* jshint esversion:6 */

function setup() {
  createCanvas(400, 400);
  colorMode(HSB);
  readTextFile("http://127.0.0.1:5500/Stock_Prices.txt");
}

function draw() {
  strokeWeight(1);
  background(220);
  fill(255, 0, 0);
  stroke(255, 0, 0);
  point(0,0);
  point(1,1);
  stroke(0, 255, 0);
  point(0,1);
  point(1,0);
}

function readTextFile(file) {
  fetch(file)
    .then(response => response.text())
    .then(jsonResponse => console.log(jsonResponse));
}