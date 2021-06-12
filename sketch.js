/* jshint esversion:6 */

function preload() {
  Prices = loadTable('Stock_Prices.csv', 'csv', 'header');
}

function setup() {
  size = (round(sqrt(Prices.getRowCount()))+1);
  createCanvas(size, size);
  frameRate(0.1);
  colorMode(HSB);
  noLoop();
  // Hue should be either 120 (green) or 10 (red)
  // Brightness shouldn't go lower than 15? This will keep the colours consistent.
  // Saturation stays at the highest value (100?)
}

function draw() {
  strokeWeight(1);
  background(255);
  pointDraw(0,0);
}

// pointDraw function will draw the pixels one by one for the output.
function pointDraw(StartX, StartY) {
  let SN = 0;
  let Hue = 235;
  for (let x = StartX; x <= width; x++) {
    for (let y = StartY; y <= height; y++) {
      let isup = Prices.getString(SN, "isup");
      if (isup == "True") {
        Hue = 120;
      } else {
        Hue = 10;
      }
      
      let Bright = map(Prices.getNum(SN, "Close"), Prices.getNum(SN, "High"), Prices.getNum(SN, "Low"), 15, 100);

      SN += 1;
      stroke(Hue, 100, Bright);
      point(x, y);
    }
  }
}