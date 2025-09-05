from flask import Flask, request, redirect, render_template, send_from_directory

app = Flask(__name__, static_folder="static", template_folder="templates")

PRIMARY_HOST = "weylo.ai"   # switch to "www.weylo.ai" if you prefer www as primary

@app.before_request
def force_primary_host_and_https():
    host = request.headers.get("Host", "")
    # Force primary host
    if host and host.lower() != PRIMARY_HOST:
        return redirect(f"https://{PRIMARY_HOST}{request.full_path}", code=301)
    # Force https if Render ever hits http (belt + suspenders)
    if request.headers.get("X-Forwarded-Proto", "https") != "https":
        return redirect(f"https://{PRIMARY_HOST}{request.full_path}", code=301)

@app.route("/")
def home():
    return render_template("index.html")

# Optional: serve robots.txt and favicon
@app.route("/robots.txt")
def robots():
    return send_from_directory(app.static_folder, "robots.txt")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, "favicon.ico")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
