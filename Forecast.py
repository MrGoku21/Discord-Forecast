import discord

from discord.ext import commands
import pyowm

API_TOKEN = "" # Put your OWM token here
BOT_TOKEN = "" # Put your discord bot token here

owm = pyowm.OWM(API_TOKEN)
bot = commands.Bot(command_prefix = "!", help_command=None)


# --------------------------------------------------------------------#
#                             Forecast                                #
# --------------------------------------------------------------------#

@bot.command() # A basic weather bot
async def forecast(ctx, *, country=None):
    if country is None:
        return await ctx.send("You need to provide a country/city!")

    await ctx.trigger_typing()
    observation = owm.weather_at_place(country) # This is where the bot finds info about the weather in the typed in country
    w = observation.get_weather()
    temp = w.get_temperature(unit="celsius")["temp"] # You can use other measurements here too 
    status = w.get_status()
    statusAD = w.get_detailed_status()
    pfp = w.get_weather_icon_url()
    humid = w.get_humidity()
    wind = w.get_wind()["speed"]
    
    embed = discord.Embed(title=":white_sun_cloud: Weather Check ", description=f"Details about the weather in {country}", color=0xff9f9f)
    embed.add_field(name="Status", value=f"{status}, {statusAD}", inline=True)
    embed.add_field(name="Temperature", value=f"{temp}c", inline=True)
    embed.add_field(name="Humidity", value=f"{humid}%", inline=True)
    embed.add_field(name="Wind speed", value=f"{wind}m/s", inline=True)

    embed.set_thumbnail(url=pfp)
    embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed) # Send the data back


bot.run(BOT_TOKEN)
