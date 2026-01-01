<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <button onclick = "openwin()">open Window</button>
    <button onclick = "closewin()">close Window</button>
    <h1></h1>
    <button onclick = "window.history.forward();"> Forward </button>
    <button onclick = "window.history.back();"> Back </button>
    <button onclick = "window.history.Go(-3);"> Go </button> <!-- going to 3rd window -->
  </body>
  <script type = "text/javascript">
    var win;
    var win2;
    function openwin(){
      win = window.open("https://images.google.com/", "width=50px", "height=50px");
      win2 = window.open()
    }
    function closewin(){
      win.close();
    }
    var cnt = window.history.length;
    document.getElementsByTagName('h1')[0].innerText = cnt;
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <button onclick = "availht()"> AVL HEIGHT </button>
    <button onclick = "totalht()"> TOTAL HEIGHT </button>
    <button onclick = "availwidth()"> AVL WIDTH </button>
    <button onclick = "colordep()"> color depth </button>
    <button onclick = "pxdepth()"> pxl Depth</button>
    <button onclick = "width()"> width </button>
    <button onclick = "OTP()"> OTP </button>
  </body>
  <script type = "text/javascript">
    function availht(){
      var ht = screen.availHeight;
      alert(ht);
    }
    function totalht(){
      var ht = screen.height;
      alert(ht);
    }
    function availwidth(){
      var ht = screen.height;
      alert(ht);
    }
    function colordep(){
      var dp = screen.colorDepth;
      alert(dp);
    }
    function pxdepth(){
      var dp = screen.pixelDepth;
      alert(dp);
    }
    function width(){
      var ht = screen.width;
      alert(ht);
    }
    function OTP(){
      var x = Math.round(Math.random() * 1000);
      document.write(x)
    }
    var x = Math.PI;
    var x = Math.round(3.6);
    var x = Math.pow(2, 8);
    var x = Math.sqrt(9);
    var x = Math.abs(-7);
    var x = Math.ceil(3.6);
    var x = Math.floor(3.4);
    var x = Math.min(3, 5, 7);
    var x = Math.max(3, 5, 7);
    var x = Math.random();
    document.write("<h1>" + x + "</h1>")
  </script>
</html>
