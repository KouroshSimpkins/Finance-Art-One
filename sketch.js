function setup() {
  createCanvas(400, 400);
  readTextFile("file://Stock_Prices.txt");
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
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", file, false);
  rawFile.onreadystatechange = function() 
  {
    if(rawFile.readyState === 4)
    {
      if(rawFile.readyState === 200 || rawFile.status == 0)
      {
        var allText = rawFile.responseText;
        alert(allText);
      }
    }
  };
  rawFile.send(null);
}