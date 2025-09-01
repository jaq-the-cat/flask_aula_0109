from flask import Flask
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

import application.routes.index
import application.routes.about