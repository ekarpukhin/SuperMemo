<?php
    $login = $_POST["login"];
    $password = $_POST["password"];
    $users_data = array(
        "vanya22124" => "qwerty",
        "admin" => "admin",
    );
    if ($users_data[$login] == $password){
        echo "Hello";
    }
    else{
        echo "Wrong password";
    }
?>