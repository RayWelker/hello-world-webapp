import sys

try:
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!\n"

    if __name__ == "__main__":
        app.run(port=80)

except ImportError:
    sys.exit("""Install requirements from requirements.txt 'pip3 install -r requirements.txt'""")
