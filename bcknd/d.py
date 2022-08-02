
from io import StringIO
import urllib.request
# using time module
import time
  
# ts stores the time in seconds
def calculateCyclone():
# Adding information about user agent
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    # setting filename and image URL
    ts = time.time()
    filename = 'C:\\Users\\vivek\\Downloads\\testimg{}.jpg'.format(ts)
    image_url = "https://mausam.imd.gov.in/Satellite/rswmo_ir1.jpg"

    # calling urlretrieve function to get resource
    urllib.request.urlretrieve(image_url, filename)


    from keras.models import load_model
    from PIL import Image, ImageOps
    import numpy as np

    # Load the model
    model = load_model('C:\\Users\\vivek\\Desktop\\CycloneTracker\\img\\keras_model.h5')

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open(filename)
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)

    prediction = prediction*100
    print(prediction)
    print(prediction[0][0])
    print(prediction[0][1])
    result="none"
    prediction[0][0] = round(prediction[0][0],2)
    prediction[0][1] = round(prediction[0][1],2)
    if prediction[0][1]<25.00:
        print('cyclone may occur')
        result="cyclone may occur"
    elif (prediction[0][1]>25) & (prediction[0][0]<75):
        print('cyclone probability is less')
        result="cyclone probability is less"
    else:
        print('cyclone aagaya RIP')
        result="cyclone has come"
        
    output = "Chances of cyclone:"+str(prediction[0][0]) +"%\n" +"Chances of no cyclone:" +str(prediction[0][1]) +"%\n"+result+"\n"
    return output



