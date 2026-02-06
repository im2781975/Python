<!DOCTYPE html>
<html>
  <head></head>
  <body>
      <button onclick = "task()"> Click </button>
      <h6 id = 'res'></h6>
      <input type = "" name = "" id = "num"/>
      <button onclick = "text()"> Press </button>
      <h2 id = 'ans'></h2>
  </body>
  <script type = "text/javascript">
    function task() {
      try {
        // alertf("YoBro");
        var val = "ws"; // 9 | ws
        var x = val.toUpperCase();
        document.getElementById('res').innerText = x;
      }
      catch(err) {
        document.getElementById('res').innerText = err
      }
    }
    var num = document.getElementById('num');
    function text() {
      var val = num.value;
      // alert(val);
      try {
        if(isNaN(val)) {
          throw "this isn't a number";
        }
        else {
          if(val < 5 || val > 10) {
            throw "OutOfBound";
          }
          else {
            throw "";
          }
        }
      }
      catch(ERM) {
        document.getElementById("ans").innerText = ERM;
      }
      finally {
        num.value = "";
      }
    }
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head>
    <style type = "text/css">
      .red {
        color : red;
      }
      .blue {
        color : blue;
      }
    </style>
  </head>
  <body>
    <div id = "idx" class = "red"> Hello </div>
    <button onclick = "func()"> click </button>
    <h1 id = "res"></h1>
  </body>
  <script type = "text/javascript">
    var x = document.getElementById('idx');
    function func(){
      var cls = x.getAttribute("class");
      // document.getElementById('res').innerText = cls;
      if(cls === "red") x.setAttribute("class", "blue");
      else x.setAttribute("class", "red");
    }
  </script>
</html>
<!DOCTYPE html>
<html>
  <head></head>
  <body><h1>Regular Expression</h1></body>
  <script type = "text/javascript">
    var pattern = /[a-z]+[0-9]+/ig;
    var ing = "WsCube1234Teach";
    document.write(pattern.exec(ing));
    document.write(pattern.test(ing));
    var pat = new RegExp("[a-z][0-9]", "i");
    document.write(pat.toString());
  </script>
</html>
