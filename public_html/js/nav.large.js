window.onload = window.onresize = function () {
	var width = window.innerWidth  || document.documentElement.clientWidth || document.body.clientWidth;
	var nav = document.getElementById("nav");
	var right = document.getElementById("right");
	var body = document.getElementById("corpo").offsetHeight;
	if (width>769) {
	    if (nav.offsetHeight < body) {
	        nav.style.height = body+"px";
	        if (right.offsetHeight < body) {
	        	right.style.height=nav.offsetHeight+"px";
	        }
	    } 	
	    if (right.offsetHeight < body) {
	        	right.style.height=nav.offsetHeight+"px";
		}
		else if (nav.offsetHeight < right.offsetHeight) {
	    	nav.style.height = right.offsetHeight+"px";
	    }
	} else {
		nav.style.height=100+"%";
	}
};
