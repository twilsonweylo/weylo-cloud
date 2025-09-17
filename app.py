from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_message = request.form.get("message")
        # For now, just echo back the message
        reply = f"You said: {user_message}"
        return render_template("index.html", reply=reply)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
