const loginButton = document.getElementById("loginButton");

loginButton.addEventListener("click", function() {
    const login = $("#login").val();
    const password = $("#password").val();

    if (!login || !password) {
        alert("Пожалуйста, заполните все поля!");
        return;
    }

    const data = {
        login: login,
        password: password
    };

    $.ajax({
        url: "http://127.0.0.1:8000/auth/get_access_token/",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function(response) {
            alert(response);
        },
        error: function(xhr, status, error) {
            alert("Произошла ошибка: " + error);
        }
    });
});