from typing import List

import discord
from discord import Guild


def get_all_users_with_role(interaction: discord.Interaction, role_name: str) -> List[str]:
    server = interaction.guild
    role_id = server.roles[0]
    for role in server.roles:
        if role_name == role.name:
            role_id = role
            break
    users = []
    for member in server.members:
        if role_id in member.roles:
            users.append(member.display_name)
    return users


def get_role_id_by_name(server: Guild, role_name: str) -> int | None:
    for role in server.roles:
        if role_name == role.name:
            return role.id
