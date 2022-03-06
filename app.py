from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def landing():
    if request.method == "POST":
        user = request.form["name"]
        print(user)
        return redirect(url_for("manifest_input"))
    else:
        return render_template("landing-page.html")

@app.route("/manifest-input", methods=["POST", "GET"])
def manifest_input():
    return render_template("manifest-input.html")

@app.route("/main")
def main_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)