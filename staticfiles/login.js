document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.querySelector(".container form");

    if (loginForm) {
        loginForm.addEventListener("submit", function (e) {
            const username = loginForm.querySelector("input[name='username']").value;
            const password = loginForm.querySelector("input[name='password']").value;

            if (username === "" || password === "") {
                alert("Please fill in all fields.");
                e.preventDefault(); // Prevent only if fields are empty
            } else {
                console.log("Form submitted!"); // Debugging step
            }
        });
    }
});
