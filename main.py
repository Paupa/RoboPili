import discord
import random
import os  # default module
from dotenv import load_dotenv


load_dotenv()  # load all the variables from the env file
bot = discord.Bot(debug_guilds=[941436192287764501])
nombres: list = []


@bot.event
async def on_ready():
    print("¡LLEGÓ LA PILI!")


def elegir_nombre():
    return random.choice(nombres)


@bot.slash_command(name = "apunta", description = "Apunta un nombre")
async def apuntar(ctx, nombre : discord.Option(str, "Nombre")):
    nombres.append(nombre)
    await ctx.respond(f"{nombre} apuntao ;)")


@bot.slash_command(name = "lista", description = "Lista los nombres apuntados")
async def listar(ctx):
    respuesta = "Los nombres apuntados son:"
    for nombre in nombres:
        respuesta += f" {nombre}"
    await ctx.respond(respuesta)


@bot.slash_command(name = "borra", description = "Borra un nombre")
async def borrar(ctx, nombre : discord.Option(str, "Nombre")):
    respuesta = f"Ya quité a {nombre}"
    try:
        nombres.remove(nombre)
    except ValueError:
        respuesta = f"No había apuntado a {nombre}, cari :("

    await ctx.respond(respuesta)


@bot.slash_command(name = "elige", description = "Elige a alguien y le mantiene en la lista")
async def elegir(ctx):
    respuesta = ""
    try:
        nombre = elegir_nombre()
        respuesta = f"{nombre}, hoy no juegas ;P"
    except IndexError:
        respuesta = "No hay nadie para elegir"

    await ctx.respond(respuesta)


@bot.slash_command(name = "mata", description = "Elige a alguien y le quita de la lista")
async def matar(ctx):
    respuesta = ""
    try:
        nombre = elegir_nombre()
        nombres.remove(nombre)
        respuesta = f"Adiós un abrazo, {nombre}"
    except IndexError:
        respuesta = "No hay nadie para matar"

    await ctx.respond(respuesta)


bot.run(os.getenv('TOKEN'))