from flask import Flask, render_template, request
from youtubesearchpython import VideosSearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_data = []
    if request.method == 'POST':
        search_query = request.form['search_query']
        if search_query:
            videos = VideosSearch(search_query, limit = 5).result()
            for video in videos['result']:
                title = video['title']
                video_data.append(title)
    return render_template('index.html', video_data=video_data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
