from flask import Flask,render_template,request
from PIL import Image
import uuid
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/gen", methods=["POST"])
def gen():
    h = int(request.form['height'])
    w = int(request.form['width'])
    c = request.form['color']
    r = int(c[1]+c[2], 16)
    g = int(c[3]+c[4], 16)
    b = int(c[5]+c[6], 16)
    p = int(request.form['colorPar'])
    img = Image.new("RGB", (w, h))
    iid = uuid.uuid4()
    iid = str(iid)
    for i in range(h):
        for j in range(w):
            r = random.randint(0, 100)
            if r < p:
                img.putpixel((j,i),(r,g,b))
            else:
                img.putpixel(
                    (j,i),
                    (
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255)
                    )
                )
    img.save("output/"+iid+".png")
    return "OK"