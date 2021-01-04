function changeBGC1() {
    document.getElementById("theBox").style.backgroundColor = "rgb(210, 255, 210)";
    document.getElementById("botton1").style.border = "3px solid black";
    document.getElementById("botton1").style.marginRight = "0";
    document.getElementById("botton1").style.marginTop = "0";
    document.getElementById("botton2").style.border = "1px solid black";
    document.getElementById("botton2").style.marginRight = "2px";
    document.getElementById("botton2").style.marginTop = "2px";

}

function changeBGC2() {
    document.getElementById("theBox").style.backgroundColor = "rgb(255, 230, 234)";
    document.getElementById("botton1").style.border = "1px solid black";
    document.getElementById("botton1").style.marginRight = "2px";
    document.getElementById("botton1").style.marginTop = "2px";
    document.getElementById("botton2").style.border = "3px solid black";
    document.getElementById("botton2").style.marginRight = "0px";
    document.getElementById("botton2").style.marginTop = "0px";
}

function alreadyFirstOne() {
    alert("已是第一章")
}

function alreadyLastOne() {
    alert("已是最后一章")
}