from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Redirect to the URL http://example.com
    return redirect('https://6054062e-c1b3-4781.gradio.live')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)

