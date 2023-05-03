from flask import Flask
from graphql_server.flask import GraphQLView
from schema import schema

# Importing this view so Flask can delegate to Graphene
app=Flask(__name__)

# Adding a single route for /
@app.route("/")
def index():    
    return "Hello There"

app.add_url_rule(
     '/graphql',
     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))