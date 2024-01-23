from dotenv import load_dotenv

from flask_app.factory import create_flask_app

load_dotenv()

app = create_flask_app()  # Automatically ran when using `flask run` command
