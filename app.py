from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

# global variables

@app.route("/", methods=["POST", "GET"])
def landing_page():
    if request.method == "POST":
        user = request.form["name"]
        if user == "":
            return render_template("landing-page.html")
        else:
            #log file record the name of login and date
            return redirect(url_for("manifest_input_page"))
    else:
        return render_template("landing-page.html")

@app.route("/manifest-input", methods=["POST", "GET"])
def manifest_input_page():
    if request.method == "POST":
        
        f = request.files['manifest']
        print(f)
        if f != "":
            return render_template("index.html")
        else:
            #read in file
            return redirect(url_for("main_page"))
    else:
        return render_template("manifest-input.html")

@app.route("/main", methods=["POST", "GET"])
def main_page():
    if request.method == "POST":
        file_name = request.get_json()
        if file_name == "":
            print("empty")
            return render_template("manifest-input.html")
        else:
            #read in file
            print(file_name)
            return render_template("index.html")
    else:
        return render_template("manifest-input.html")

if __name__ == "__main__":
    app.run(debug=True)