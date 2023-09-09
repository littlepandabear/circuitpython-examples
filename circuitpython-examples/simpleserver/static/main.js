let accel;

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

//JS timer
setInterval(getAccel, 1000)

