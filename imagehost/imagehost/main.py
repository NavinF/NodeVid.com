from flask import Flask, url_for, request, send_file
import ffmpy 
import requests
import os.path
import posixpath

# Workflow
# Delete video and keyframes (from previous try) 
# Accept input url via json
# Download video  
# Feed video into FFMpeg, create keyframes 
# Serve keyframes out
# Repeat 

# internal.atube.com/keyframes?url={}&frame={}

app = Flask(__name__, static_url_path='/static')

@app.route("/keyframes")
def keyframes():
    url = request.args.get('url')
    frame = request.args.get('frame')

    path = url.rsplit('/', 1)[1]
    filename = posixpath.basename(path)

    if not os.path.isfile(filename):
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
        os.mkdir('static/' + filename)
        ff = ffmpy.FFmpeg(
        inputs={filename:  '-skip_frame nokey'},
        outputs={'static/' + filename + '/thumbnails-%09d.jpeg': '-vsync 0 -r 30 -f image2'}
        )
        ff.run()    

    return send_file('static/' + filename + '/thumbnails-%09d.jpeg' % int(frame))

if __name__ == '__main__':
    app.run(host='::')

