import base64
import hashlib
import os.path

import requests

class Weichat():

    def __init__(self):
        # self.uri = 'https://qygitapi.weixin.qq.com/cgi-bin/webhook/send?key=98253339-56d9-422a-bdff-8596abf7f8e1'
        self.uri = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b4c9e32d-08b1-4e16-b5d2-f2cd16a64b8f'



    def sendTxt(self, dt):
        dates = {
            "msgtype": "text",
            "text": {
                "content": dt
            }
        }
        resp = requests.post(self.uri, headers={'Content-Type': 'application/json'}, json=dates)


    def sendMarkdown(self, dt):
        dates ={
            "msgtype": "markdown",
            "markdown": {
                "content": dt  }
                }
        resp = requests.post(self.uri, headers={'Content-Type': 'application/json'}, json=dates)


    def sendPics(self, pic):
        b64 = self.genPicBs64(pic)
        # print(b64)
        md5 = self.genPicMd5(pic)
        # print(md5)
        dates ={
            "msgtype": "image",
            "image": {
                "base64": f"{b64}",
                "md5": f"{md5}"
            }
        }
        # print(dates)
        resp = requests.post(self.uri, headers={'Content-Type': 'application/json'}, json=dates)
        # print(resp.json())

    def sendNews(self):

        pass


    def genPicMd5(self, filepath):

        with open(filepath, 'rb') as f:
            ct = f.read()
        return hashlib.md5(ct).hexdigest()

    def genPicBs64(self, filepath):
        with open(filepath, 'rb') as f:
            b64encode = base64.b64encode(f.read())
        s = b64encode.decode()
        return s


if __name__ == '__main__':
    print('coding here:')
    from config import config

    rootpath = config().res_path
    pic = os.path.join(rootpath, '601601_20220.png')

    bt = Weichat()
    # bt.sendMarkdown('asdsadasda')
    bt.sendPics(pic)
