import os
import json
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
import aiofiles
import asyncio
from fungsi import *
import requests
import asyncio

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/reset")
def reset():
    reset_history()
    return "Reset Success"

@app.route("/chat", methods=["POST"])
async def chat():
    message = request.json.get("message", "")
    chat = chat_ai(message)
    try:
        bot = json.loads(chat)
        messagess = bot.get("message")
        audios = generate_vc(messagess)
        bentar = metadata("output.mp3")
        ekspresi = bot.get("ekspresi")
        animasi = bot.get("animasi")
    except json.JSONDecodeError:
        print("Error bang")
    response_messages = [
        {
            "text": messagess,
            "audio": audios,
            "lipsync": bentar,
            "facialExpression": ekspresi,
            "animation": animasi,
        }
    ]

    return jsonify({"messages": response_messages}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
