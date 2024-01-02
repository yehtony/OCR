# Note: The openai-python library support for Azure OpenAI is in preview.
# Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
import openai
from computervision import analyze_image

openai.api_type = "azure"
openai.api_base = "https://qag02.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "17f82d1fc6fe4d0ba2a768d8836c3e89"

image_url = "http://127.0.0.1:8080/%E8%97%A5%E5%93%81%E6%98%8E%E7%B4%B0%E5%8F%8A%E6%94%B6%E6%93%9A.png"
content = analyze_image(image_url)

message_text = [
    {
        "role": "system",
        "content": '你是一名藥師，你會接收到病患的藥單資料，你必須先自行判斷藥單內容的正確性並在必要時自行做修正，你必須依照格式整理出以下資料，並且要遵守資料型態，格式為{名稱：值}，且值的基本單位要符合相應名稱，你只能列出以下集合中提到的內容，其他一律不回應，並且集合間用空行分開，如果無法從訊息中辨識到資料名稱，請把對應的值設為"null"：\n\n第一種集合，只需列出一個：\n{開方日期：(date)\n開方醫院：(varchar)}\n\n第二種集合，依據藥品數量列出：\n{商品名：(varchar)\n成分名/學名 : (varchar)\n劑量：(varchar)\n單位劑量：(varchar)\n每日劑量：(varchar)}\n',
    },
    {
        "role": "user",
        "content": content,
    },
]

completion = openai.ChatCompletion.create(
    engine="LC-gpt35turbo",
    messages=message_text,
    temperature=0,
    max_tokens=500,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
)

print(completion['choices'][0]['message']['content'].encode('utf-8').decode('utf-8'))
