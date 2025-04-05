from flask import Flask, render_template, request, Response
import os
from yt_dlp import YoutubeDL

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DOWNLOAD_DIR = '/app/downloads'

def download_video(url, download_dir):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True, f"Download completed successfully for: {url}"
    except Exception as e:
        return False, f"An error occurred while downloading {url}: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        success, message = download_video(url, DOWNLOAD_DIR)
        if success:
            return message
        else:
            return Response(message, status=400)
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    app.run(host='0.0.0.0', port=5000, debug=True)
