let cr = {
    name : "BMW", cost : 76.5, mileage : 8.6, 
    start : function() { console.log("start"); },
    stop : function() { console.log("end"); },
};
console.log(cr.name); console.log(cr.mileage);
cr.stop(); cr.start();
let rc = cr; console.log(rc.name);
rc.name = "KIA";
console.log(rc.name); console.log(cr.name);
function exmp() {
    let cr = {
    name : "BMW", cost : 76.5, mileage : 8.6 }; return cr;
}
console.log(exmp());
function fun(car) { console.log(car); }
fun(cr);
function add(a, b) { console.log(a + b); }
console.log(add.name); console.log(add.length);
let add2 = add; add2(30, 35);
function exp(addd){ 
    addd(100, 200);
}
function ad(a, b){ console.log(a + b); } 
exp(ad); add(300, 600);
let role = "Admin";
function checkAccess() {
    let hasAccess = false;
    if(role === "Admin") {
        let welcomemsg = '${role} admin privilages';
        hasAccess = true;
        console.log(welcomemsg);
    }
    console.log("Has Access: ", hasAccess);
}
checkAccess();
// closure
function fun1() {
    console.log("fun1()");
    let val = 10;
    function fun2() {
        console.log("fun2()", val);
    } return fun2;
}
exmp = fun1();
exmp();
function createcounter() {
    let counter = 0;
    return function () {
        counter += 1; console.log(counter);
    }
}
let countA = createcounter();
countA();
// callback
function add(a, b) { return a + b; }
function sub(a, b) { return a - b; }
function mul(a, b) { return a * b; }
function calc(a, b, callback){ return callback(a, b); }

console.log(add(5, 9));
