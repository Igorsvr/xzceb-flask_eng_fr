from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    # return "Translated text to French"
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # return "Translated text to English"
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
