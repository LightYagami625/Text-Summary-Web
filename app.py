import flask
from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from model.model import summarize_text

app = flask.Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.form.get("text")
    length_choice = request.form.get("max_length")
    if length_choice == "smaller":
        max_length = 120
        min_length = 40
    elif length_choice == "medium":
        max_length = 250
        min_length = 80
    else:
        max_length = 300
        min_length = 150
    return flask.Response(
        flask.stream_with_context(summarize_text(model=model, tokenizer=tokenizer, text=data, min_length=min_length, max_length=max_length)),
        mimetype='text/plain'
    )

if __name__ == "__main__":
    app.run(debug=True)
