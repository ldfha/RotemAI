// 자료 추가시 입력 자료 간단 검증 스크립트
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#addForm");
    if(!form) return;

    form.addEventListener("submit", (e) => {
        const sang = document.getElementById("sang").value.trim();
        const su = document.getElementById("su").value.trim();
        const dan = document.getElementById("dan").value.trim();

        // validation
        // 1) 필수 입력 체크하기
        if(sang === ''){
            alert("상품명을 입력하시오");
            document.getElementById("sang").focus();
            // submit 중단
            e.preventDefault();
            return;
        }

        // 2) 숫자 체크
        if(!/^\d+$/.test(su)){
            alert("수량은 숫자만 허용");
            document.getElementById("su").focus();
            e.preventDefault();
            return;
        }
        if(!/^\d+$/.test(dan)){
            alert("단가는 숫자만 허용");
            document.getElementById("dan").focus();
            e.preventDefault();
            return;
        }
    })
});