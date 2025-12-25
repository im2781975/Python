<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <script type = "text/javascript">
      // alert("Error")
      // console.log("Gama Tech")
      // document.write("<h1> Hello </h1>")
      // document.write("<h1> EveryOne! </h1>")
      prompt("Enter sentence", "")
      confirm("Do You want to login?")
      var name = "wscube"; document.write(name)
    </script>
  </body>
</html>
<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <div id = "main"> 
      <h1> PISQR </h1>
    </div>
    <h1> 1 </h1>
    <div class = "base"> PHARMACY </div>
    <h1> 2 </h1>
    <div class = "base"> THYSQR </div>
  </body>
  <script type = "text/javascript">
    // var x = documet.getElementById("main").innerHTML
    // console.log(x)
    // document.getElementById("main").innerHTML = "<h1>PISQRE</h1>";
    var x = document.getElementsByClassName("base")[0].innerHTML;
    var x = document.getElementsByClassName("base")[1].innerHTML;
    var x = document.getElementsByClassName("base")[1].innerHTML = "PHARMA"
    // alert(x)
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <h1 id="res" style = "margin : 50px auto; width : 250px"></h1>
  </body>
  <script type = "text/javascript">
    var x = "Even"
    var y = "Odd"
    document.write(x + " " + y + " zero ")
    //alert(x + " " + y + " zero")
    document.write(3 + 3)
    var a = 5;
    var b = 7;
    var a += b;
    document.getElementById('res').innerHTML = a * b;
    document.getElementById('res').innerHTML = ++a;
    document.getElementById('res').innerHTML = a == b;
    document.getElementById('res').innerHTML = a >= b;
    document.getElementById('res').innerHTML = x > y ? "yes" : "no";
    var x = 0;
    var y = true;
    document.getElementById('res').innerHTML = x && y;
    document.getElementById('res').innerHTML = x || y;
  </script>
</html>
