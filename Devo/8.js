<!DOCTYPE HTML>
<html>
  <head>
    <style type = "text/css">
      div{
        border-bottom: 1px solid black;
        width : 100px;
        font-family : verdana;
      }
    </style>
    <script type = "text/javascript">
      var num = prompt("Enter name","");
      for(var i = 1; i <= 10; i++) {
        document.write("<div>");
        document.write(i + " x " + num + " = " + i * num);
        document.write("</div>");
      }
    </script>
  </head>
  <body></body>
</html>
<!DOCTYPE HTML>
<html>
  <head>
  </head>
  <body></body>
  <script type = "text/javascript">
    var row = prompt("Enter rows");
    pattern(row);
    function pattern(row) {
      for(var i = 1; i <= row; ++i) {
        for(var j = 1; j <= i; ++j) {
          document.write("*");
        }
        document.write("</br>");
      }
      for(var i = row; i >= 1; i--) {
        for(var j = 1; j <= i; ++j) {
          document.write("*");
        }
        document.write("</br>");
      }
    }
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head>
    <style type = "text/css">
      .yellow {
        width : 350px;
        height : 350px;
        background : yellow;
        position : relative;
        margin-top : 5px;
      }
      #red {
        width : 40px;
        height : 40px;
        background : red;
        position : absolute;
        top : 0px;
        left : 0px;
      }
    </style>
  </head>
  <body>
    <button onclick="move()"> click </button>
    <div class = "yellow">
      <div id = "red"></div>
    </div>
  </body>
  <script type = "text/javascript">
    function move() {
      var elem = document.getElementById('red');
      var pos = 0;
      var anim = setInterval(animate, 5);
      function animate() {
        if(pos == 310) {
          clearInterval(anim);
        }
        pos++;
        elem.style.top = pos + "px";
        elem.style.left = pos + "px";
      }
    }
  </script>
</html>
