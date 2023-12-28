# ########### Python 3.2 #############
# import http.client, urllib.request, urllib.parse, urllib.error, base64, json, os

# headers = {
#     # Request headers
#     "Content-Type": "application/json",
#     "Ocp-Apim-Subscription-Key": "48ee175c411d4cd4b9ee2513f5b83cc5",
# }

# image = "https://pic.pimg.tw/mulicia/1390350684-3189396833_l.png"
# body = {"url": image}
# body = json.dumps(body)

# params = urllib.parse.urlencode(
#     {
#         # Request parameters
#         "features": "read",
#         "language": "zh-Hant",
#         "gender-neutral-caption": "False",
#     }
# )

# try:
#     conn = http.client.HTTPSConnection("medocr.cognitiveservices.azure.com")
#     conn.request(
#         "POST",
#         "/computervision/imageanalysis:analyze?api-version=2023-02-01-preview&%s"
#         % params,
#         body,
#         headers,
#     )
#     response = conn.getresponse()
#     data = response.read().decode("utf-8")
#     result_dict = json.loads(data)
#     content = result_dict.get("readResult", {}).get("content", "").replace("\n", "")
#     print(content)
#     return content
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

# ####################################

# computervision.py

import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json
import os

def analyze_image(image_url):
    headers = {
        # Request headers
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "48ee175c411d4cd4b9ee2513f5b83cc5",
    }

    body = {"url": image_url}
    body = json.dumps(body)

    params = urllib.parse.urlencode(
        {
            # Request parameters
            "features": "read",
            "language": "zh-Hant",
            "gender-neutral-caption": "False",
        }
    )

    try:
        conn = http.client.HTTPSConnection("medocr.cognitiveservices.azure.com")
        conn.request(
            "POST",
            "/computervision/imageanalysis:analyze?api-version=2023-02-01-preview&%s"
            % params,
            body,
            headers,
        )
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        result_dict = json.loads(data)
        content = result_dict.get("readResult", {}).get("content", "").replace("\n", "")
        conn.close()
        return content
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return None
