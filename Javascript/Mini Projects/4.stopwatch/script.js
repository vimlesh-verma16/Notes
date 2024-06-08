let hr = 0;
let min = 0;
let sec = 0;
let count = 0;

var time = false;

function start() {
    time = true;
    stopwatch();
}

function stop() {
    time = false;
}

function reset() {
    time = false;
    hr=0;
    sec=0;
    min=0;
    count=0;
   let t= document.getElementsByClassName("digit");
   for(let x of t){
       x.innerHTML="00";
   }
}

function stopwatch() {
    if (time == true) {
        count += 1;
        if (count == 100) {
            sec += 1;
            count=0;
        }
        if (sec == 60) {
            min += 1;
            sec=0;
        }
        if (min == 60) {
            hr += 1;
            min=0;
        }

        document.getElementById("count").innerHTML=count;
        document.getElementById("sec").innerHTML=sec;
        document.getElementById("min").innerHTML=min;
        setTimeout("stopwatch()", 10);
    }
}