var counter = 0;
function darkMode() {
    let Darkmode;
    let lightmode;

    if (counter % 2 == 0) {
        Darkmode = document.getElementById("color");
        Darkmode.style.backgroundColor = "black";
        Darkmode.style.color = "white";
        Dark.innerHTML="Light Mode";
    }
    else {
        lightmode = document.getElementById("color");
        lightmode.style.backgroundColor = "white";
        lightmode.style.color = "black";
        dark.innerHTML="Dark Mode";
    }
    counter++;
}

