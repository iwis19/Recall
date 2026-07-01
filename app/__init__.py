from flask import Flask
from flasgger import Swagger

from app.form import *

"""
goal:

- have a terminal page -> like powershell / claude, upload file button on top right, sleek design
- have a normal page -> regular upload, regular answers, etc
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