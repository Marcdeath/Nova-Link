from flask import Flask, request, send_file
from rembg import remove 
from PIL import Image 
import io

app = Flask(__name__)

@app.route('/remove-bg',methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
                    
                    return "Aucune image envoyée",400

                    Image_file= request.files['image']
                    input_image=Image.open(image_file.stream)

                    output_image= remove(input_image)

                    img_io = io.BytesIO()
                    output_image.save(img_io, 'PNG')
                    img_io.seek(0)

                    return send_file(img_io,minetype='image/png')

                    if _name_ == '_main_':
                                        app.run(debug=True)