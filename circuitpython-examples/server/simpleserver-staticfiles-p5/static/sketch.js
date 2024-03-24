let accel = {x: 0, y: 0, z: 0};

function setup(){
	createCanvas(500, 500)
	//JS timer
	setInterval(getAccel, 1000)
}

function draw(){
	background(255, 0, 0)
	fill(0)
	const x = map(accel.x, -1, 1, 0, width)
	circle(x, width/2, 50)
}


//asynchrounous get request
async function getAccel() {
	
	try {
	    const response = await window.fetch("/ajax/get_accel", {
	        method: "GET",
	        headers: {
	            'Content-Type': 'application/json; charset=utf-8',
	        },
	    })
		
		accel = await response.json()
		
		//update div 
		document.getElementById("accel").innerHTML = JSON.stringify(accel)
	    
	} catch(error) {
		console.log("error!: " + error)
	}
    
}
