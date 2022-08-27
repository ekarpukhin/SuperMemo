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

const hideEl = (id) => {
    let div = document.getElementById(id);
    div.style.visibility = 'hidden';
}

const showEl = (id) => {
    let div = document.getElementById(id);
    div.style.visibility = 'visible';
}

function getAnswer(set_mode, user_answer) {
    let form = document.getElementById("input-form");

    function complete() {
        document.onkeydown = null;
        if (!set_mode) form.text.value = '';   // Что бы была пустая строка после ввода
    }

    const endingOfStudy = () => {
        document.getElementById("btn-to-answer").remove();
        document.getElementById("answer-field").remove();
        document.getElementById("title-card-h5").textContent = "😢";
        let fields = document.getElementsByClassName("vers-btn");
        for (let i = 0; i < fields.length;) {
            fields[i].remove();
        }
        ability_to_answer = false;
    }

    const changeQuestion = (new_word, new_set) => {
        let field = document.getElementById("question-field");
        field.textContent = new_word;
        let fields = document.getElementsByClassName("vers-btn");
        for (let i = 0; i < fields.length; i++) {
            fields[i].textContent = new_set[i];
        }
    }

    function get_value() {
        if (set_mode) return user_answer;
        return form.text.value;
    }

    let value = {
        user_answer: get_value(),
    };

    form.onsubmit = function () {
        if (value.user_answer == '') return false;

        postAJAX('/courses/get_answer/', value, function (xhr) {
            window.alert(gradenote[xhr.answer_status]);
            changeQuestion(xhr.new_word, xhr.new_set);
            if (xhr.end_of_study) endingOfStudy();
        }, function (xhr, errmsg, err) {
        });

        complete();
        return false;
    };
}

function showCard(set_mod) {
    modalWrap = document.getElementById('OutCardModal');
    if (ability_to_answer) {
        if (set_mod) {
            document.getElementById('title-card-h5').textContent = "Выбери перевод слова";
            hideEl('answer-field');
            hideEl('btn-to-answer');
            let btns = document.getElementsByClassName("vers-btn");
            for (let i = 0; i < btns.length; i++) {
                btns[i].style.display = '';
                btns[i].onclick = function () {
                    getAnswer(set_mod, btns[i].textContent);
                }
            }
        } else {
            document.getElementById('title-card-h5').textContent = "Напиши перевод слова";
            showEl('answer-field');
            showEl('btn-to-answer');
            let btns = document.getElementsByClassName("vers-btn");
            for (let i = 0; i < btns.length; i++) {
                btns[i].style.display = 'none';
            }
            modalWrap.querySelector('.modal-success-btn').onclick = function () {
                getAnswer(set_mod, "");
            };
        }
    }

    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
}