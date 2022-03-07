from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def landing_page():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("manifest_input_page"))
    else:
        return render_template("landing-page.html")

@app.route("/manifest-input", methods=["POST", "GET"])
def manifest_input_page():
    if request.method == "POST":
        print(request.form)
        if "manifest-continue" in request.form:
            return redirect(url_for("main_page"))
        elif "manifest-quit" in request.form:
            return redirect(url_for("landing_page"))
    else:
        return render_template("manifest-input.html")

@app.route("/main")
def main_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)