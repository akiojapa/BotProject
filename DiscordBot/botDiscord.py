
import random

import database.database
import discord

from discord.ext import commands

intents = discord.Intents.all()
intents.members = True




class MyClient(commands.Bot):

    bot = commands.Bot(command_prefix='!', intents=intents)

    # Bot prefix

    db = database.database.Database()

    consultCommand = db.consult('commands')

    consultUser = db.consult('user')

    # Tic Tac Toe configuration
    player1 = ""
    player2 = ""
    turn = ""
    gameover = True

    board = []

    wincondition = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # End Tic Tac Toe configuration


    async def ShowPoint(self):
        channel = self.get_channel(1024341823533109270)
        auxpoint = 0
        auxuser = ''
        for i in self.consultUser:
            if i[3] > auxpoint:
                auxpoint = i[3]
                auxuser = str(i[1])

        if auxpoint == 0:
            embed = discord.Embed(title=f"Maior número de vitórias no jogo da velha:",
                                  description=f"Campeão atual: {auxuser}\n\n"
                                              f"Total de vitórias: {auxpoint}")
        else:
            embed = discord.Embed(title=f"Maior número de vitórias no jogo da velha:",
                                  description="Ainda não há campeões, venha ser o primeiro!")

        await channel.send(embed=embed)


    async def on_member_join(self, member):
        channel = self.get_channel(1024341823533109270)
        embed = discord.Embed(title=f"Bem-Vindo {member.name}",
                              description=f"Obrigado por ser juntar ao {member.guild.name}!\n\n"
                                          f"Espero que goste de passar seu tempo aqui!")
        data = {
            member.name,
            member.id
        }
        self.db.CreateUser(data)

        await channel.send(embed=embed)

    @bot.event
    async def on_ready(self):
        print('logged on as {0}!'.format(self.user))

    # def add_commands(self):
    #     @self.command(name="testing", pass_context=True)

    bot.load_extension("cog")


    # @bot.event
    # async def on_message(self, message):
    #     channel = self.get_channel(1024341823533109270)
    #     print(f'Message from {message.author}: {message.content}')
    #
    #     for i in self.consultCommand:
    #         if message.content == i[1]:
    #             # if i[1] == '$tictactoe':
    #             await message.channel.send(str(i[2]).replace('Autor', str(message.author.name)))



    @bot.command()
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
        global player1
        global player2
        global turn
        global gameover
        global count
        global board

        if gameover:
            board = [
                ":white_large_square", ":white_large_square", ":white_large_square",
                ":white_large_square", ":white_large_square", ":white_large_square",
                ":white_large_square", ":white_large_square", ":white_large_square"
            ]

        turn = ""
        gameover = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send(f"<@{str(player1.id)} é o seu turno!>")
        elif num == 2:
            turn = player2
            await ctx.send(f"<@{str(player2.id)} é o seu turno!")
        else:
            await ctx.send("O jogo já está rolando!")


    async def on_place(self, ctx, pos: int):
        global turn
        global player1
        global player2
        global count
        global gameover
        global board

        if not gameover:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                    board[pos - 1] = mark
                    count += 1

                    # print the board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]

                    self.checkWinner(self.wincondition, mark)
                    print(count)
                    if gameover == True:
                        self.db.AttPoints(1, turn)
                        await ctx.send(mark + " Venceu!!")
                    elif count >= 9:
                        gameover = True
                        await ctx.send("Deu velha!")

                    # switch turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await ctx.send("Escolha um número entre 1 e 9 apenas, utilizando !place {número do quadrado} ")
            else:
                await ctx.send("Ainda não é seu turno")
        else:
            await ctx.send("Inicie um novo game utilizando o comando !tictactoe(@jogador1, @jogador2)")

    def checkWinner(wincondition, mark):
        global gameover
        for condition in wincondition.wincondition:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameover = True


client = MyClient(command_prefix='!', intents=intents)



client.run('MTAyNDM0MzcyNDA2ODcwNDI1Ng.GUJIn5.Vg51SW6lEXSeJUqbyBLcpO7NKs4J32kzio1PzE')
