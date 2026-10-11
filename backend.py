import json
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def login():
    s=None
    if(request.method=="POST"):
        a=str(request.form.get("username"))
        b=str(request.form.get("password"))
                
        with open("user_data.json","r") as file:
            content=json.load(file)

        user_found=False
        for user in content:
            if user["username"]==a:
                user_found=True
                if user["password"]==b:
                    return render_template("index.html",s="Login Successfull")
                else:
                    return render_template("index.html",s="incorrect password")


        if(user_found==False):
            return render_template("index.html",s="username doesn't exist")

    return render_template("index.html",s=None)
    


if __name__=="__main__":
    app.run(debug=True)