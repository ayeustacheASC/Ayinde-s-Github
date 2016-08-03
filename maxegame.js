function setup(){
	createCanvas(600,600);
	background(0);
}
ballX=26
ballY=36
function levelOne(){
	fill(255,204,0);
	noStroke();
	background(0);
	ellipse(ballX,ballY,35,35);
	fill(255);
	noStroke();
	rect(0,53.5,450,50);
	fill(255);
	noStroke();
	rect(150,157,450,50);
	fill(255);
	noStroke();
	rect(0,264,450,50);
	fill(255);
	noStroke();
	rect(150,371,450,50);
	fill(255);
	noStroke();
	rect(0,478,450,50);
	fill(255,0,0)
	noStroke();
	rect(0,550,100,100)
	if (keyIsDown(LEFT_ARROW)){
    	ballX -= 8;
	}

    if(keyIsDown(RIGHT_ARROW)) {
        ballX += 8;
    }

    if(keyIsDown(DOWN_ARROW)){
        ballY +=8;
    }

    if(keyIsDown(UP_ARROW)){
        ballY -= 8; 
    }

    if (ballX <= 18.5){
        ballX+= 8;
    }
    
    if (ballX >= 581.5){
        ballX -= 8; 
    }

    if(ballY <= 10){
        ballY += 8;
    }

    if(ballY >= 585){
        ballY -= 8;
    }

 	if (ballX >= 0 && ballY <= 467.5) && (ballY >= 38 && ballY <= 118));
	ballx= 36;
	ballY= 26;
	ellipse(ballx,ballY, 35,35)

}
	if(ballx >= 132.5 && ballx <=58.3) && (ballY >= )

function draw(){
	levelOne()
}







	