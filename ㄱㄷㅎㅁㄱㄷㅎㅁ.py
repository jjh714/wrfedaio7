import streamlit as st
import streamlit.components.v1 as components

st.title("🦖 방향키로 움직이는 공룡")

components.html("""
<!DOCTYPE html>
<html>
<body style="margin:0; overflow:hidden;">
<div id="game" style="
width:800px;
height:400px;
background:#87CEEB;
border:2px solid black;
position:relative;
overflow:hidden;
">

<div id="ground"
style="
position:absolute;
bottom:0;
width:100%;
height:40px;
background:green;">
</div>

<div id="dino"
style="
position:absolute;
left:100px;
bottom:40px;
font-size:60px;">
🦖
</div>

</div>

<script>
const dino = document.getElementById("dino");

let x = 100;
let y = 40;

document.addEventListener("keydown", function(e){

    if(e.key=="ArrowRight") x += 10;
    if(e.key=="ArrowLeft") x -= 10;
    if(e.key=="ArrowUp") y += 10;
    if(e.key=="ArrowDown") y -= 10;

    if(x<0) x=0;
    if(x>730) x=730;

    if(y<40) y=40;
    if(y>300) y=300;

    dino.style.left=x+"px";
    dino.style.bottom=y+"px";

});
</script>

</body>
</html>
""", height=430)
