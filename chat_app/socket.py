from .views import *


@socketio.on("connect_chat")
def handle_connect_chat(data):
    group_id = data.get("group_id")
    group = Group.query.get(group_id)
    if group:
        join_room(f"chat_{group_id}")
        socketio.emit("chat_connected", {"group_id": group_id})


@socketio.on("send_message")
def handle_send_message(data):
    text = data.get("text")
    group_id = data.get("group_id")
    if not text or not group_id:
        return
    msg = Message(text=text, user_id=current_user.id, group_id=group_id)
    DATA_BASE.session.add(msg)
    DATA_BASE.session.commit()
    socketio.emit("new_message", {"id": msg.id, "text": msg.text, "user_id": msg.user_id, "group_id": msg.group_id}, room=f"chat_{group_id}")