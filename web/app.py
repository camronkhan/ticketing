from flask import Flask
from modules.db import db_session
from modules.apis.v1 import blueprint as api_v1_blueprint

app = Flask(__name__)
app.register_blueprint(api_v1_blueprint)

@app.teardown_appcontext
def cleanup(resp_or_exc):
    """
    This method will be executed when the current application context is torn
    down. This happens after each request. That way we make sure to release the
    resources used by a session after each request.
    """
    db_session.remove()
