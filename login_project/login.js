// szukamy elementów formularza na stronie i przypisujemy je do zmiennych 
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

// czekamy na kliknięcie przycisku logowania
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    // pobieramy wartości wpisane w pola formularza
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    // sprawdzamy czy hasło i login jest prawidłowe
    if (username === "" && password === "") {
        // wyświetlamy alert jeśli się powiodło
        alert("You have successfully logged in.");
        location.reload();
    } else {
        // zmieniamy opacity błędu na 1, aby był widoczny
        loginErrorMsg.style.opacity = 1;
    }
})