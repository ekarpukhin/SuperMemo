let gradenote = {
    0: "Dolboeb, incorrect",
    1: "Very Bad",
    2: "Very Bad, A few letters are correct",
    3: "Mediocre",
    4: "A few letters incorrect",
    5: "Excellent!"
}
let modalWrap = null;

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

function getAnswer() {
    let form = document.getElementById("input-form");

    function completeV() {
        complete();
        form.text.value = '';   // Что бы была пустая строка после ввода
    }

    const changeQuestion = (new_word, new_lvl) => {
        let field = document.getElementById("question-field");
        field.textContent = new_word;
        field = document.getElementById("title-card-h6");
        field.textContent = new_lvl;
    }

    form.onsubmit = function () {
        let value = {
            user_answer: form.text.value
        };
        if (value.user_answer == '') return false;

        postAJAX('/courses/get_levelcheck/', value, function (xhr) {
            window.alert(gradenote[xhr.answer_status]);
            changeQuestion(xhr.new_word, xhr.new_level);
        }, function (xhr, errmsg, err) {
        });

        completeV();
        return false;
    };
}

function showCard() {
    modalWrap = document.getElementById('OutCardModal');
    modalWrap.querySelector('.modal-success-btn').onclick = function () {
        getAnswer();
    };

    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
}