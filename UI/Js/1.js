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
