function checkPassword() {
    const password = document.getElementById("password").value;

    fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password })
    })
    .then(res => res.json())
    .then(data => {
        let text = `Strength: ${data.strength}`;
        if (data.feedback?.length) {
            text += "\nSuggestions:\n- " + data.feedback.join("\n- ");
        }
        document.getElementById("result").innerText = text;
    });
}
