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
<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <input type = "number" name = "first" id = "first" step = "any"/>
    <select id = "ope">
      <option value = "+"> + </option>
      <option value = "-"> - </option>
      <option value = "*"> * </option>
      <option value = "/"> / </option>
      <option value = "%"> ℅ </option>
    </select>
    <input type = "number" name = "duo" id = "duo" step = "any"/>
    <button onclick = "cal()"> calculate </button>
    <input type = "text" name = "" id = "res" readonly = ""/>
  </body>
  <script type = "text/javascript">
    function cal(){
      var op1 = document.getElementById('first').value;
      var op2 = document.getElementById('duo').value;
      var ope = document.getElementById('ope').value;
      if (ope == '+'){
        var res = parseInt(op1) + parseInt(op2);
      }
      if (ope == '-'){
        var res = parseInt(op1) - parseInt(op2);
      }
      if (ope == '*'){
        var res = parseInt(op1) * parseInt(op2);
      }
      if (ope == '/'){
        var res = parseInt(op1) / parseInt(op2);
      }
      if (ope == '%'){
        var res = parseInt(op1) % parseInt(op2);
      }
      document.getElementById('res').value = res;
    }
  </script>
</html>
