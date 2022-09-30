import os
import json, requests
import discord
from discord.ext import commands

from DiscordBot.database.database import Database


def main():
    # ------------------------------------------- Initial Config ------------------------

    # API config
    def getAPI(user=''):
        respose = requests.get(f"https://api.github.com/users/{user}")
        json_data = json.loads(respose.text)
        return json_data
    #

    # DB Config
    db = Database()
    consultCommand = db.consult('commands')
    # Db config ENd

    # Discord bot Configuration
    intents = discord.Intents.all()
    intents.members = True

    client = commands.Bot(command_prefix="$", intents=intents)

    # Discord bot Configuration End

    # Start the Bot
    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to Discord.")

    # Welcome message!
    @client.event
    async def on_member_join(member):
        channel = client.get_channel(1024341823533109270)
        embed = discord.Embed(title=f"Bem-Vindo {member.name}",
                              description=f"Obrigado por ser juntar ao {member.guild.name}!\n\n"
                                          f"Espero que goste de passar seu tempo aqui!\n\n"
                                          f"Digite $commands para ficar por dentro!")
        data = {
            member.name,
            member.id
        }
        db.CreateUser(data)

        await channel.send(embed=embed)

    @client.command()
    async def test(ctx: commands.Context):
        await ctx.send("Testando")

    @client.event
    async def on_message(message):
        print(f'Message from {message.author}: {message.content}')

        for i in consultCommand:
            if message.content == str(i[1]):
                await message.channel.send(str(i[2]).replace('Autor', str(message.author.name)))

        await client.process_commands(message)

    @client.command(pass_context=True)
    async def github(ctx):

        dev = str(ctx.message.content)[8:]

        print(dev)

        data = getAPI(dev)

        if len(data) < 4:
            await ctx.send("Usuário não encontrado!")
        else:
            embed = discord.Embed(title=f"Usuário: {data['html_url']}",
                                  description=f"NickName: {data['login']}\n\n"
                                              f"Nome: {data['name']}\n\n"
                                              f"Localidade:{data['location']}\n\n"
                                              f"Seguidores: {data['followers']}\n\n"
                                              f"Seguindo: {data['following']}\n\n"
                                              f"Biografia: {data['bio']}")

            embed.set_thumbnail(
                url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fgithub.com%2Flogos&psig'
                    '=AOvVaw1yQR4zojLqIzoCP25rds0T&ust=1664652313427000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLjz_J'
                    '-fvfoCFQAAAAAdAAAAABAS')
            embed.set_image(url=data['avatar_url'])

            await ctx.send(embed=embed)

    for item, value in os.environ.items():
        print('{}: {}'.format(item, value))

    client.run(os.getenv('MTAyNDM0MzcyNDA2ODcwNDI1Ng.GUJIn5.Vg51SW6lEXSeJUqbyBLcpO7NKs4J32kzio1PzE'))


if __name__ == '__main__':
    main()
