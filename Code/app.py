from flask import Flask, render_template, request

import model as md
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

#Allowing the user to upload
@app.route('/', methods=['POST'])
def predict():
    #We need to be able to get the image, save it into a folder and do all of the preprocessing
    #To get the image we need to access it using the name that we used in the HTML
    imagefile=request.files['imagefile']
    #After getting the image uploaded by the used, we need to be able to save it
    image_path="./images/" + imagefile.filename
    imagefile.save(image_path)
    #We need to be able to ADD the model: we want to load the model and then we past the image or the text to the model

    #Load the model

    classification = md.modelVgg(image_path)
    return render_template('index.html', prediction= classification)

if __name__ == '__main__':
    app.run(port=3000, debug=True)