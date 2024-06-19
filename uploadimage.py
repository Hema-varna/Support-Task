from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def upload_form():
    return render_template('upload.htm')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return redirect(url_for('show_image_name', filename=filename))
    return redirect(request.url)

@app.route('/image/<filename>')
def show_image_name(filename):
    return render_template('display.htm', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)




