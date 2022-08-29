let addp1 = document.querySelector (".addp1");
let adda1 = document.querySelector (".adda1");
let minp1 = document.querySelector (".minp1");
let mina1 = document.querySelector (".mina1");
let counter = document.querySelector(".counter");
let counter2 = document.querySelector(".counter2");


addp1.addEventListener('click', addp1g);
adda1.addEventListener('click', addp1a);
minp1.addEventListener('click', minp1g);
mina1.addEventListener('click', minp1a);



function addp1g(){
	counter_num = counter.innerHTML
	counter.innerHTML = parseInt(counter_num) + 1
}

function addp1a(){
	counter_num = counter2.innerHTML
	counter2.innerHTML = parseInt(counter_num) + 1
}

function minp1g(){
	counter_num = counter.innerHTML
	counter.innerHTML = parseInt(counter_num) - 1
}

function minp1a(){
	counter_num = counter2.innerHTML
	counter2.innerHTML = parseInt(counter_num) - 1
}