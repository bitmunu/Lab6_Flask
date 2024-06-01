from flask import Flask, render_template, request, redirect, \
    make_response
from random import randint

answers = {
    "hehe":{"he":0, "not hehe": 0, "hehe?": 0},
}
app = Flask(__name__)

voted_users = []
redemption = False

@app.errorhandler(404)
def page_not_found(e):
    return "page not found"

@app.route("/")
@app.route("/questions", methods=["GET", "POST", "DIALOG"])
def show_questions():
    if "voted" in request.cookies and request.cookies["voted"] in voted_users:
        return render_template("changes.html")
    else:
        return render_template("questions.html")


@app.route("/results", methods=["GET", "POST"])
def process_results():
    #(print(request.form))
    if request.method == "GET":
        return render_template("answers.html", answers=answers)

    if request.method == "POST":
        if "voted" in request.cookies and request.cookies["voted"] in voted_users:
            return render_template("changes.html")

        if "hehe" in request.form:
            if request.form["hehe"] == "hehe x1":
                answers["hehe"]["he"]+=1
            elif request.form["hehe"] == "no":
                answers["hehe"]["not hehe"]+=1
            elif request.form["hehe"] == "hehe?":
                answers["hehe"]["hehe?"]+=1
            elif request.form["hehe"] == "hehe x2":
                answers["hehe"]["he"]+=2
            elif request.form["hehe"] == "hehe x3":
                answers["hehe"]["he"]+=3

        response = make_response(redirect("/results"))
        x = randint(1, 1_000_000_000)
        s = str(x)
        voted_users.append(s)
        response.set_cookie("voted", s)
        return response


@app.route("/pepegas", methods=["GET","POST","DIALOG"])
def no_not_again():

    request.cookies.to_dict().pop("voted")
    voted_users.clear()
    print(request.cookies.to_dict())
    print(voted_users)
    answers["hehe"]["he"]=0
    answers["hehe"]["hehe?"]=0
    answers["hehe"]["not hehe"]=0


    return render_template("questions.html")


app.run(host="127.0.0.1", port=5000)
