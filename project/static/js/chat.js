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
    let currentChatId = null;

    
    document.querySelectorAll(".sidebar-chat-card").forEach(card => {
        card.addEventListener("click", function () {
            const groupId = this.dataset.groupId;
            currentChatId = groupId;
            socket.emit("connect_chat", { group_id: groupId });

            
            const history = document.querySelector(".chat-history");
            history.innerHTML = "";

            
            fetch(`/messages/${groupId}`)
                .then(res => res.json())
                .then(messages => {
                    messages.forEach(msg => {
                        const msgDiv = document.createElement("div");
                        msgDiv.classList.add("message");
                        msgDiv.innerHTML = `
                            <img src="/static/img/avatar.png.png" class="avatar" alt="avatar">
                            <div>
                                <div class="message-header">
                                    <span class="author">${msg.username}</span>
                                    <span class="time">${msg.created_at}</span>
                                </div>
                                <div class="message-text">${msg.text}</div>
                            </div>
                        `;
                        history.appendChild(msgDiv);
                    });
                    history.scrollTop = history.scrollHeight; 
                });
        });
    });

   
    const sendBtn = document.querySelector(".send-btn");
    if (sendBtn) {
        sendBtn.addEventListener("click", function () {
            const input = document.querySelector(".write-message");
            const text = input.value.trim();
            if (text && currentChatId) {
                socket.emit("send_message", { text: text, group_id: currentChatId });
                input.value = "";
            }
        });
    }

    
    socket.on("new_message", function (data) {
        console.log("Got new_message:", data);
        if (data.group_id == currentChatId) {
            const history = document.querySelector(".chat-history");
            const msgDiv = document.createElement("div");
            msgDiv.classList.add("message");
            msgDiv.innerHTML = `
                <img src="/static/img/avatar.png.png" class="avatar" alt="avatar">
                <div>
                    <div class="message-header">
                        <span class="author">${data.username || "User " + data.user_id}</span>
                        <span class="time">${data.created_at || new Date().toLocaleTimeString()}</span>
                    </div>
                    <div class="message-text">${data.text}</div>
                </div>
            `;
            history.appendChild(msgDiv);
            history.scrollTop = history.scrollHeight; 
        }
    });

    
    socket.on("new_chat", function (data) {
        const list = document.querySelector(".sidebar-cards-list");

        const card = document.createElement("div");
        card.classList.add("sidebar-chat-card");
        card.dataset.groupId = data.id;
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

       
        card.addEventListener("click", function () {
            const groupId = this.dataset.groupId;
            currentChatId = groupId;
            socket.emit("connect_chat", { group_id: groupId });

            const history = document.querySelector(".chat-history");
            history.innerHTML = "";

            fetch(`/messages/${groupId}`)
                .then(res => res.json())
                .then(messages => {
                    messages.forEach(msg => {
                        const msgDiv = document.createElement("div");
                        msgDiv.classList.add("message");
                        msgDiv.innerHTML = `
                            <img src="/static/img/avatar.png.png" class="avatar" alt="avatar">
                            <div>
                                <div class="message-header">
                                    <span class="author">${msg.username}</span>
                                    <span class="time">${msg.created_at}</span>
                                </div>
                                <div class="message-text">${msg.text}</div>
                            </div>
                        `;
                        history.appendChild(msgDiv);
                    });
                    history.scrollTop = history.scrollHeight;
                });
        });
    });

    
    socket.on("chat_deleted", function (data) {
        const list = document.querySelector(".sidebar-cards-list");
        const card = list.querySelector(`.sidebar-chat-card[data-group-id="${data.id}"]`);
        if (card) {
            card.remove();
            window.location.reload();
        }
    });
});


function deleteChat() {
    fetch("/delete_chat", { method: "POST" });
}



