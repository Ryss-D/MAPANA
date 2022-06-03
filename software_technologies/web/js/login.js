function validate(){
var username = document.getElementByName("username").value;
var password = document.getElementByName("password").value;
var token = document.getElementByName("token")
if ( username == "mapana" && password == "123" && token == "123456"){
alert ("Login successfully");
return false;
}
else{
alert ("Wrong credentials")
return false;

}
}

document.querySelector("#loginForm").addEventListener("click", function(e){
	e.preventDefault();
	login();
});