from flask import Flask, render_template, request, redirect, url_for, flash
import os
from yt_dlp import YoutubeDL
#from urllib.parse import quote as url_quote

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key in production

DOWNLOAD_DIR = '/app/downloads'

# def download_video(url, download_dir):
#     ydl_opts = {
#         'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
#         'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
#     }
#     try:
#         with YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         return f"Download completed successfully for: {url}"
#     except Exception as e:
#         return f"An error occurred while downloading {url}: {str(e)}"

def download_video(url, download_dir):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',  # Custom user agent
        # 'ratelimit': 1000000,  # Limit download speed
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Download completed successfully for: {url}"
    except Exception as e:
        return f"An error occurred while downloading {url}: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=DOWNLOAD_DIR)
            return "Download Successful"
        except Exception:
            return "Invalid URL", 400  # ✅ Ensure error message is sent correctly

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    app.run(host='0.0.0.0', port=5000, debug=True)
