import discord

from discord.ext import commands
import pyowm

owm = pyowm.OWM(PUT YOUR API HERE)

bot = commands.Bot(command_prefix = "!", help_command=None)


# ---------------------------------------------------------------------
#                           Forecast                                  |
# ---------------------------------------------------------------------

@bot.command() # A basic weather bot
async def forecast(self, ctx, *, country):
    observation = owm.weather_at_place(country) # This is where the bot finds info about the weather in the typed in country
    w = observation.get_weather()
    temp = w.get_temperature(unit='celsius') # You can use others here. 
    status = w.get_status()
    statusAD = w.get_detailed_status()
    pfp = w.get_weather_icon_url()
    avgTemp=temp['temp']
    humid = w.get_humidity()
    w_speed = w.get_wind()
    wind=w_speed['speed']
    username = ctx.message.author
    userpfp = username.avatar_url
    embed=discord.Embed(title="🌥 Weather Check ", description=f"Details about the weather in {country}", color=0xff9f9f)
    embed.add_field(name="Status", value=f"{status}, {statusAD}", inline=True)
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(name="Tempreture", value=f"{avgTemp}c", inline=True)
    embed.add_field(name="Humidity", value=f"{humid}%", inline=True)
    embed.add_field(name="Wind speed", value=f"{wind}m/s", inline=True)
    embed.set_footer(text=f"Requested by {username}", icon_url=f"{userpfp}")
    await ctx.send(embed=embed) # Posts the info the bot gathered


bot.run(YOUR BOT token here)
