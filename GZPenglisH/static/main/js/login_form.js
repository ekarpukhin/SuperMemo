$("#Login-button").on("click", function(){
    var login = $("#login_login").val();
    var password = $("#password_login").val();
    if(login == ""){
        $("#errorMessage_login").text("Введите логин");
        return false;
    }
    else if(password == ""){
        $("#errorMessage_login").text("Введите пароль");
        return false;
    }

    $("#errorMessage_login").text("");

    $.ajax({
        url: 'ajax/login_form.php',
        type: "POST",
        cache: false,
        data: {'login': login, 'password': password},
        dataType: "html",
        beforeSend: function() {
            $("#Login-button").prop("disabled", true);
        },
        success: function(data){
            if (data == "Hello") {
                $("#CloseLogin").click();
             } else {
                $("#errorMessage_login").text(data);
             }
            $("#Login-button").prop("disabled", false);
        }
    });

});