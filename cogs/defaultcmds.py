import discord
from discord.ext import commands

class DefaultCmds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        
        # Default
        default_embed = discord.default_embed(
            title = "Default",
            colour = discord.Colour.light_gray()
        )
        default_embed.add_field(name = "help", value = "Returns a list of commands.", inline = False)
        default_embed.add_field(name = "load [EXTENTION]", value = "Loads a cog.", inline = False)
        default_embed.add_field(name = "unload [EXTENTION]", value = "Unloads a cog.", inline = False)
        default_embed.add_field(name = "reload [EXTENTION]", value = "Unloads and loads a cog.", inline = False)
        default_embed.add_field(name = "checkforupdates", value = "Unloads and loads all cogs", inline = False)
        await ctx.send(embed = default_embed)

        # Fun
        fun_embed = discord.fun_embed(
            title = "Fun",
            colour = discord.Colour.blue()
        )
        fun_embed.add_field(name = "ping", value = "Returns the user's ping.", inline = False)
        fun_embed.add_field(name = "8ball [QUESTION]", value = "Returns a random answer to the question.", inline = False)
        fun_embed.add_field(name = "senddudes [AMOUNT = 1]", value = "Returns [AMOUNT] images of dudes.", inline = False)
        fun_embed.add_field(name = "bordem [AMOUNT = 1]", value = "Returns [AMOUNT] random videogames.", inline = False)
        fun_embed.add_field(name = "votemf [AMOUNT = 1]", value = "Returns a random Among Us player.", inline = False)
        fun_embed.add_field(name = "test", value = "Returns a defined message.", inline = False)
        await ctx.send(embed = fun_embed)

        # Moderation
        moderation_embed = discord.moderation_embed(
            title = "Moderation",
            colour = discord.Colour.red()
        )
        moderation_embed.add_field(name = "clear [AMOUNT = 1]", value = "Clears [AMOUNT] messages in the executed channel.", inline = False)
        moderation_embed.add_field(name = "kick [USER] [REASON = NONE]", value = "Kicks the user from the server with an optional reason. User executing command must have kick permissions", inline = False)
        moderation_embed.add_field(name = "ban [USER] [REASON = NONE]", value = "Bans a user from that server with an optional reason. User executing the command must have ban permissions.", inline = False)
        moderation_embed.add_field(name = "unban [USER]", value = "Unbans a user from the server. User executing the command must have ban permissions.", inline = False)
        await ctx.send(embed = moderation_embed)

def setup(client):
    client.add_cog(DefaultCmds(client))