from flask import Flask, render_template, request
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

        cur=db().cursor
        try:
            cur.execute("insert into studmarks values (?,?,?)",data)
            cur.commit()
        except:
            return("error")
        print(data)
        return render_template("submitted.html")
    


if (__name__)=="__main__":
    app.run(debug=True)





# return render_template("submitted.html")


