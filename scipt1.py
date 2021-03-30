from flask import Flask, render_template
# handles requests, render template accesses html files to render them depending on route
app=Flask(__name__)
# instantiating that class object
@app.route('/')
# home page route
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)