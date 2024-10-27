let flag = true;
function control() {
    let btn = document.getElementById("btn");

    let circle = document.getElementById("circle");

    if (flag) {
        btn.style.backgroundColor = "rgba(5, 122, 255, 0.747)";
        flag = false;
        circle.className = "right";
        document.getElementById("bodybg").style.backgroundColor="aqua";
    }
    else {
        btn.style.backgroundColor = "lightgrey";
        flag = true;
        circle.className = "left";
        document.getElementById("bodybg").style.backgroundColor="green";
    }

}

function menu(){
    let ele=document.getElementById("parent");
    ele.classList.toggle("display-n");
}

let arr=0;
function controller(num){
arr+=num;
show(arr);
}

show(arr);

function show(num){
    let slides=document.getElementsByClassName("inner");
    
    for(let x of slides){

        x.style.display="None";
    }
    if(num==slides.length){
        num=0;
        arr=0;
    }
    if(num<0){
        num=slides.length-1;
        arr=slides.length-1;
    }
    slides[num].style.display="block";
}



function sub(e){
    let book=document.getElementById("book");
    console.log(book.value);
e.preventDefault();
}

