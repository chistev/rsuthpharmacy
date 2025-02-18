document.addEventListener("DOMContentLoaded", function () {
    var button = document.getElementById("back-to-top");

    // Show/hide button on scroll
    window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
            button.style.display = "block";
        } else {
            button.style.display = "none";
        }
    });

    // Smooth scroll to top
    button.addEventListener("click", function (e) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
});
