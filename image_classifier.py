import subprocess
import dramatiq
import deploy_keys
def install(name):
    subprocess.run(['pip', 'install', name])
install('dramatiq[rabbitmq, watch]')
from dramatiq.brokers.rabbitmq import RabbitmqBroker

rabbitmq_broker = RabbitmqBroker(url="amqp://admin:{}@54.183.183.4".format(deploy_keys.rabbitmq_password))
dramatiq.set_broker(rabbitmq_broker)

from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from requests import get
import numpy as np
from pathlib import Path
from requests.utils import quote

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)
        
model = ResNet50(weights='imagenet')

@dramatiq.actor
def classify_images(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)  
    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    print('Predicted:', decode_predictions(preds, top=3)[0])

@dramatiq.actor
def classify_video(video_url):
    for i in range(125):
        image = download("robert.com/keyframe?frame={}&url={}".format(i, quote("https://r2---sn-a5mlrn76.googlevideo.com/videoplayback?dur=0.000&itag=43&signature=745E5675AF27E7A5BBDFA137D960EEC5DFB4C83C.4403DD831AC451690683705300B19B69305E7A63&key=cms1&gir=yes&expire=1524977533&id=o-AAyZQDWBqx9kO7n-Ubg9kpekefTB1mKFWks0XkZwvblB&lmt=1518836860313898&ip=45.77.200.244&ei=HfvkWpbtBouL8wSMmI3oBQ&pl=24&source=youtube&sparams=clen%2Cdur%2Cei%2Cexpire%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmip%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource&c=WEB&fexp=23724337&mime=video%2Fwebm&clen=51298521&fvip=2&ipbits=0&ratebypass=yes&requiressl=yes&title=Science%20Copies%20Nature%27s%20Secrets%20-%20Biomimicry&mip=64.62.224.29&redirect_counter=1&cm2rm=sn-n4ves7l&req_id=ac95d2efd3a4a3ee&cms_redirect=yes&mm=34&mn=sn-a5mlrn76&ms=ltu&mt=1524961281&mv=u")), '{}.jpg'.format(i))
        classify_images(image)