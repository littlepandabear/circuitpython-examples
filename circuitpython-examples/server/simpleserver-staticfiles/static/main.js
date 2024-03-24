let accel;
let temp;

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

async function getTemp() {
	
	try {
	    const response = await window.fetch("/ajax/get_temp", {
	        method: "GET",
	        headers: {
	            'Content-Type': 'application/json; charset=utf-8',
	        },
	    })
		
		temp = await response.text()
		
		//update div 
		document.getElementById("temp").innerHTML = JSON.stringify(temp)
	    
	} catch(error) {
		console.log("error!: " + error)
	}
    
}

 getTemp()

//JS timer
setInterval(getAccel, 1000)

