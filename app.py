from flask import Flask, render_template, request, redirect
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=["POST", "GET"])
def download():
    url = request.form.get("link")
    print("Someone just tried to download", url)

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return "Download started!"
    except Exception as e:
        print("Error:", str(e))
        return str(e), 400

if __name__ == '__main__':
    app.run(port=80, debug=True)
