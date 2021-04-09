function validation(){
    var user = document.getElementById("user").value;
    var email = document.getElementById("email").value;
    var text = document.getElementById("text").value;
  
    if( user === ""){
      document.getElementById("user").focus();
      alert("Enter your Name");
      return false;
    }
    else if (email === ""){
      document.getElementById("email").focus();
      alert("Enter your Email");
      return false;
    }
  
    else if (text === ""){
      document.getElementById("text").focus();
      alert("Enter your Query");
      return false;
    }
    else{
      return true;
    }
  
  }