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
<!DOCTYPE html>
<html>
  <head>
    <meta name = "viewpoint", content = "width=device-width, initial-scale= 1.0 maximum-scale = 1.0, user-scalable = no">
    <style type = "text/css">
      .inner {
        width : 1170px;
        margin : auto;
        border : 1px solid red;
      }
      .col {
        width : 23%; margin : 1%;
        text-align : center;
        background : olive; float : left;
      }
      .col img{
        width : 100%;
      }
      .clear {
        clear : both;
      }
      @media only screen and (min-width : 568px) and (max-width : 992px ) {
        .inner {
          width : 100%;
        }
      .col {
        width : 23%; margin : 1%;
      }
      @media only screen and (min-width : 200px) and (max-width : 567px ) {
        .inner {
          width : 100%;
        }
      /*.col {
        width : 48%; margin : 1%; */
      }
    </style>
  </head>
  <body>
    <div class = "inner">
      <div class = "col">
        <img src = ".jpg"/>
        <h5> Demo </h5>
      </div>
      <div class = "col">
        <img src = ".jpg"/>
        <h5> Demo </h5>
      </div>
      <div class = "col">
        <img src = ".jpg"/>
        <h5> Demo </h5>
      </div>
      <div class = "col">
        <img src = ".jpg"/>
        <h5> Demo </h5>
      </div>
      <div class = "clear"></div>
    </div>
  </body>
</html>
