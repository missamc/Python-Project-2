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
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))



@app.route("/cupcakes")
def all_cupcakes():
     return render_template("cupcakes.html", cupcakes=get_cupcakes("cupcakes.csv"))

# @app.route("/cupcake_individual")
# def individual_cupcake():
#      return render_template("individual-cupcake.html")

@app.route("/orders", methods=['POST', 'GET'])
def orders():
    if request.method == "POST":
         add_cupcake = request.form["cupcake"]
         return redirect(url_for("add-cupcake", name=add_cupcake))
    #  Cupcake = request.args.get('cupcake')
    # name = request.form.get('cupcake')

    # cupcake=find_cupcake('cupcakes.csv', name)
    # print(cupcake)
    # print(name)
    else:
        return render_template("orders.html", cupcakes=get_cupcakes("cupcakes.csv"))





@app.route("/add-cupcake", methods=["POST"])
def add_cupcake():
    print(request.form)
    name= request.form['cupcake_name']
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found ", 404
    






if __name__ == "__main__":
        app.env = "development"
        app.run(debug = True, port = 8000, host = "localhost")