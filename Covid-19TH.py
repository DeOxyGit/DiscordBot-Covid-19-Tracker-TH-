from configparser import DEFAULTSECT
from socket import EBADF
from warnings import resetwarnings
import discord
from datetime import datetime,timedelta
from discord import embeds
from discord import colour
from discord.ext import commands
import requests

# Global varible
bot = commands.Bot(command_prefix='#',help_command=None)





# thai เช๊คcovid-19
@bot.command()
async def thai(ctx):
    # API
    response=requests.get("https://disease.sh/v3/covid-19/countries/thailand")
    data=response.json()
    newcon=data['todayCases']
    allcase=data['cases']
    reco=data['recovered']
    hospi=data['active']
    die=data['deaths']
    todaydie=data['todayDeaths']

    datestr = datetime.fromtimestamp(data["updated"] / 1e3)
    normdate=datestr.strftime("%A %d/%m/%Y")

    mention = ctx.author.mention
    
    emBedcovid=discord.Embed(title='Covid-19 Update today!',description=f'request by [{mention}]',color=0xFF0000)
    emBedcovid.add_field(name='ผู้ติดเชื้อทั้งหมด',value='{:,}'.format(allcase)+' คน')
    emBedcovid.add_field(name='ติดเชื้อเพิ่ม',value='{:,}'.format(newcon)+' คน')
    emBedcovid.add_field(name='หายแล้ว',value='{:,}'.format(reco)+' คน')
    emBedcovid.add_field(name='อยู่โรงพยาบาล',value='{:,}'.format(hospi)+' คน')
    emBedcovid.add_field(name='ตายแล้ว',value='{:,}'.format(die)+' คน')
    emBedcovid.add_field(name='ตายเพิ่ม',value='{:,}'.format(todaydie)+' คน')
    emBedcovid.add_field(name='อัพเดตเมื่อ',value=f'{normdate}')
    emBedcovid.set_thumbnail(url='https://phil.cdc.gov//PHIL_Images/23311/23311_lores.jpg')

    await ctx.channel.send(embed=emBedcovid)

bot.run('your token')
# Code by Ratchanon Promsombut
