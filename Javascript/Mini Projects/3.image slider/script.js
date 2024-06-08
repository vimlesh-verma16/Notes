let flag=1;

function controller(num){
    flag=flag+num;
    slideshow(flag)
}

slideshow(flag);

function slideshow(num){
    let slides=document.getElementsByClassName("slide");
    
    for(let x of slides){
        x.style.display="None";
    }
    
    if (flag==slides.length){
        num=0;
        flag=0;

    }
    if (flag<0){
        num=slides.length-1;
        flag=slides.length-1;

    }
    slides[num].style.display="block";
}