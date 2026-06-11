document.addEventListener("DOMContentLoaded", function () {

    const modal = document.getElementById("createChatModal");
    const openBtn = document.getElementById("openModal");
    const closeBtn = document.querySelector(".close-modal");
    const cancelBtn = document.querySelector(".btn-cancel");

    if (openBtn) {
        openBtn.addEventListener("click", function () {
            modal.style.display = "flex";
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }

    if (cancelBtn) {
        cancelBtn.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }

    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

});

document.addEventListener("DOMContentLoaded", function () {
    
    const socket = io();

    
    socket.on("new_chat", function (data) {
        const list = document.querySelector(".sidebar-cards-list");

        const card = document.createElement("div");
        card.classList.add("sidebar-chat-card");
        card.innerHTML = `
            <img src="/static/img/avatar.png.png" class="sidebar-chat-avatar" alt="Chat">
            <div class="sidebar-card-content">
                <div class="sidebar-card-top">
                    <span class="sidebar-chat-name font-semibold">${data.name}</span>
                </div>
                <p class="sidebar-chat-text text-muted">Чат користувача</p>
            </div>
        `;
        list.appendChild(card);
    });
});


function deleteChat() {
    fetch("/delete_chat", { method: "POST" });
}
document.addEventListener("DOMContentLoaded", function () {
    const socket = io();

    socket.on("chat_deleted", function (data) {
        const list = document.querySelector(".sidebar-cards-list");
        const card = list.querySelector(".sidebar-chat-card");
        if (card) {
            card.remove();
            window.location.reload();
        }
    });
});

