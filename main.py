import discord
from discord.ext import commands
from discord.ui import Button, View
from discord import app_commands

'''
© 2024. 201580ag MIT License
'''

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
intents.voice_states = True

@bot.command(name="modal", description="modal 만들기")
async def 팀(ctx, *, 설명):
    voice_state = ctx.author.voice
    if voice_state is None or voice_state.channel is None:
        await ctx.send("❌ 음성채널 입장 후 명령어를 사용해주세요.")
        return

    channel = voice_state.channel
    members = len(channel.members)
    max_members = 4  # 최대 멤버 수

    member_text = f"{members}명 / {max_members}명"

    embed = discord.Embed(title="팀원 모집", color=0x992D22)
    embed.add_field(name="", value=f"{ctx.author.mention} 님이 팀원 모집 중입니다.", inline=False)
    embed.add_field(name="카테고리", value=ctx.channel.category.name, inline=False)
    embed.add_field(name="채널 URL", value=f"https://discord.com/channels/{ctx.guild.id}/{channel.id}", inline=True)
    embed.add_field(name="멤버", value=member_text, inline=True)
    embed.add_field(name="설명", value=설명, inline=False)

    button1 = Button(label="🔈 음성채널 입장", style=discord.ButtonStyle.green, url=f"https://discord.com/channels/{ctx.guild.id}/{channel.id}")

    view = View()
    view.add_item(button1)

    await ctx.send(embed=embed, view=view)

bot.run("TOKEN")
