document.addEventListener("DOMContentLoaded", function () {
    const liveClock = document.getElementById("liveClock");

    function updateClock() {
        if (!liveClock) return;

        const now = new Date();
        const time = now.toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit"
        });

        liveClock.textContent = time;
    }

    updateClock();
    setInterval(updateClock, 1000);
});