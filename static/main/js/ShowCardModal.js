let gradenote = {
    0: "Dolboeb, incorrect",
    1: "Very Bad",
    2: "Very Bad, A few letters are correct",
    3: "Mediocre",
    4: "A few letters incorrect",
    5: "Excellent!"
}
let modalWrap = null;
let ability_to_answer = true;

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

function getAnswer() {
    let form = document.getElementById("input-form");

    function completeV(value) {
        complete();
        form.text.value = '';   // Что бы была пустая строка после ввода
    }

    const changeQuestion = (new_word) => {
        let field = document.getElementById("question-field");
        field.textContent = new_word;
    }

    const endingOfStudy = () => {
        document.getElementById("btn-answer").remove();
        document.getElementById("answer-field").remove();
        document.getElementById("title-card-h5").textContent = "😢";
        ability_to_answer = false;
    }

    form.onsubmit = function () {
        let value = {
            user_answer: form.text.value
        };
        if (value.user_answer == '') return false;

        postAJAX('/courses/get_answer/', value, function (xhr) {
            window.alert(gradenote[xhr.answer_status]);
            changeQuestion(xhr.new_word);
            if (xhr.end_of_study) endingOfStudy();
        }, function (xhr, errmsg, err) {
        });

        completeV(value);
        return false;
    };
}

function showModalCard() {
    modalWrap = document.getElementById('OutCardModal');
    if (ability_to_answer) {
        modalWrap.querySelector('.modal-success-btn').onclick = function () {
            getAnswer();
        };
    }

    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
}

function showModalOverCard() {
    modalWrap = document.getElementById('OutCardModal');
    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
}