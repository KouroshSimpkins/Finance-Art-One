/* jshint esversion:6 */

function preload() {
  Prices = loadTable('Stock_Prices.csv', 'csv', 'header');
}

function setup() {
  createCanvas(1000, 1000);
  frameRate(1);
  colorMode(HSB);
  // Hue should be either 120 (green) or 0-10 (red)
  // Brightness shouldn't go lower than 15? This will keep the colours consistent.
  // Saturation stays at the highest value (100?)
  /*readTextFile("http://127.0.0.1:5500/Stock_Prices.txt");*/
}

function draw() {
  strokeWeight(1);
  background(255);
  pointDraw(0,0);
}

function readTextFile(file) {
  fetch(file)
    .then(response => response.text())
    .then(data => {
      console.log(data);
    });
}

// pointDraw function will draw the pixels one by one for the output.
function pointDraw(StartX, StartY) {
  for (let x = StartX; x <= width; x++) {
    for (let y = StartY; y <= height; y++) {
      stroke(120, 100, random(25,100));
      point(x, y);
    }
  }
}