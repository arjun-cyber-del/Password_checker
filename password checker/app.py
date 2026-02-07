from flask import Flask, render_template,request, jsonify
import re 
app = Flask(__name__)
def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score +=1
    if re.search("[A-Z]",password):
        score +=1
    if re.search("[a-z]",password):
        score +=1
    if re.search("[0-9]",password) :
        score +=1
    if re.search("[!@#$%&^*]",password):
        score +=1


    if score <= 2:
        return "weak password stupid"
    elif score == 3:
        return " ok mhann"
    else:
        return "good password bro"

@app.route("/") 
def home():
     return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data["password"]
    result = check_password_strength(password)
    return jsonify({"strength": result})

if __name__ == "__main__":
    app.run(debug=True)
