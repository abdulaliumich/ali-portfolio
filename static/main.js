
//add blue outline to login buttons when you hover over them
function signInMouseOver (loginId) {
	if (loginId == "bigSignInButton") {
		document.getElementById(loginId).src="static/signin/btn_google_signin_light_focus_web.png";
	}
	else if (loginId == "smallSignInButton") {
		document.getElementById(loginId).src="static/signin/btn_google_light_normal_ios.png";
	}
	else {
		console.log("invalid argument");
	}
}

//remove blue outline from login buttons when you hover over them
function signInMouseOut (loginId) {
	if (loginId == "bigSignInButton") {
		document.getElementById(loginId).src="static/signin/btn_google_signin_light_normal_web.png";
	}
	else if (loginId == "smallSignInButton") {
		document.getElementById(loginId).src="static/signin/btn_google_light_focus_ios.png";
	}
	else {
		console.log("invalid argument");
	}
}

//add shadow to login buttons when you mouse down over them
function signInMouseDown (loginId) {
	if (loginId == "bigSignInButton") {
		document.getElementById(loginId).src="static/signin/btn_google_signin_light_pressed_web.png";
	}
	else if (loginId == "smallSignInButton") {
		document.getElementById(loginId).src="static/signin/btn_google_light_pressed_ios.png";
	}
	else {
		console.log("invalid argument");
	}
}

function loginButton(loginId, logoutId, loggedIn) {
	if (loggedIn) {
		document.getElementById(loginId).style.display = "none";
	}
	else {
		document.getElementById(logoutId).style.display = "none";
	}
}