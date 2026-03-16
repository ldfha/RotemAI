// 각종 요소
const code = document.querySelector('#code');
const sang = document.querySelector('#sang');
const su = document.querySelector('#su');
const dan = document.querySelector('#dan');

const msg = document.querySelector('#msg');
const tbody = document.querySelector('#tbody');

const btnAdd = document.querySelector('#btnAdd');
const btnUpdate = document.querySelector('#btnUpdate');
const btnDelete = document.querySelector('#btnDelete');
const btnReload = document.querySelector('#btnReload');

function setMsg(text){
    msg.textContent = text;
}

// 입력 폼 초기화
function clearForm(){
    code.value = "";
    sang.value = "";
    su.value = "";
    dan.value = "";
}

// 전체 자료 읽기
async function loadAll() {
    const res = await fetch('/api/sangdata');
    const data = await res.json();
    // console.log(data);
    tbody.innerHTML = "";
    data.data.forEach(r => {
        const tr = document.createElement("tr");
        tr.innerHTML = "<td>" + r.code + "</td>" + 
            "<td>" + r.sang + "</td>" + 
            "<td>" + r.su + "</td>" + 
            "<td>" + r.dan + "</td>" ;
        tbody.appendChild(tr);
    });
    clearForm();
    setMsg("조회완료");
}

async function addData() {
    const data = {
        code:Number(code.value),
        sang:sang.value,
        su:Number(su.value),
        dan:Number(dan.value),
    }
    const res = await fetch('/api/sangdata', {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(data)   // json으로 전송
    })

    await res.json();
    setMsg("추가 완료");
    clearForm();
    loadAll();  
}

async function updateData() {
    const data = {
        sang:sang.value,
        su:Number(su.value),
        dan:Number(dan.value),
    }
    const res = await fetch('/api/sangdata/'+ code.value, {
        method:"PUT",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(data)   // json으로 전송
    })
    const imsi = await res.json();
    if(imsi.ok)
        setMsg("수정 완료");
    else
        setMsg("수정 실패");

    clearForm();
    loadAll();  // 수정 후 조회  
}

async function deleteData() {
    const res = await fetch('/api/sangdata/'+ code.value, {
        method:"DELETE"
    })
    const imsi = await res.json();
    if(imsi.ok)
        setMsg(imsi.msg);
    else
        setMsg("삭제 실패" + "imsi.msg");

    clearForm();
    loadAll();  // 삭제 처리 후 전체 자료 보기  
}

window.onload = loadAll;

btnAdd.onclick = addData;
btnUpdate.onclick = updateData;
btnDelete.onclick = deleteData;
btnReload.onclick = loadAll;