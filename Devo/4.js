<!DOCTYPE HTML>
<html>
  <head>
    <style type = "text/css">
      h1{
        font-size : 40px;
        text-align : center;
        font-family : verdana;
      }
    </style>
  </head>
  <body onload = "showtime()">
    <h2 style = "text-align : center"> clock </h2>
    <h1></h1>
  </body>
  <script type = "text/javascript">
    function showtime(){
      var d = new Date()
      var h = d.getHours()
      var m = d.getMinutes()
      var s = d.getSeconds()
      var session = "AM"
      if (h > 12){
        h = h - 12;
      }
      if (h >= 12){
        session = "PM"
      }
      h = h < 10 ? "0" + h : h;
      m = m < 10 ? "0" + m : m;
      s = s < 10 ? "0" + s : s;
      var time = h + " : " + m + " : " + s + " " + session;
      document.getElementsByTagName("h1")[0].innerText = time;
      setTimeout(showtime, 1000);
    }
  </script>
</html>
