import discord
import random
from discord.ext import commands
import os
from settings import settings
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    imagenes = (os.listdir('meme'))
    with open(f'meme/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)    

# ¡Y así es como se puede sustituir el nombre del fichero desde una variable!

@bot.command()

async def consejos(ctx):

        await ctx.send(f"""Hola soy un bot {bot.user}!""")
        await ctx.send(f"Es de muhca importancia el que uno mismo tenga encuenta su salud fisica ")
        # enviar pregunta al usuario 
        await ctx.send("quieres consejos de como cuidar tu salud ?, responde con 'si', o con 'no'.")
        #esperando respuestaaaa
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
        response = await bot.wait_for('message', check=check)

        if response :
            
            if response.content in ["si","si"]:
                await ctx.send("1.No cuidar tu alimentacion")
                await ctx.send("2.Tomar suficiente agua al dia")
                await ctx.send("3.dormir 8hrs")

            else :
                 await ctx.send(" esta bien , si algun dia necesitas de unos buenos consejos , aqui estoy") 

        else:
             await ctx.send("eh, lo siento , no te entiendo ,cambia tu respuesta por favor")  
            

     



bot.run(settings["TOKEN"])