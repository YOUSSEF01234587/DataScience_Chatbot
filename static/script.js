/* 
Data Science Chatbot Script (script.js)
- Handles sending user messages to the Flask server
- Receives bot responses via /chat endpoint
- Appends messages to chatbox with proper styling
- Auto-scrolls chat to show latest messages
*/
async function send() {
    const input = document.getElementById("msg");
    const message = input.value.trim();
    if(!message) return;

    addMessage(message, "user");

    const res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message})
    });

    const data = await res.json();
    addMessage(data.reply, "bot");

    input.value = "";
}

function addMessage(text, cls){
    const box = document.getElementById("chatbox");
    const div = document.createElement("div");
    div.className = cls;
    div.innerText = text;
    box.appendChild(div);


    box.scrollTop = box.scrollHeight;
}