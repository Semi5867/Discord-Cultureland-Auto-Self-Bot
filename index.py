import discord, requests, setting, datetime, os
from setting import token, cul_id, cul_pw, api, api_token, prefix

client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    os.system('cls')
    print('문화상품권 자동충전 셀프봇 시작됨 - 개발자: 세미#3182')

@client.event
async def on_message(message):
    if message.content.startswith(f"{prefix}충전 "):
        pin = message.content.split(" ")[1]
        jsondata = {"token" : api_token, "id" : cul_id, "pw" : cul_pw, "pin" : pin}
        res = requests.post(api, json=jsondata)
        res = res.json()
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        if (res["result"] == True):
            await message.reply(f"**```scss\n[ Charging Success ]\n``````\nPincode\n{pin}\n``````\nAmount\n{res['amount']}원\n``````\nDays\n{nowDatetime}\n```**")
        elif (res["result"] == False):
            await message.reply(f"**```scss\n[ Charging Failure ]\n``````\nPincode\n{pin}\n``````\nReason\n{res['reason']}\n``````\nDays\n{nowDatetime}\n```**")

client.run(token, bot=False)