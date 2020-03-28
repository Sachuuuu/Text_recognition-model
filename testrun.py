# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:36:35 2020

@author: SACHUU
"""

import requests
import base64
import json
import numpy as np

content_type = 'application/json'
headers = {'content-type': content_type}
url = "http://sachuu96.westus2.cloudapp.azure.com:8080/api/expression/"



def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


text = {"text":get_base64_encoded_image('ss.jpeg')}

ini_string = json.dumps(text)

gg = requests.post(url,json=json.loads(ini_string),headers = headers)
print(gg.text)