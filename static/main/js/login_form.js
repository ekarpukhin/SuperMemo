let modalWrap = null;

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

    function complete() {
        document.onkeydown = null;
    }

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
            // window.alert(xhr.status + "\n" + xhr.responseText)
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