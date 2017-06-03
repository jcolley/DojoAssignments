function randomChance(quarters,leave){
  quarters -= 1;
  var prize = 0;
  var rand1 = genRandom();
  var rand2 = genRandom();

  console.log(rand1 +" | "+rand2)

  if(rand1 === rand2){
    prize = Math.floor(Math.random() * (50 - 1 + 1)) + 1;
  }
  quarters += prize;
  return quarters;
}

function genRandom(){
  return Math.floor(Math.random() * (100 - 1 + 1)) + 1;
}

var quarters = 10;
var leave = 200;

while(quarters<leave && quarters){
  quarters = randomChance(quarters,leave);
  console.log(quarters);
}

if(quarters>0){console.log("YOU WIN!");}else{console.log("Lost it all...");}