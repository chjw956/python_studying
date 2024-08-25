let target = document.getElementById("clock")

function clock() {
    let time = new Date();

    let hours = time.getHours();
    let minutes = time.getMinutes();
    let apm = "AM";

    // Anywhere, Korea (11:00 AM)
    if (hours >= 13) {
    hours %= 12
    apm = "PM"
    } 

    target.innerHTML = `Anywhere, Korea (${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")} ${apm})`;
}

// 참고 사이트: https://qh5944.tistory.com/158
function copy() {
    let url = '';
    let textarea = document.createElement("textarea");

    document.body.appendChild(textarea);

    url = 'chjw9559@gmail.com';

    textarea.value = url;
    textarea.select();

    document.execCommand("copy");
    document.body.removeChild(textarea);

    alert("메일 주소가 복사되었습니다.");
}

const speed = 90;

// reference: https://www.designkits.co.kr/blog/web-css/text/typing-effect?srsltid=AfmBOopT_IJQ18nLtbcIjKu13SFGvPFa1qRssYT2Tf_7kNvU8ja8IOGV
function typeWriter(arr, level, text, index) {  
    if (index < text.length) {
        document.getElementById("text" + level).textContent += text.charAt(index);
        setTimeout(() => typeWriter(arr, level, text, index + 1), speed);
    }else{
        if(level < arr.length){
            text = arr[level + 1]
            setTimeout(() => {
                cursor.insertAdjacentHTML("beforebegin",`<span class = "text_span" id = "text${level + 1}"></span>`);
                typeWriter(arr, level + 1, text, 0), speed});
        }  
    }
}  

// const arr = [
//     "Hi!", 
//     "I'm Jiwon Choi.", 
//     "I'm aspiring backend developer, based in Korea.",
//     "I'm interested in DB design,",
//     "and my dream is to become a developer",
//     "who creates a good experience for users",
//     "through efficient programming💛"
// ];

const arr = [
    "안녕!", 
    "나는 백엔드 개발자를 꿈꾸는 최지원이야.", 
    "나는 DB 설계에 흥미가 많아.",
    "그래서 내 꿈은 사용자에게 효율적인 프로그래밍으로",
    "좋은 경험을 주는 개발자가 되는 거야!",
    "우헤헤💛"
];

const cursor = document.getElementById("cursor");          

clock();
setInterval(clock, 600000);
cursor.insertAdjacentHTML("beforebegin",`<span id="text0"></span>`);
typeWriter(arr, 0, arr[0], 0); 