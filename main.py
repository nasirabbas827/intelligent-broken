from flask import Flask, flash, request, redirect, render_template
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
UPLOAD_BROKEN = 'static/broken/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_BROKEN'] = UPLOAD_BROKEN
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        original_image = cv2.imread("static/uploads/" + filename)

        makred_amages = cv2.imread("static/uploads/" + filename, 0)  # gray scale
        ret, thresh = cv2.threshold(makred_amages, 254, 255, cv2.COLOR_BGR2HSV)

        kernel = np.ones((7, 7), np.uint8)

        img = original_image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blured = cv2.blur(gray, (1, 1))
        ret, thres = cv2.threshold(img_blured, 210, 255, cv2.THRESH_BINARY)
        neg = cv2.bitwise_not(thres)
        erosion = cv2.erode(neg, np.ones((6, 6), np.uint8), iterations=1)
        img[erosion == 0] = 0

        mask = cv2.dilate(thres, kernel, iterations=1)

        repair_image = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

        cv2.imwrite("static/broken/" + filename, img)
        cv2.imwrite("static/repair/" + filename, repair_image)
        filepath_original = "static/uploads/" + filename
        broken_path = "static/broken/" + filename
        repair_path = "static/repair/" + filename

        flash('Image Processed Successfully')
        return render_template('index.html', filename=filepath_original, filenameBroken=broken_path, filenameRepair=repair_path)
    # return render_template('index.html', filename=filename)

    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    # return redirect(url_for('static', filename='uploads/' + filename), code=301)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
