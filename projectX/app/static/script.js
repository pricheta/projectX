const loginButton = document.getElementById("loginButton");

loginButton.addEventListener("click", function() {
    const username = $("#username").val();
    const password = $("#password").val();

    if (!username || !password) {
        alert("Пожалуйста, заполните все поля!");
        return;
    }

    const data = {
        login: username,
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
        error: function(response) {
            alert(response);
        }
    });
});