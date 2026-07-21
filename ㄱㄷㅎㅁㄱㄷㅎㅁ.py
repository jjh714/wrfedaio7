<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>동물 미연시 - 숲속의 인연</title>

<style>
body {
    background:#f5ffe8;
    font-family: "Arial", sans-serif;
    text-align:center;
}

#game {
    width:500px;
    margin:50px auto;
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0 0 20px #aaa;
}

button {
    padding:12px 20px;
    margin:10px;
    border:none;
    border-radius:10px;
    background:#79c267;
    color:white;
    cursor:pointer;
}

button:hover {
    background:#4f9d43;
}

#animal {
    font-size:80px;
}

</style>
</head>

<body>

<div id="game">

<h1>🌲 숲속의 인연 🌲</h1>

<div id="animal">🐺</div>

<h2 id="name">늑대 루루</h2>

<p id="story">
깊은 숲에서 길을 잃은 당신은 신비로운 늑대를 만났다.
</p>

<p>
호감도 : <span id="love">0</span>
</p>

<button onclick="choice(1)">🍎 먹이를 준다</button>
<button onclick="choice(2)">🎵 노래를 불러준다</button>
<button onclick="choice(3)">🏃 도망간다</button>

<h3 id="result"></h3>

</div>


<script>

let love = 0;
let day = 0;

const events = [
[
"🐺",
"늑대 루루",
"루루가 꼬리를 흔들며 다가왔다.",
[3,2,-2]
],

[
"🐱",
"고양이 나나",
"길고양이 나나가 당신의 손 냄새를 맡는다.",
[2,3,-1]
],

[
"🦊",
"여우 코코",
"여우 코코가 숲의 비밀을 알려준다.",
[4,1,-3]
]
];


let animalIndex = 0;


function choice(num){

let gain = events[animalIndex][3][num-1];

love += gain;
day++;

document.getElementById("love").innerText = love;

document.getElementById("story").innerText =
"당신의 선택에 동물이 반응했다!";


if(day >= 3){
ending();
}

else if(day == 1){
changeAnimal(1);
}

else if(day == 2){
changeAnimal(2);
}

}


function changeAnimal(index){

animalIndex=index;

document.getElementById("animal").innerText =
events[index][0];

document.getElementById("name").innerText =
events[index][1];

document.getElementById("story").innerText =
events[index][2];

}


function ending(){

let text="";

if(love>=8){
text="💚 해피 엔딩!\n동물 친구가 평생의 파트너가 되었다!";
}

else if(love>=3){
text="🙂 좋은 친구 엔딩!\n숲속에서 계속 만나는 사이가 되었다.";
}

else{
text="💔 이별 엔딩...\n동물은 조용히 숲으로 돌아갔다.";
}


document.getElementById("result").innerText=text;

document.querySelectorAll("button")
.forEach(b=>b.disabled=true);

}

</script>

</body>
</html>
