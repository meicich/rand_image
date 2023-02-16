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
    c = request.form['color2']
    r2 = int(c[1]+c[2], 16)
    g2 = int(c[3]+c[4], 16)
    b2 = int(c[5]+c[6], 16)
    p = int(request.form['colorPar'])
    p2 = int(request.form['colorPar2'])
    img = Image.new("RGB", (w, h))
    iid = uuid.uuid4()
    iid = str(iid)
    for i in range(h):
        for j in range(w):
            r = random.randint(0, 99)
            if r < p:
                img.putpixel((j,i),(r,g,b))
            elif r < p+p2:
                img.putpixel((j,i),(r2,g2,b2))
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