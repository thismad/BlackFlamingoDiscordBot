import json
import discord
from discord.utils import get


with open("config.json") as config_file:
    config = json.load(config_file)

black_flamingo_discord_id = config['black_flamingo_discord_id']
french_role_id = config['french_role_id']
english_role_id = config['english_role_id']
language_selection_channel_id = config['language_selection_channel_id']
language_selection_message_id = config['language_selection_message_id']

bf_guild = None
french_role = None
english_role = None


def get_bf_guid(bot):
    global bf_guild
    if bf_guild == None:
        bf_guild = get(bot.guilds, id=black_flamingo_discord_id)
    return bf_guild


def get_french_role():
    global french_role
    if french_role == None:
        french_role = get(bf_guild.roles, id=french_role_id)
    return french_role


def get_english_role():
    global english_role
    if english_role == None:
        english_role = get(bf_guild.roles, id=english_role_id)
    return english_role


async def add_language_from_reaction(bot, payload):
    if payload.guild_id == black_flamingo_discord_id and \
            payload.channel_id == language_selection_channel_id and \
            payload.message_id == language_selection_message_id:

        if payload.emoji.name == '🇫🇷':
            bf_guild = get_bf_guid(bot)
            french_role = get_french_role()
            member = get(bf_guild.members, id=payload.user_id)

            await member.add_roles(french_role)

        elif payload.emoji.name == '🇬🇧':
            bf_guild = get_bf_guid(bot)
            english_role = get_english_role()
            member = get(bf_guild.members, id=payload.user_id)

            await member.add_roles(english_role)


async def remove_language_from_reaction(bot, payload):
    if payload.guild_id == black_flamingo_discord_id and \
            payload.channel_id == language_selection_channel_id and \
            payload.message_id == language_selection_message_id:

        if payload.emoji.name == '🇫🇷':
            bf_guild = get_bf_guid(bot)
            french_role = get_french_role()
            member = get(bf_guild.members, id=payload.user_id)

            await member.remove_roles(french_role)

        elif payload.emoji.name == '🇬🇧':
            bf_guild = get_bf_guid(bot)
            english_role = get_english_role()
            member = get(bf_guild.members, id=payload.user_id)

            await member.remove_roles(english_role)