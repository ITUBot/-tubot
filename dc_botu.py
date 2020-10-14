import discord
from discord.ext.commands import Bot
from discord.ext import commands

bot = discord.Client()
bot_prefix="!"
bot = commands.Bot(commands_prefix=bot_prefix)

@bot.event
async def on_ready() :
    print("Bot çevrimiçi!")
    print(f"isim: {bot.user.name}")
    print(f"ID: {bot.user.id}")
    print(str(len(bot.servers)) + "tane serverda çalışıyor.")
    print(str(len(set(bot.get_all_members()))) + "tane kullanıcıya erişiyor.")
    await bot.change_presence(game=discord.Game(name='İTÜ BOTa erişmek için !it ile başla'))

@bot.commands(pass_context=True)
async def it(ctx) :      #birisi !it yazarsa alttaki şeyi yazıcak bot
    await bot.say("efendim canımıniçi")

@bot.commands(pass_context=True)
async def a(ctx) :                #birisi !a yazarsa bot onun ismini söylicek
    await bot.say(csx.message.author.name)

@bot.commands(pass_context=True)
async def a(ctx, member:discord.Member) :      #taglenen kişi member.name oluyor oraya yazıyor
    await bot.say(csx.message.author.name + "sizden bahsetti sayın " + member.name)

@bot.commands(pass_context=True)
async def a(ctx, member:discord.Member) :
    linkler = ["","","","","","","",""]   #buraya foto linkleri yapıştır 
    embed = discord.Embed(title=csx.message.author.name + "sana sarılıyor" + member.name)
    embed.set_image(linkler=random.choice(linkler))
    await bot.say(embed=embed)           #embed fotoğrafla birlikte yazı çıkarmayı sağlıyor

@bot.commands(pass_context=True)
async def sil(ctx, number) :
    baba = []                     #mesaj silmeyi sağlar
    sayi = int(sayi)
    async for x in bot.logs_from(ctx.message.channel, limit=sayi):
        baba.append(x)
    await bot.delete.messages(baba)

@bot.commands(pass_context=True)
async def s(ctx) :
    baba = ctx.message.content.split("1")
    await bot.delete_message(ctx.message)      #yazdığın komutu bot yazıyor ama listede alıyor
    await bot.send_message(ctx.message.channel , baba)

bot.run("NzY0MTMzNTgzNzY1NzY2MTc1.X4B02w._4ehSAnO3hzNq_1FQiLJ9XlXqBc")