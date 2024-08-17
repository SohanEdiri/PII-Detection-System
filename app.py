from flask import Flask, request, render_template, redirect, url_for
import joblib
import re
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)  

# Load the PII detection model
model = joblib.load('pii_detection_model.pkl')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def replace_pii(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_pattern = re.compile(r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b')
    name_pattern = re.compile(r'\b[A-Z][a-z]* [A-Z][a-z]*\b')
    address_pattern = re.compile(r'\b\d+ [A-Z][a-z]* [A-Z][a-z]*\b')

    text = re.sub(email_pattern, '<span class="pii">[PII]</span>', text)
    text = re.sub(phone_pattern, '<span class="pii">[PII]</span>', text)
    text = re.sub(name_pattern, '<span class="pii">[PII]</span>', text)
    text = re.sub(address_pattern, '<span class="pii">[PII]</span>', text)
    
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            file_path = os.path.join('uploads', secure_filename(file.filename))
            file.save(file_path)

            with open(file_path, 'r') as f:
                content = f.read()

            processed_content = replace_pii(content)

            return render_template('result.html', original=content, processed=processed_content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
