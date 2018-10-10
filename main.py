from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form below -->
        <form action="/" method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit">
        </form>
      <!-- create your form above -->
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotate_amount = int(request.form["rot"])
    plain_text = request.form["text"]
    
    encrypted_string = rotate_string(plain_text, rotate_amount)
    return form.format(encrypted_string)

@app.route("/")
def index():
    return form.format("")

app.run()