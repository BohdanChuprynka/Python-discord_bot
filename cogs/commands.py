from discord.ext import commands
import discord

#cog only for commands !
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", help="- pong")
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f"Something went wrong:\n{error}")
        print(f"Error: {error}")

    @commands.command(name="embed", help="- test command")
    async def embed(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author

        name = member.display_name
        pfp = member.display_avatar

        embed = discord.Embed(title="That's a title", description="That's a description", color=discord.Color.random())
        embed.set_author(name=name)
        embed.set_thumbnail(url=pfp)
        embed.add_field(name="This is 1 field", value="This field is just a value")
        embed.add_field(name="This is 2 field", value="This field is inline True", inline=True)
        embed.add_field(name="This is 3 field", value="This field is inline False", inline=False)
        embed.set_footer(text=f'{name} Made this Embed')

        await ctx.send(embed=embed)

    @commands.command(name="hello", help="- Hello, dude")
    async def hello(self, ctx):
        await ctx.send("Hello, my dear")

async def setup(bot):
    await bot.add_cog(Commands(bot))
