<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <div id = "Counter"></div>
    <button id = "btn">click</button>
    <button id = "bt" onclick = "stop()"> stop </button>
  </body>
  <script type = "text/javascript">
    var i = 0
    document.getElementById('btn').addEventListener("click", changeval);
    function changeval(){
      document.getElementById('Counter').innerText = i;
      i++;
    }
    document.getElementById('btn').addEventListener("mouseenter", colorolive);
    function colorolive() {
      document.getElementById('Counter').style.background = "olive";
    }
    document.getElementById('btn').addEventListener("mouseleave", colorchange);
    function colorchange() {
      document.getElementById('Counter').style.color = "red";
    }
    function stop(){
      document.getElementById('btn').removeEventListener("click", changeval)
    }
  </script>
</html>
