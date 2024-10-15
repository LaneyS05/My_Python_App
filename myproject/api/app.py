from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask on Vercel!"

def handler(event, context):
    return app(event, context)
