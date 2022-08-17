let previous;
    let select;
    //let dict;
    //const send_method = 'POST';
    //const url = 'http://127.0.0.1:5000/';
    //const url_address = 'http://127.0.0.1:5000/main/table';

async function send_json(message) {
    const request = new XMLHttpRequest();
    request.open(send_method, url_address, true);
    request.responseType = "json";
    request.setRequestHeader("Content-Type", "application/json");
    request.send(message);
    // let result = await fetch(url_address, {
    //         method : 'POST',
    //     headers : {
    //             'Content-Type': 'application/json;charset=utf-8'
    //     },
    //     body : JSON.stringify({ "button": "update", "choice_item": choice})
    // }).catch();

}

function onClickRow(element) {
    if(previous !== undefined)
        previous.style.background = "white";
    element.style.background = "#c4beed";
    previous = element;
     select = element.cells[0].innerText;
     console.log(select);
}

function onClickUpdate(element) {
    if (select === undefined) {
        alert("Select a table row")
    }
    else {
        //dict = JSON.stringify({ "button": "update", "choice_item": choice});
        //send_json(dict);
        document.location.href = window.location.href + "/" + select + "/update";
        console.log(document.location.href);
        }
}

function onClickDelete(element) {
    if (select === undefined) {
        alert("Select a table row")
    }
    else {
        //dict = {button: "delete", choice_item: choice};
        //send_json(dict);
        document.location.href = window.location.href + "/" + select + "/delete";
        }
}