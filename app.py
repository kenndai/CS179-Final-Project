import os
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from handle_log import *

ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)

# global variables

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
        file = request.files['manifest']
        print(file.filename)
        if file.filename == "":
            print("no file selected")
            return render_template("manifest-input.html")
        elif file and allowed_file(file.filename):
            #save file to data folder
            filename = secure_filename(file.filename)
            file.save(os.path.join("data", filename))
            return redirect(url_for("main_page"))
        else:
            print("file selected must be .txt file")
            return render_template("manifest-input.html")
    else:
        return render_template("manifest-input.html")

#helper function for checking if extension is allowed
#https://www.tutorialspoint.com/flask/flask_file_uploading.htm
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/main", methods=["POST", "GET"])
def main_page():
    if request.method == "POST":
        # get "name" attribute from input
        request_form_key = list(request.form.keys())[0]

        #looks up function to call for given request_form_key
        post_dict[request_form_key](request.form[request_form_key])

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)