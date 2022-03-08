from flask import Flask, redirect, render_template, request, url_for
from handle_log import *

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def landing_page():
    if request.method == "POST":
        username = request.form["name"]
        if username == "":
            return render_template("landing-page.html")
        else:
            log(f"{username} signs in")
            return redirect(url_for("manifest_input_page"))
    else:
        return render_template("landing-page.html")

@app.route("/manifest-input", methods=["POST", "GET"])
def manifest_input_page():
    if request.method == "POST":
        if "manifest-continue" in request.form:
            return redirect(url_for("main_page"))
        elif "manifest-quit" in request.form:
            return redirect(url_for("landing_page"))
    else:
        return render_template("manifest-input.html")

@app.route("/main", methods=["POST", "GET"])
def main_page():
    if request.method == "POST":
        # get "name" attribute from input
        request_form_key = list(request.form.keys())[0]

        #looks up function to call for given request_form_key
        post_dict[request_form_key](request.form[request_form_key])

        return render_template("index.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)