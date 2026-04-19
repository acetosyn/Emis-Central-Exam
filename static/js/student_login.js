document.addEventListener("DOMContentLoaded", function () {
    const menuLink = document.querySelector(".menu-link");
    const menu = document.getElementById("menu");
    const togglePassword = document.getElementById("togglePassword");
    const passwordInput = document.getElementById("password");
    const togglePasswordIcon = document.getElementById("togglePasswordIcon");

    document.documentElement.classList.add("js");

    if (menuLink && menu) {
        menuLink.addEventListener("click", function (e) {
            e.preventDefault();
            menu.classList.toggle("active");
        });
    }

    if (togglePassword && passwordInput && togglePasswordIcon) {
        togglePassword.addEventListener("click", function () {
            const isPassword = passwordInput.getAttribute("type") === "password";
            passwordInput.setAttribute("type", isPassword ? "text" : "password");
            togglePasswordIcon.className = isPassword ? "fa fa-eye-slash" : "fa fa-eye";
        });
    }
});