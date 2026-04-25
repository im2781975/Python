let a = 45.9
console.log(a); console.log(typeof a);
let b = -1 / 0;
console.log(b); console.log(typeof b);
let c = "Hello" / 2;
console.log(c); console.log(typeof c);
let d = 9876543211234567890123n;
let e = 9876543311234567890123n;
console.log(d + e); console.log(typeof d);
// bigint & int can't perform any arithmetic operation
let e1 = "abcd"; console.log(e1);
let iscontain = true; 
console.log(iscontain); console.log(typeof iscontain)
let f; console.log(f);
let g = 97; let h = String(g);
console.log(typeof h);
let i = String(iscontain); console.log(typeof i);
let j = Number(e1); console.log(typeof j);
let k = "567TAP"; // "TAP567", " 123TAP", " 1 2 3"
let l = parseInt(k);
console.log(typeof(l)); console.log(l);
console.log(Boolean(NaN));// 0, "", [], null
console.log(Boolean(-Infinity));
// compare
let age = 18; console.log(age == 18);
console.log("ibrahim" == "Ibrahim")
console.log(5 == "5"); console.log(5 === '5')
console.log(true == '1');console.log(undefined == null);
console.log('' == 0); console.log(false == '')
console.log(null == false); console.log(undefined == 0);
console.log(NaN == NaN);
console.log(Number(true) == Number('1'));
console.log('01' == 1); console.log('010' == 10);
// control statement
let ag = 20;
if(ag < 12) { console.log("child"); }
else if(ag < 65){ console.log("adult"); }
else{ console.log("senior");}
let isvip = true;
if(isvip){ console.log("welcome"); }
else { console.log("Go Away"); }

let balance = 1000, withdraw = 700;
if(balance >= withdraw){ balance -= withdraw;}
else{ console.log("Insufficient"); }
console.log(balance);

let user = "student"
switch(user == "admin") {
    case "admin":
        console.log("Admin"); break;
    case "editor":
        console.log("editor"); break;
    case "author":
        console.log("author"); break;
    default:
        console.log("denied")
}
let day = 0
switch(day) {
    case 0:
    case 6:
        console.log("Happy weekend!!"); break;
    case 1:
        console.log("Monday"); break;
    case 2:
    case 3:
    case 4:
        console.log("Midweak"); break;
    case 5:
        console.log("TGIF"); break;
}
let age = 20;
console.log(age >= 18 ? "can vote" : "can't vote");

let i;
for(i = 0; i <= 2; i++) console.log("*");
i = 0;
while(i <= 2) { console.log("#"); i++;}
i = 0;
do {
    console.log("¥"); i++;
} while(i <= 2);
// rectangle
let row;
for(let i = 0; i <= 5; i++) {
    row = "";
    for(let j = 0; j <= 5; j++) row += "*";
    console.log(row);
}
// holo rect
row; 
let n = 5;
for(let i = 1; i <= n; i++) {
    row = "";
    for(let j = 1; j <= n; j++) {
        if(i == 1 || i == n || j == 1 || j == n) row += "*";
        else row += " ";
    }
    console.log(row);
}
//shape
row; 
n = 35;
for(let i = 0; i < n; i++) {
    row = "";
    for(let j = 0; j < n; j++) {
        if(i == 0 || i == n - 1|| j == 0 || j == n - 1 || i == Math.floor(n / 2) || j == Math.floor(n / 2) || i == j || i == n - j - 1 || i + j == Math.floor(n / 2) || i - j == Math.floor(n / 2) || i + j == (n - 1) + Math.floor(n / 2) || j - i == Math.floor(n / 2)) row += "*";
        else row += " ";
    }
    console.log(row);
}
// function
let a = 100, b = 200;
function add() {
    let c = a + b; /*console.log(c); */
    return c; 
} console.log(add());
function sub(x, y) {
    let c = x - y; /* console.log(c); */
    return c;
} console.log(sub(a, b));
let fun = function(m, n) { return m + n; }
console.log(fun(5, 9));
/*let unc = (a, b) => { return a + b; } */
let unc = (a, b) => a + b;
console.log(unc(8, 6));
// persentage
function calcgrade(marks, total) {
    let percent = (marks / total) * 100;
    let grade;
    if(percent >= 90) grade = 'A';
    else if(percent >= 80) grade = 'B';
    else if(percent >= 70) grade = 'C';
    else if(percent >= 60) grade = 'D';
    else if(percent >= 50) grade = 'E';
    else grade = 'F';
    console.log(grade);
}
calcgrade(93, 100);
let exmp = function() { console.log("called"); }
exmp();
(function() { console.log("called")})();
// Hoisting
console.log(l); var l = 100; console.log(l);
console.log(l); let l = 50; console.log(l);
greet();
function greet () { console.log("Hello"); }

let a;
function fun() { console.log(a); }
a = 100; console.log(a);
fun();
function unc() {
    var x = 100; console.log(x);
}
// console.log(x);
unc();
//block scope
tmp = 30
if(tmp > 25) {
    var cool = tmp - 25; console.log(cool);
}
else {
    var heat = 25 - tmp; console.log(heat);
}
console.log(tmp); console.log(heat); console.log(cool);
function print(num) {
    for(var i = 1; i <= num; ++i) console.log(i);
    console.log(i);
}
print(8);
