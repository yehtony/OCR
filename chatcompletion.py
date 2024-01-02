# Note: The openai-python library support for Azure OpenAI is in preview.
# Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
import openai
from computervision import analyze_image

openai.api_type = "azure"
openai.api_base = "https://qag02.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "17f82d1fc6fe4d0ba2a768d8836c3e89"

image_url = "http://140.115.126.98:8080/00.jpg"
content = analyze_image(image_url)

message_text = [{"role": "system", "content": "你是一名藥師，你會接收到病患的藥單資料，你必須先自行判斷藥單內容的正確性並在必要時自行做修正，你必須依照格式整理出以下資料，並且要遵守資料型態，格式為{名稱：值}，且值的基本單位要符合相應名稱，你只能列出以下集合中提到的內容，其他一律不回應，集合用大括弧，集合間用空行分開，內容遵照JSON格式，如果無法從訊息中辨識到資料名稱，請把對應的值設為\"null\"：\\n\\n第一種集合，只需列出一個：\\n{\"開方日期\"：(date)\\n\"開方醫院\"：(varchar)}\\n\\n第二種集合，依據藥品數量列出：\\n{\"商品名\"：(varchar)\\n\"成分名/學名\" : (varchar)\\n\"劑量\"：(float)\\n\"每次劑量\"：(smallint)\\n\"每日劑量\"：(varchar)}\\n\"給藥日份\"：(smallint)}"}, {"role": "user", "content": "院所名稱:身心診所[3531133279]【藥品明細及收據】院所地址:[02-01991姓名:生日:年齡: 歲 月女 就醫序號:0011日期:107.03.30 證號:發藥21日份 身份證:XXXXX調      \n劑藥師:林醫師姓名:梁=健保項目點數藥=品=名=稱=單位劑量 用法 次量 x次x天 總=量 診察 費:1601 MOCALM(0.5)内服 1.00必要時 21.0 藥服費:352 ALPRALINE(0.5)       \n内服 1.00必要時 21.0 藥費:154成份名:ALPRAZOLAM診療費:3443 Genclone(7.5)*內服 1.00x1x21 21.0 合計: 693成份名:ZOPICLONE健保申請:623加收自付額:20元合計      \n藥費:付費用項目3118324950昌門診:藥費一付:: 06:300華容許自付:2070掛號費:150實收金額:220"}, {
    "role": "assistant", "content": "{\"開方日期\"：107.03.30,\n\"開方醫院\"：身心診所[3531133279]}\n\n{\"商品名\"：\"MOCALM\",\n\"成分名/學名\"：null,\n\"劑量\"：0.5,\n\"每次劑量\"：1,\n\"每日劑量\"：\"必要時\",\n\"給藥日份\"：21}\n\n{\"商品名\"：\"ALPRALINE\",\n\"成分名/學名\"：\"ALPRAZOLAM\",\n\"劑量\"：0.5,\n\"每次劑量\"：1,\n\"每日劑量\"：\"必要時\",\n\"給藥日份\"：21}\n\n{\"商品名\"：\"Genclone\",\n\"成分名/學名\"：\"ZOPICLONE\",\n\"劑量\"：7.5,\n\"每次劑量\"：1,\n\"每日劑量\"：\"1\",\n\"給藥日份\"：21}"},{"role": "user", "content": content}]

completion = openai.ChatCompletion.create(
    engine="gpt-35-turbo-16k",
    messages=message_text,
    temperature=0,
    max_tokens=500,
    top_p=0,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
)

print(completion['choices'][0]['message']
      ['content'].encode('utf-8').decode('utf-8'))
