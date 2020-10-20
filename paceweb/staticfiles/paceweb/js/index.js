const cameraBtn = document.getElementById("cameraBtn");
const historyBtn = document.getElementById("historyBtn");

cameraBtn.addEventListener("click", loadCamera);
historyBtn.addEventListener("click", changPage);

function loadCamera(e) {
    console.log("카메라를 실행합니다.");
}

function changPage(e) {
    location.href = '/history';
}