#導入Discord.py
import discord
#client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)
@client.slash_command(name="更改狀態")
async def 更改狀態(ctx, arg1): 
    await ctx.respond(arg1)
@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果以「說」開頭
    if message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])

client.run('MTE4NjYzMDMwODk0MzEwNjA4MA.Gp6_vU.ul4TeMxRvC2hZVVzjlNoAVRozAwlq8cx-GwRRM') #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
