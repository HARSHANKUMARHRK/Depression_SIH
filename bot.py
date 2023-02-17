from flask import Flask, render_template, request
import os
import openai
import gradio as gr

from chatgpt import chatgpt_clone

app = Flask(__name__)

openai.api_key = "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"

@app.route('/')
def home():
    prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
    return render_template('bot.html', prompt=prompt)

@app.route('/process', methods=['POST'])
def process():
    message = request.form['message']
    state = request.form.getlist('state[]')
    history, _ = chatgpt_clone(message, state)
    response = history[-1][1]
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)


    