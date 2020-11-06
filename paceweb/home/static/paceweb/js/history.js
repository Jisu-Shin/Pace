const useBtn = document.getElementById("useBtn");
const addBtn = document.getElementById("addBtn");
const add_point = document.getElementById("add_point").innerHTML;
const use_point = document.getElementById("use_point");
const total_point = document.getElementById("total_point").innerText;

useBtn.addEventListener('click', onClickUsePoint);
addBtn.addEventListener('click', onClickAddPoint);

// 포인트 사용
function onClickUsePoint(e) {
    console.log("포인트를 " + use_point.value + "원 사용합니다.");

    isValue(use_point.value);
}

function isValue(value) {
    if(value != null && value != '' && value != '0') {
        const question = confirm(value+" 포인트를 사용하시겠습니까?");
        
        // Would you like to your points? yes!
        if(question == true)
            usedPoint(value)
    } else {
        alert("입력값이 없습니다. 다시 입력해주세요.");
    }
}

// uesd point(DB 연동 필요. DB의 point 값을 total 값으로 업데이트 해야함)
function usedPoint(value) {
    console.log(value+"포인트를 사용합니다.");
    
    const total = parseInt(total_point) - value;

    alert(total+" 누적 포인트 입니다.");
}

// add point(DB 연동 필요. DB의 point 값을 total 값으로 업데이트 해야함)
function onClickAddPoint(e) {
    console.log("포인트를 적립합니다.");
    
    const total = parseInt(total_point) + parseInt(add_point);

    alert(total+" 누적 포인트 입니다.");
}

