
import os
os.environ['FOR_DISABLE_CONSOLE_CTRL_HANDLER'] = '1'
from flask import Flask, request,render_template
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
import time
from scipy import stats
time.sleep(1)
app = Flask('Cancer Detection')
UPLOAD_FOLDER='D:\archive\HAM10000_images_part_1'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Load the model
from tensorflow import keras
model = keras.models.load_model('D:\BeCode\challenge-mole\mole_detection.h5')
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(file1.filename)
         # Get the image and clean the image
        image_size = (224, 224)
        original_image = image.load_img(file1.filename, target_size=image_size)
        # Convert your image pixels to a numpy array of values .
        image_array = image.img_to_array(original_image)
        # Reshape your image dimensions so that the colour channels correspond to what your model expects.
        image_array = image_array.reshape((1, image_array.shape[0], image_array.shape[1], image_array.shape[2]))
        # Preprocess your image with preprocess_input.
        prepared_image = preprocess_input(image_array)
        # Apply the model and get the prediction
        prediction = model.predict(prepared_image)
        # Clean the prediction
       # Show the prediction to the user
        print(prediction)
        return (path)
        return render_template('html.xhtml')
    else:
        return render_template('html.xhtml')

if __name__ == '__main__':
    app.run()


