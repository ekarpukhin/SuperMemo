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
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const getLoginInformation = () => {
    let form = document.getElementById("login-form");
    let json_return = null;

    form.onsubmit = function () {
        let value = {
            login: form.login_login.value,
            password: form.password_login.value
        };
        if (value.login == '' || value.password == '') return false;

        $.ajax({
            url: '/userpage/get_logininfo/',
            method: "POST",
            dataType: "json",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
            },
            data: {
                login: value.login,
                password: value.password
            },
        }).done(function (xhr) {
            if (typeof xhr.responseText == "string"
                && (xhr.responseText == "login incorrect" || xhr.responseText == "password incorrect")) {
                window.alert(xhr.status + ": " + xhr.responseText)
            } else location.reload();
            json_return = xhr;

        }).fail(function (xhr, errmsg, err) {
            // window.alert(xhr.status + ": " + xhr.responseText);
        });

        complete();
        return false;
    }

    return json_return;
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
        $.ajax({
            url: '/userpage/get_logout/',
            method: "POST",
            dataType: "json",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
            },
            data: {
                logout: true
            },
        }).done(function (xhr) {
            //window.alert(xhr.status + ": " + xhr.responseText);
            location.reload();
        }).fail(function (xhr, errmsg, err) {
            // window.alert(xhr.status + ": " + xhr.responseText);
        });

        complete();
        return false;
    }
}

const getSignUpInformation = () => {
    let form = document.getElementById("signup-form");
    let json_return = null;

    form.onsubmit = function () {
        let value = {
            name: form.name_signup.value,
            login: form.login_signup.value,
            password: form.password_signup.value
        };
        if (value.login == '' || value.password == '' || value.name == '') return false;

        $.ajax({
            url: '/userpage/get_signup/',
            method: "POST",
            dataType: "json",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
            },
            data: {
                name: value.name,
                login: value.login,
                password: value.password
            },
        }).done(function (xhr) {
            if (typeof xhr.responseText == "string"
                && (xhr.responseText == "login duplicate" || xhr.responseText == "password incorrect")) {
                window.alert(xhr.status + ": " + xhr.responseText)
            } else location.reload();
            json_return = xhr;

        }).fail(function (xhr, errmsg, err) {
            // window.alert(xhr.status + ": " + xhr.responseText);
        });

        complete();
        return false;
    }

    return json_return;
}

function showSignUp() {
    modalWrap = document.getElementById("SignUpModal");
    modalWrap.querySelector(".btn-success").onclick = function () {
        getSignUpInformation();
    };

    let modal = new bootstrap.Modal(modalWrap.querySelector('.modal'));
    modal.show();
}
