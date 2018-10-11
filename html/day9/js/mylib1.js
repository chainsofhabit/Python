function $(id){
	return document.getElementById(id);
}

function bind(elem,en,fn){
	if(elem.addEventListener){
		elem.addEventListener(en,fn);
	}else{
		elem.attachEvent("on" + en,fn);
	}
	
}

function unbind(elem,en,fn){
	
	if(elem.removeEventListener){
		elem.removeEventListener(en,fn);
	}else{
		elem.detachEvent("on" + en,fn);
	}
}


function randomColor(){
	var red = parseInt(Math.random()*256);
	var green = parseInt(Math.random()*256);
	var blue = parseInt(Math.random()*256);
	return "rgb(" + red + "," + green + "," + blue +")";
};