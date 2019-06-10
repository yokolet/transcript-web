from flask import Flask
from flask_graphql import GraphQLView
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
from schema import schema

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema))

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
