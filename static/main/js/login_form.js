let modalWrap = null;
let askModalWrap = null;

const complete = () => {
    document.onkeydown = null;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const postAJAX = (url, data, successFunc, failFunc) => {
    $.ajax({
        url: url,
        method: "POST",
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        data: data,
    }).done(function (xhr) {
        //window.alert(xhr.status + ": " + xhr.responseText)
        successFunc(xhr);

    }).fail(function (xhr, errmsg, err) {
        // window.alert(xhr.status + ": " + xhr.responseText);
        failFunc(xhr, errmsg, err);
    });
}

function showAskLogin() {
    askModalWrap = document.getElementById("AskLoginModal");
    document.getElementById("close-form").onsubmit = function () {
        complete();
        return false;
    }

    let modal = new bootstrap.Modal(askModalWrap.querySelector('.modal'));
    modal.show();
}