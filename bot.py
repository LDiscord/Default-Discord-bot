import discord
import discord
import discord
import discord
import time
import asyncio
from discord import Activity, ActivityType
from discord.ext.commands import Bot
from discord.ext import commands
from config import settings
bot = commands.Bot(command_prefix = settings['prefix'])
bot.remove_command('help')
@bot.command()
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.channel.purge(limit=1 )
    return await ctx.send(mesg)
@bot.command()
async def help(ctx):
    emb = discord.Embed(title ="Основные команды", colour= discord.Colour.blue())
    emb.add_field(name= "a!help", value= "Выводит это меню")
    emb.add_field(name="a!say", value="Сказать что-то от имени бота")
    emb.add_field(name="a!calc",value="Калькулятор")
    emb.add_field(name="a!ava",value="Аватар Человека")
    emb.add_field(name="a!clear",value="Очистить Сообщения")
    emb.add_field(name="a!ban",value="Забанить Участника")
    emb.add_field(name="a!thx",value="Благодарности")
    await ctx.send(embed=emb)
@bot.command()
async def ava(ctx, *, user: discord.
  Member = None):
    if user == None:
        user = ctx.author
    embed = discord.Embed(description=f'Аватар: {user}', color=0x2f3136)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)
@bot.event
async def on_ready():
    print("БОТ ЗАПУЩЕН!")
    while True:
        await bot.change_presence(status=discord.Status.idle,activity=Activity(name="за серверами",type=ActivityType.watching)) #online - зелень. idle - желтый. #смотрит
@bot.command()
async def calc(ctx, numb:int, numb2:int):
		xd = int(numb) + int(numb2)
		v2 = int(numb) - int(numb2)
		v3 = int(numb) * int(numb2)
		v4 = int(numb) / int(numb2)
		emb = discord.Embed(title= 'Калькулятор', colour = discord.Color.blue())
		emb.add_field(name= 'Ответ:', value= 'Добавление: '+str(xd)+"\n" + 'Вычетание: '+ str(v2)+'\n' + 'Умножение: ' + str(v3) +'\nДеление: ' + str(v4))
		await ctx.send(embed = emb)
@bot.command(pass_context=True)
async def clear(ctx, amount:int):
        if amount >= 301:
        	await ctx.send('Максимальное количество для очистки:300! ')
        else:
        	await ctx.channel.purge(limit=amount)
        	await ctx.send(str(ctx.message.author)+ " " + f"Очистил {amount} сообщений! ") 
#ban
@bot.command()
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member:discord.Member=None, reason=None):
    if member and reason:
        emb = discord.Embed(title="Бан", colour= discord.Color.blue())
        emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
        emb.add_field(name='Нарушитель',value=member.mention,inline=False)
        emb.add_field(name='Причина',value=reason,inline=False)
        emb.set_thumbnail(url=ctx.author.avatar_url)
        emb.set_footer(text=f"Использовал команду: {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed= emb)
        await member.send("⚠️Вас забанили по причине " + reason + " ,Всего доброго!")
        await member.ban(reason=reason)
    else:
        await ctx.send("Укажите участника и причину⚠️")
@bot.command()
async def h(ctx):
    emb = discord.Embed(title ="Основные команды", colour= discord.Colour.blue())
    emb.add_field(name= "a!help", value= "Выводит это меню")
    emb.add_field(name="a!say", value="Сказать что-то от имени бота")
    emb.add_field(name="a!calc",value="Калькулятор")
    emb.add_field(name="a!ava",value="Аватар Человека")
    emb.add_field(name="a!clear",value="Очистить Сообщения")
    emb.add_field(name="a!ban",value="Забанить Участника")
    emb.add_field(name="a!thx",value="Благодарности")
    await ctx.send(embed=emb)
@bot.command()
async def thx(ctx):
	emb = discord.Embed(title= 'Благодарности',colour=discord.Color.blue())
	emb.add_field(name="Acelot",value="Очень помог с ботом", inline=False)
	emb.add_field(name="Never See",value="Очень помог с ботом", inline=False)
	emb.add_field(name="[UNX] Fonsy13",value="Придумал название")
	emb.add_field(name= "Kaven0n",value="Хз,попросил совместку.")
	await ctx.send(embed=emb)
bot.run(settings['token'])