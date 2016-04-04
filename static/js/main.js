
//add blue outline to login buttons when you hover over them
function signInMouseOver (loginId) {
	if (loginId == "bigSignInButton") {
		document.getElementById(loginId).src="static/imgs/signin/btn_google_signin_dark_focus_web.png";
	}
	else if (loginId == "smallSignInButton") {
		document.getElementById(loginId).src="static/imgs/signin/btn_google_light_focus_ios.png";
	}
	else {
		console.log("invalid argument");
	}
}

//remove blue outline from login buttons when you hover over them
function signInMouseOut (loginId) {
	if (loginId == "bigSignInButton") {
		document.getElementById(loginId).src="static/imgs/signin/btn_google_signin_dark_normal_web.png";
	}
	else if (loginId == "smallSignInButton") {
		document.getElementById(loginId).src="static/imgs/signin/btn_google_light_normal_ios.png";
	}
	else {
		console.log("invalid argument");
	}
}

//add shadow to login buttons when you mouse down over them
function signInMouseDown (loginId) {
	if (loginId == "bigSignInButton") {
		document.getElementById(loginId).src="static/imgs/signin/btn_google_signin_dark_pressed_web.png";
	}
	else if (loginId == "smallSignInButton") {
		document.getElementById(loginId).src="static/imgs/signin/btn_google_light_pressed_ios.png";
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
};

//jQuery stuff

//When the page loads
$( document ).ready(function() {
	console.log("Hello!");
	//Change navbar from nav-pills to nav-navbar based on the screen size of the device
    if ($(window).width() < 768) {
    	$('#my-navbar').removeClass('nav-pills').addClass('navbar-nav');
    }
});

//change nav class when a user resizes the screen
$(window).on('resize', function(){
      var win = $(this);
      if (win.width() >= 768) {
      	$('#my-navbar').removeClass('navbar-nav').addClass('nav-pills');
      }
      else {
      	$('#my-navbar').removeClass('nav-pills').addClass('navbar-nav');
      }
});