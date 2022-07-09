import discord
import random
import os
from dotenv import load_dotenv


load_dotenv()  # Carga las variables del archivo .env
bot = discord.Bot(debug_guilds=[941436192287764501])
nombres: list = []


@bot.event
async def on_ready():
    print("¡LLEGÓ LA PILI!")


def elegir_nombre():
    return random.choice(nombres)


@bot.slash_command(name = "apunta", description = "Apunta un nombre")
async def apuntar(ctx, nombre: discord.Option(str, "Nombre")):
    nombres.append(nombre)
    await ctx.respond(f"{nombre} apuntao ;)")


@bot.slash_command(name = "lista", description = "Lista los nombres apuntados")
async def listar(ctx):
    numero_de_nombres = len(nombres)
    respuesta: str
    if numero_de_nombres == 0:
        respuesta = "No tengo a nadie apuntado"
    else:
        respuesta = f"Tengo apuntado a "
        if numero_de_nombres == 1:
            respuesta += nombres[0]
        else:
            nombres_medio = nombres.copy()
            ultimo_nombre = nombres_medio.pop()  # Elimino el último nombre

            respuesta += ", ".join(nombres_medio)
            respuesta += f" y {ultimo_nombre}"

    await ctx.respond(respuesta)


@bot.slash_command(name = "borra", description = "Borra un nombre")
async def borrar(ctx, nombre: discord.Option(str, "Nombre")):
    respuesta: str
    try:
        nombres.remove(nombre)
        respuesta = f"Ya quité a {nombre}"
    except ValueError:
        respuesta = f"No había apuntado a {nombre}, cari :("

    await ctx.respond(respuesta)


@bot.slash_command(name = "elige", description = "Elige a alguien y le mantiene en la lista")
async def elegir(ctx):
    respuesta: str
    try:
        nombre = elegir_nombre()
        respuesta = f"{nombre}, hoy no juegas ;P"
    except IndexError:
        respuesta = "No hay nadie para elegir"

    await ctx.respond(respuesta)


@bot.slash_command(name = "mata", description = "Elige a alguien y le quita de la lista")
async def matar(ctx):
    respuesta: str
    try:
        nombre = elegir_nombre()
        nombres.remove(nombre)
        respuesta = f"Adiós un abrazo, {nombre}"
    except IndexError:
        respuesta = "No hay nadie para matar"

    await ctx.respond(respuesta)


bot.run(os.getenv('TOKEN'))