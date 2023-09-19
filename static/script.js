
document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("email-input");
    const suggestionBox = document.getElementById("suggestion-box");

    emailInput.addEventListener("input", function () {
        const email = emailInput.value;
        const isValid = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email); // Basic email format validation

        if (!isValid) {
            suggestionBox.style.display = "block";
            suggestionBox.innerHTML = "Invalid email format. Please use example@example.com format.";
        } else {
            suggestionBox.style.display = "none";
            suggestionBox.innerHTML = "";
        }
    });
});
var pass1 = document.getElementById("pass1")
var pass2 = document.getElementById("pass2")
function clicked1() {

    if (pass1.type === 'password') {
        pass1.type = 'type'
    }
    else {
        pass1.type = 'password'

    }
}
function clicked2() {
    if (pass2.type === 'password') {
        pass2.type = 'text'
    }
    else {
        pass2.type = "password"

    }
}
