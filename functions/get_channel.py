import discord

async def get_channel(guild):
    bot_channel = discord.utils.get(guild.text_channels, name="ia-channel")

    if not bot_channel and guild.me.guild_permissions.manage_channels:
        bot_channel = await guild.create_text_channel('ia-channel')
        await bot_channel.send("Este es el canal dedicado para interactuar con el bot.")

    return bot_channel