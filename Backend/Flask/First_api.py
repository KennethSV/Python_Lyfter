from flask import Flask, jsonify, request, Response, json

app = Flask(__name__)

shows_list = [
    {
        "title": "3 Body Problem",
        "genre": "Sci-Fi",
    },
    {
        "title": "Severance",
        "genre": "Thriller",
    },
    {
        "title": "Black Knight",
        "genre": "Sci-Fi",
    },
]

comments_list = [
    "Genial video, entendí todo a la perfeccion!",
    "Me encantó el intro jajaja",
]

users_list = [
	{
		"email": "action.bronson@gmail.com",
		"password": "123@a!",
	},
]

@app.route("/")
def root():
    print("Hola pillo")
    return "<h1>Hello, World!</h1"

@app.route("/productos")
def productos():
    return {
        "Cheesecake": "Vasco",
        "Cheesecake2": "Clasico",
    }

@app.route("/login", methods=["GET", "POST"])
def login():
    request = Flask.request_class
    if request.method == "POST":
        return "do_the_login()"
    else:
        return "show_the_login_form()"

@app.route("/user/<username>")
def profile(username):
    return f"{username}\'s profile"

@app.route("/shop/<category>/<subcategory>/all")
def products_subcategory(category, subcategory):
    return f"Shopping category {category}, {subcategory}"

@app.route("/shows")
def shows():
    filtered_shows = shows_list
    genre_filter = request.args.get("genre")
    if genre_filter:
        filtered_shows = list(
            filter(lambda show: show["genre"] == genre_filter, filtered_shows)
        )

    return {"data": filtered_shows}

@app.route("/echo", methods=["POST"])
def echo():
    request_body = request.json
    return {"request_body": request_body}

@app.route("/comment", methods=["POST"])
def post_comment():
    comment_content = request.form.get("comment_content")
    if not comment_content:
        return jsonify(message="no empty comments allowed"), 400
    
    comments_list.append(comment_content)
    return comments_list

@app.route("/register", methods=["POST"])
def register_user():
    try:
        if "email" not in request.json:
            raise ValueError("email missing from the body")

        if "password" not in request.json:
            raise ValueError("password missing from the body")

        users_list.append(
            {
                "email": request.json["email"],
                "password": request.json["password"],
            }
        )
        return users_list
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
		    # enviar un mensaje por slack
        return jsonify(message=str(ex)), 528

@app.route('/view-token')
def view_token():
	token = request.headers.get('token', '')
	return token

@app.route("/hello")
def hello():
    response_body = json.dumps({"msg": "Hello World!"})
    return Response(response_body, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host="localhost", port=8001, debug=True)