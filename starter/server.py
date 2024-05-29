from flask import Flask, render_template, url_for, redirect, request



from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary



# cupcake = find_cupcake("cupcakes.csv", "")

app = Flask(__name__)

#@app.route("/endpoint")


    





# @app.route("/")
# def home():
#     return render_template("index.html")



     


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/cupcakes")
def all_cupcakes():
     return render_template("cupcakes.html")

# @app.route("/cupcake_individual")
# def individual_cupcake():
#      return render_template("individual-cupcake.html")

@app.route("/orders")
def order():
     Cupcake = request.args.get('cupcake')

     return render_template("orders.html")





@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."
    






if __name__ == "__main__":
        app.env = "development"
        app.run(debug = True, port = 8000, host = "localhost")