from .database import *
from app import *


@app.route('/')
def hello_world():  # put application's code here
    return render_template("")
