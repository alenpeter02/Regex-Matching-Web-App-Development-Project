from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.finditer(regex_pattern, test_string)
    matches_info = [{'match': match.group(), 'position': match.start()} for match in matches]
    num_matches = len(matches_info)
    return render_template ('index.html', 
                           test_string=test_string, 
                           regex=regex_pattern, 
                           matches=matches_info, 
                           num_matches=num_matches,
                           test_string_length=len(test_string))

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = validate_email_regex(email)
    return jsonify({'is_valid': is_valid})

def validate_email_regex(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
