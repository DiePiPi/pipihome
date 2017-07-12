function home(){
	window.location.assign("/");
	}

function iframeredir(dest){
	document.getElementById('iframe1').src = '/reservation-sys/' + dest + '/';
	}

function switch_lan(){
	if(getCookie('language') == 'en'){
		document.cookie = "language=ch";
	}else{
		document.cookie = "language=en";
	}
	location.reload();
}

function getCookie(cname) {
    var name = cname + "=";
	// decode cookie if it was encoded
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
var lan = getCookie('language');
