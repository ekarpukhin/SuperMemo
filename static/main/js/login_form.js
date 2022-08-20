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

const getLoginInformation = () => {
    let form = document.getElementById("login-form");

    form.onsubmit = function () {
        let value = {
            login: form.login_login.value,
            password: form.password_login.value
        };
        if (value.login == '' || value.password == '') return false;

        postAJAX('/userpage/get_logininfo/', value, function (xhr) {
            window.alert(xhr.status + ": " + xhr.responseText)
            if (typeof xhr.responseText == "string"
                && (xhr.responseText == "login incorrect" || xhr.responseText == "password incorrect")) {
                window.alert(xhr.status + ": " + xhr.responseText)
            } else location.reload();
        }, function (xhr, errmsg, err) {});

        complete();
        return false;
    }
}

const getSignUpInformation = () => {
    let form = document.getElementById("signup-form");

    form.onsubmit = function () {
        let value = {
            name: form.name_signup.value,
            login: form.login_signup.value,
            password: form.password_signup.value
        };
        if (value.login == '' || value.password == '' || value.name == '') return false;

        postAJAX('/userpage/get_signup/', value, function (xhr) {
            if (typeof xhr.responseText == "string"
                && (xhr.responseText == "login duplicate" || xhr.responseText == "password incorrect")) {
                window.alert(xhr.status + ": " + xhr.responseText)
            } else location.reload();
        }, function (xhr, errmsg, err) {});

        complete();
        return false;
    }
}

function showLogin() {
    modalWrap = document.getElementById("LoginModal");
    modalWrap.querySelector(".btn-success").onclick = function () {
        getLoginInformation();
    };

    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
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

function logout() {
    document.getElementById("logout-form").onsubmit = function () {
        postAJAX('/userpage/get_logout/', {logout: true}, function (xhr) {
            location.reload();
        }, function (xhr, errmsg, err) {});

        complete();
        return false;
    }
}

function showSignUp() {
    modalWrap = document.getElementById("SignUpModal");
    modalWrap.querySelector(".btn-success").onclick = function () {
        getSignUpInformation();
    };

    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
}
