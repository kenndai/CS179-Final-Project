import os, manifest_parser, problem, a_star

from more_itertools import consecutive_groups

from sqlalchemy import false, true

from flask import Flask, redirect, render_template, request, url_for, jsonify, Response
from werkzeug.utils import secure_filename
from handle_log import *

ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)

# global variables
filename = "test_2.txt"
condensedManifest = []
ship = None
balance_pressed = false
load_list = []

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
            global filename
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
        #balance button was pressed
        global ship

        json = request.get_json()

        if json == "balance pressed":

            global balance_pressed
            balance_pressed = true
            
            steps = a_star.get_steps(a_star.a_star(ship))

            return jsonify(steps)
        #load button was pressed
        #elif request.form["num-containers"] != "":
        #    # retrieve container_count but also container arr values
        #    container_str = request.form["num-containers"]
        #    load_list = parseContainerStr(container_str)
        #    for x in load_list:
        #        print(x)

        #    #return ('', 204)
        #    return jsonify(load_list)
        elif isinstance(json, dict):
            # call function to get coordinates based on weight
            # add container to grid
            # return coordinates for that container
            return jsonify([5, 6])
        else:
            # get "name" attribute from input
            request_form_key = list(request.form.keys())[0]

            #looks up function to call for given request_form_key
            post_dict[request_form_key](request.form[request_form_key])
            data = [{'filename': filename[:-4]}]
            return render_template("index.html", data)
    
    else:
        #code runs here when continue button pressed
        global condensedManifest

        condensedManifest = manifest_parser.parse(filename)
        print(condensedManifest)
        ship = problem.ShipProblem(grid=condensedManifest)

        #print(filename)
        data = [{'filename': filename[:-4]}]
        return render_template("index.html", data=data)

def parseContainerStr(str):
    arr = [x.strip() for x in str.split(',')]

    return arr

# this route runs when mainpage is loaded for the first time
@app.route("/main-manifest-loaded", methods=["GET"])
def send_manifest_to_main_page():
    return jsonify(condensedManifest)

# this route runs when balance button pressed
@app.route("/balance", methods=["POST", "GET"])
def balance():
    # balance button was pressed
    if request.form["balance-btn"] == "Balance":
        global balance_pressed
        balance_pressed = true
        steps = a_star.get_steps(a_star.a_star(ship))
        return render_template("index.html", data=steps)

if __name__ == "__main__":
    app.run(debug=True)