const create_deactivate = () => {
    document.querySelector(".create-post").classList.remove("create-post-active")
}

const create_activate = () => {
    document.querySelector(".create-post").classList.add("create-post-active")
}

document.querySelector(".add-post").addEventListener("click", create_activate)
document.querySelector(".cancel-creating-post").addEventListener("click", create_deactivate)