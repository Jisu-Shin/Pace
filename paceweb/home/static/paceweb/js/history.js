const useBtn = document.getElementById("useBtn");
const addBtn = document.getElementById("addBtn");
const usePoint = document.getElementById("use_point")

useBtn.addEventListener('click', onClickUsePoint);
addBtn.addEventListener('click', onClickAddPoint);

function onClickUsePoint(e) {
    console.log("포인트를 " + usePoint.value + "원 사용합니다.");
}

function onClickAddPoint(e) {
    console.log("포인트를 적립합니다.");

}

