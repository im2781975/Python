<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <input type = "text" name = "name" id = "name"/>
    <button onclick="greet()"> Greet </button>
    <div class = "greet"></div>
  </body>
  <script type="text/javascript">
    function greet(){
      var name = document.getElementById('name').value;
      //alert(name);
      var string = "Hello " + name;
      document.getElementsByClassName('greet')[0].innerHTML = string;
    }
  </script>
</html>
