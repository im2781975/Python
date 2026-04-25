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
