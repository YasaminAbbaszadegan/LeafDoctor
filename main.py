from flask import Flask
import views

app = Flask(__name__)

# create rule (url)
app.add_url_rule('/','base',views.base,methods=["GET","POST"])

# run the flask app

if __name__ == "__main__":
    app.run(debug=True)
