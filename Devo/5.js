<!DOCTYPE HTML>
<html>
  <head>
    <style type = "text/css">
      #main{
        color : blue;
        font-size : 20px;
        text-align : center;
        margin-top : 5px;
        cursor: pointer;
        transition : 2s;
      }
    </style>
  </head>
  <body>
    <div id = "main" onmouseenter = "modify()" onmouseleave = "unmodify()"> PISAR-TECH </div>
  </body>
  <script type = "text/javascript">
    function modify(){
      document.getElementById('main').style.fontSize = "30px";
      document.getElementById('main').style.color = "olive";
      document.getElementById('main').style.fontFamily = "oblique";
    }
    function unmodify(){
      document.getElementById('main').style.fontSize = "20px";
      document.getElementById('main').style.color = "blue";
      document.getElementById('main').style.fontFamily= "";
    }
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head>
    <style type = "text/css">
    </style>
  </head>
  <body>
    <button onclick = "start()"> start </button>
    <button onclick = "stop()"> stop </button>
    <h1 id = "h1"></h1>
    <button onclick = "Off()"> Off </button>
  </body>
  <script type = "text/javascript">
    var my;
    function start(){
      my = setTimeout(
        function(){
          document.write("cube")
        },5000
      );
    }
    function stop(){
      clearTimeout(my);
      alert("")
    }
    var ou = setInterval(count, 1000);
    var c = 0
    function count(){
      document.getElementById('h1').innerText = c;
      c++;
    }
    function Off(){
      clearInterval(ou);
    }
  </script>
</html>
