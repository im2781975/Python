<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <h1 id = "res"></h1>
    <button onclick = "getDateTime()"> DateTime </button>
    <button onclick = "getYear()"> Year </button>
    <button onclick = "getMonth()"> Month </button>
    <button onclick = "getHour()"> Hour </button>
    <button onclick = "getDate()"> Date </button>
    <button onclick = "getmin()"> Minute </button>
    <button onclick = "getsec()"> Second </button>
    <button onclick = "getmilisec()"> Milisec </button>
    <button onclick = "toTime()"> Time </button>
    <button onclick = "toDay()"> Day </button>
  </body>
  <script>
    var date = new Date()
    function getDateTime(){
      document.getElementById('res').innerText = date;
    }
    function getYear(){
      document.getElementById('res').innerText = date.getFullYear();
    }
    function getMonth(){
      var month = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Set", "Oct", "Nov", "Dec"]
      document.getElementById('res').innerText = month[date.getMonth()];
    }
    function getHour(){
      document.getElementById('res').innerText = date.getHours();
    }
    function getDate(){
      document.getElementById('res').innerText = date.getDate();
    }
    function getmin(){
      document.getElementById('res').innerText = date.getMinutes();
    }
    function getsec(){
      document.getElementById('res').innerText = date.getSeconds();
    }
    function getmilisec(){
      document.getElementById('res').innerText = date.getMilliseconds();
    }
    function toTime(){
      document.getElementById('res').innerText = date.getTime();
    }
    function toDay(){
      document.getElementById('res').innerText = date.getDay();
    }
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head></head>
  <body>
    <input type = "" name = "nome"/>
    <button onclick = "getname()"> submit </button></br>
    <button onclick = "text()"> text </button>
    <button onclick = "Interval()"> Try! </button>
    <button onclick = "Delay()"> Delay </button>
    <h1></h1>
  </body>
  <script>
    //var a = "mollavai" // 1 | true | [] | 
    //var a = new Array()
    //document.write(typeof a)
    function getname(){
      var name = document.getElementsByName('nome')[0].value;
      document.getElementsByName('nome')[0].value = "";
      document.getElementsByTagName("h1")[0].innerHTML = name;
    }
    function text(){
      alert("No")
    }
    function Interval(){
      setInterval(
        function(){
          alert("Yes")
        }, 5000 // repeted alert every 5 sec
        )
    }
    function Delay(){
      setTimeout(
        function(){
          document.write("Hello")
        },9000 // delay for execute the func
      );
    }
  </script>
</html>
