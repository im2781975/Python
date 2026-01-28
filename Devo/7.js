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
<!DOCTYPE HTML>
<html>
  <head></head>
  <body id = "body">
    <center>
      <div></div>
      <h2> PRINTABLE DATA</h2>
      <p id = "data">
        Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Ut ut maximus sem, sed 
        iaculis neque. Fusce ultricies augue euismod 
        mi dignissim, ut efficitur mauris sodales. Nullam
        dictum tristique facilisis. Fusce at justo in dolor 
        gravida placerat vel eu sapien. Vivamus purus felis, 
        pellentesque eu eros ut, efficitur hendrerit diam. sed
        eu augue lacus. Morbi nulla eros, aliquam quis pharetra in, 
        blandit a eros. Duis vestibulum, nunc nec maximus efficitur, 
        nibh dui aliquet tortor, a vulputate ipsum nunc eu erat.
      </p>
      <button onclick = "printpage()">print</button>
      <p>
        Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Ut ut maximus sem, sed 
        iaculis neque. Fusce ultricies augue euismod 
        mi dignissim, ut efficitur mauris sodales. Nullam
        dictum tristique facilisis. Fusce at justo in dolor 
        gravida placerat vel eu sapien. Vivamus purus felis, 
        pellentesque eu eros ut, efficitur hendrerit diam. sed
        eu augue lacus. Morbi nulla eros, aliquam quis pharetra in, 
        blandit a eros. Duis vestibulum, nunc nec maximus efficitur, 
        nibh dui aliquet tortor, a vulputate ipsum nunc eu erat.
      </p>
    </center>
  </body>
  <script type = "text/javascript">
    function printpage() {
       window.print();
      var body = document.getElementById('body').innerHTML;
      var data = document.getElementById('data').innerHTML;
      document.getElementById('body').innerHTML = data;
      window.print();
      document.getElementById('body').innerHTML = body;
    }
  </script>
</html>
<!DOCTYPE HTML>
<html>
  <head></head>
  <body> <!--onkeyup - when the key will be press -->
    <input type="text" name = "" onkeyup="val(this)">
    <div id = "res"></div>
  </body>
  <script type = "text/javascript">
    function val(elem) {
      // document.getElementById('res').innerText = elem.value
      // isNan - if not a Number
      document.getElementById('res').style.color = "red";
      if(isNaN(elem.value)) {
        document.getElementById('res').innerText = "please enter number only"
      }
      else {
        document.getElementById('res').innerText = "";
        if(elem.value.length >= 10) {
          document.getElementById('res').innerText = "please enter only 10 digit"
        }
        else {
          document.getElementById('res').innerText = "";
        }
      }
    }
  </script>
</html>
