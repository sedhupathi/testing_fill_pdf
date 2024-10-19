from flask import Flask, render_template, request, send_file
from fillpdf import fillpdfs
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from the form
    form_data = {
        "name": request.form.get('name'),
        "gender": request.form.get('gender'),
        "maritalStatus": request.form.get('maritalStatus'),
        "email": request.form.get('email'),
        "phone": request.form.get('phone'),
        "country": request.form.get('country'),
        "state": request.form.get('state'),
    }
    
    # Path to your fillable PDF form
    template_path = 'template.pdf'
    output_path = 'output.pdf'
    
    # Map the form data to the fields in the PDF form
    data_dict = {
        'Name': form_data['name'],
        'Gender': form_data['gender'],
        'MaritalStatus': form_data['maritalStatus'],
        'Email': form_data['email'],
        'Phone': form_data['phone'],
        'Country': form_data['country'],
        'State': form_data['state'],
    }
    
    # Fill in the PDF using fillpdfs
    fillpdfs.write_fillable_pdf(template_path, output_path, data_dict)
    
    # Return the generated PDF as a download
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    # Set up the app to run in debug mode
    app.run(debug=True)
