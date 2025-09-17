from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message", "")
    reply = f"You said: {user_message}"
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
