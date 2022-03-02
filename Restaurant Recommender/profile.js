function changeText()
{
    let h = document.getElementById('myTarget');
    h.textContent = "When you're eating a watermelon!"
}
//DON'T FORGET ABOUT THE ELEMENT!!!
function remark(remarkName, elmnt, color) {

    var i, linktoclickinfo, linktoclicks;
//REMEMBER CORRECT CLASS NAME!!!
    linktoclickinfo = document.getElementsByClassName("linktoclickinfo");
    


    for (i = 0; i < linktoclickinfo.length; i++) {
        linktoclickinfo[i].style.display = "none";
    }
  
    linktoclicks = document.getElementsByClassName("linktoclick");



    for (i = 0; i < linktoclicks.length; i++) {
        linktoclicks[i].style.backgroundColor = "";
    }
  
    document.getElementById(remarkName).style.display = "block";
    elmnt.style.backgroundColor = color;
  }
  document.getElementById("openSesame").click();