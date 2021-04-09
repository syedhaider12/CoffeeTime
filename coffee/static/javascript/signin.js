function validation(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
   
    if (email === ""){
      document.getElementById("email").focus();
      alert("Enter your Email");
      return false;
    }
    else if (password === ""){
      document.getElementById("Password").focus();
      alert("Enter your password");
      return false;
    }
    else{
      return true;
    }
  }