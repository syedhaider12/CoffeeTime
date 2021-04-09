function validation() {
  var a = document.getElementById("fn").value;
  var b = document.getElementById("ln").value;
  var c = document.getElementById("em").value;
  var d = document.getElementById("ps1").value;
  var e = document.getElementById("ps2").value;
  var f = document.getElementById("us").value;
  if (a === "") {
    document.getElementById("fn").focus();
    alert("Enter your First Name");

    return false;
  }
  else if (b === "") {
    document.getElementById("ln").focus();
    alert("Enter your Last Name");
    return false;
  }
  else if (c === "") {
    document.getElementById("em").focus();
    alert("Enter your Email");
    return false;
  }
  else if (d === "") {
    document.getElementById("ps1").focus();
    alert("Enter your Pasword");
    return false;
  }
  else if (e === "") {
    document.getElementById("ps2").focus();
    alert("Re-Enter your Pasword");
    return false;
  }
  else if (f === "") {
    document.getElementById("us").focus();
    alert("Enter your User Name");
    return false;
  }

  else {
    return true;

  }


}


