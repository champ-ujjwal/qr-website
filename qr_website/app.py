from flask import Flask, render_template, request
import qrcode
import base64
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_image = None

    if request.method == "POST":
        url = request.form["url"]

        img = qrcode.make(url)
        buf = io.BytesIO()
        img.save(buf, format="PNG")

        # Convert image to base64 to show in HTML
        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        qr_image = img_base64

    return render_template("index.html", qr_image=qr_image)

if __name__ == "__main__":
    app.run()
