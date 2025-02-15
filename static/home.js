document.addEventListener("DOMContentLoaded", function () {
    const btn = document.querySelector(".btn");

    btn.addEventListener("mouseover", function () {
        btn.style.boxShadow = "0px 4px 10px rgba(0, 0, 0, 0.2)";
    });

    btn.addEventListener("mouseout", function () {
        btn.style.boxShadow = "none";
    });

    // Smooth scroll effect when clicking "Get Started"
    btn.addEventListener("click", function (event) {
        event.preventDefault(); 
        window.location.href = btn.getAttribute("href");
    });
});
