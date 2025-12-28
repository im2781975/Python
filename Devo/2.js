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
<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    name : <i id = "res"></i>
    </br>
    <button onclick = "call()"> call </button>
  </body>
  <script type = "text/javascript">
    function call(){
      var res = prompt("Enter Your name", "")
      document.getElementById('res').innerHTML = res
    }
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head></head>
  <body></body>
  <script type = "text/javascript">
    var age = 17
    if (age >= 18){
      document.write("<h1> can vote</h1>")
    }
    else if(age == 17){
      document.write("<h1> please wait one more year</h1>")
    }
    else {
      alert("can't vote")
    }
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head>
    <h1 id = "res"></h1>
    <button onclick="pop()"> POP </button>
    <button onclick="push()"> PUSH </button>
    <button onclick="slice()"> SLICE </button>
    <button onclick="Reverse()"> REVERSE </button>
    <button onclick="Shift()"> SHIFT </button>
  </head>
  <body></body>
  <script type = "text/javascript">
    //Array
    cars = [] ; // new Array()
    cars = ["A", "B", "C", "D"]
    cars[4] = "E"
    document.write(cars[4]);
    var arr = ["A", "B", "C", "D"]
    var ray = ["1", "2", "3", "4"]
    //var flg = Array.isArray(arr);
    //var flg = arr.valueOf();
    //var flg = arr.join("|");
    var flg = arr.concat(ray);
    document.write("<h1>" + flg + "</h1>");
    var idx = flg.indexOf("C");
    document.write("<h1>" + idx + "</h1>");
    var dem = flg;
    document.getElementById('res').innerText = dem;
    function pop(){
      dem.pop();
      document.getElementById('res').innerText = dem;
    }
    function push(){
      var x = prompt("Enter", "")
      dem.push(x)
      //dem.push("X");
      document.getElementById('res').innerText = dem;
    }
    function slice(){
      var x = dem.slice(2);
      // var x = dem.slice(1, 2);
      document.getElementById('res').innerText = x;
    }
    function Reverse(){
      dem.reverse();
      document.getElementById('res').innerText = dem;
    }
    function Shift(){
      var x = dem.shift();
      document.getElementById('res').innerText = x;
    }
    //for loop
    for(var count = 10; count >-10; --count){
      if(count == 5){
        continue; //break
      }
      if(count % 2 == 0){
        continue;
      }
      document.write(" " + count);
    }
    document.write("<br/>Loop Ended<br/>")
    //while loop
    var i = 0;
    while(i < 10){
      document.write(i + " ");
      i++;
    }
    document.write("<br/>Loop Ended<br/>")
    //forEach loop
    var cars = ["A", "B", "C", "D"]
    cars.forEach(car);
    function car(item, index, array){
      // document.write(index + item + " ")
      array[index] = item + "0"
    }
    cars.forEach(after);
    function after(item, index){
      document.write(index + "-" + item + " ")
    }
    document.write("<br/>")
    //switch
    var i = 4
    switch(i){
      case 1:
      document.write("i is equal to 1");
      break;
      case 2:
      document.write("i is equal to 2");
      break;
      case 3:
      document.write("i is equal to 3");
      break;
      case 4:
      document.write("i is equal to 4");
      break;
      default:
      document.write("i is greater than 5");
      break;
    }
    document.write("<br/>Out of switch<br/>")
  </script>
</html>
