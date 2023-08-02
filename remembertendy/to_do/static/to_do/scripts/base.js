const navbar_deactivate = () => {
    document.querySelector(".toggle-navbar").classList.remove("toggle-navbar-active")
}

const navbar_activate = () => {
    document.querySelector(".toggle-navbar").classList.add("toggle-navbar-active")
}

document.querySelector("#icon").addEventListener("click", navbar_activate)
document.querySelector(".prof-icon").addEventListener("click", navbar_deactivate)
