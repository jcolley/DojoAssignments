//Enter Parameters Here
var days = 30; //How much reward after X days
var target = 10000.00; //How many days until king makes $X
var infinite = Infinity; //How many days until king has Infinite funds

function rewardAfterXDays(days){
    var amount = .01;
    for(var i=0;i<=days;i++){
        amount *= 2;
    }
    return amount;
}

function daysUntilTarget(target){
    var amount = .01;
    var days = 0;
    while(amount<=target){
        amount *= 2;
        days++;
    }
    return days;
}

function daysUntilInfinite(infinite){
    var amount = .01;
    var days = 0;
    while(amount!==infinite){
        amount *= 2;
        days++;
    }
    return days;
}

console.log("King has", "$"+rewardAfterXDays(days), "after",days,"days.");
console.log("It would take the King",daysUntilTarget(target),"days to reach","$"+target+".");
console.log("It would take the King",daysUntilInfinite(infinite),"days to reach infinite funds!");