from flask import Flask
from flasgger import Swagger

from app.form import *

"""
goal:

- use this temp rag system to test things out for now, features will be a research papers rag search + relation nodes
"""

"""
1. create a form to upload context file
2. create a form to submit text questions to ask about yourself
3. implement ui
"""

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024 # 16 mb
app.config['SECRET_KEY'] = 'hahatemporarysecretkey'

Swagger(app)

from app import routes

# use: flask --app app:app --debug run