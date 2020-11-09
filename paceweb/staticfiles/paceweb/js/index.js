const cameraBtn = document.getElementById("cameraBtn");
const historyBtn = document.getElementById("historyBtn");

cameraBtn.addEventListener("click", loadCamera);
historyBtn.addEventListener("click", changPage);

function loadCamera(e) {
    console.log("카메라를 실행합니다11111.");
    location.href = '/call_pop';
}

function changPage(e) {
    location.href = '/history';
}