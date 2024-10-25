from flask import Flask, redirect, render_template, request
import sqlite3

def db():
    conn=sqlite3.connect("C:\\Users\\rakes\\records-of-failure\\marks.db")
    return conn


app=Flask(__name__)

# @app.route("/")
# def home():
#     user={"name":"prateek"}
#     return render_template("form.html",user=user)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit_marks", methods=['POST','GET'])
def submission():

    if request.method=='POST':
        subject= request.form['subject']
        marks= request.form['marks']
        name= request.form['name']
        data=([name,marks,subject])

        cur=db().cursor()
        try:
            cur.execute("insert into marks values (?,?,?)",data)
            db().commit()
        except:
            return("error")
        print(data)
        return render_template("submitted.html")
    
@app.route("/next_action", methods=['POST','GET'])
def page():

    if request.method=='POST':
        val=request.form['next_action']
        if val=="sd":
            return redirect("/")
        else:
            return redirect("/result")

@app.route("/result", methods=['GET'])
def table():
    cur=db().cursor()
    rows=cur.execute("select * from marks").fetchall()
    return render_template("display.html", rows=rows)

if (__name__)=="__main__":
    app.run(debug=True)





# return render_template("submitted.html")


