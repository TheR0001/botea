import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(help="Génère un code Nitro valide.")
async def nitro(ctx):
    await ctx.send("Récupére ton code nitro ici https://arrea.netlify.app/nitroeaclaim.html")

@bot.command(help="Donne une rapide description du bot")
async def description(ctx):
    await ctx.send(
        "Salut ! Je suis un bot discord français développé par Arrea en python !"
    )

@bot.command(help="Répond avec un message Pile ou Face aléatoirement")
async def pileface(ctx):
    await ctx.send(random.choice(["Pile !", "Face !"]))

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower() == "ping":
        await message.channel.send("Pong !")
    await bot.process_commands(message)

token = os.getenv('TokenBotEa')
bot.run(token)
