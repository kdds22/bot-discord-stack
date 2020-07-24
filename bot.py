import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

from stackapi import StackAPI

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print(f'{bot.user.name} entrou no Discord!')


@bot.command(name='ajuda', help='Mostra uma breve INFO do Dr. Dev')
async def ajuda(ctx):
    ajuda_respostas = [
        'Sou o Dr. Dev, e meu trabalho aqui é te ajudar (ou tentar pelo menos)\n '+
        'Use \'$\' no inicio pra chamar minha atenção;\n '+
        'Se quiser ver a lista de comandos use: $howto',
        'Espere ai rapidinho... estou codando um troço aqui....',
        'Chego já, to subindo o JBoss...',
        'Estou dando um commit aqui nas mudanças, pere...'
    ]

    response = random.choice(ajuda_respostas)
    await ctx.send(response)


@bot.command(name='howto', help='Mostra a lista de comandos do Dr. Dev')
async def howto(ctx):
    response = '''
        Por enquanto só existe esses 2 (dois): \n
        **$ajuda** = Diz pra que eu sirvo; \n
        **$howto** = Mostra essa lista de comandos \n
        **$rolar_dado** = Simula uma rolagem de dado, escolhendo a quantidade e o tipo de dado \n\n
        -->> tem o *$help*, mas ele é padrão... pode ignora-lo se desejar <<--
    '''
    await ctx.send(response)


@bot.command(name='rolar_dado', help='Simula uma rolagem de dados (params: [quantidade, tipo] \nEx.: \'$rolar_dado 2 6\' == 2 dados de 6 lados)')
async def rolar(ctx, quantidade: int, lados: int):
    dado = [
        str(random.choice(range(1, lados + 1)))
        for _ in range(quantidade)
    ]
    if str(dado[0]) == str(lados):
        await ctx.send(', '.join(dado) + ' CRITICO!! ')
    else: await ctx.send(', '.join(dado))


bot.run(TOKEN)


'''
@client.event
async def on_ready():
    print(f'{client.user.name} entrou no Discord!!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    stack_bot_respostas = [
        'Pergunta qualquer coisa ai, talvez eu ajude!',
        'Não consegue né Moisés? Pergunta ai.',
        'Ta com medinho? Pediu arrego? É so me chamar.',
        'Preguiça o nome disso né? Pergunte logo!'
    ]

    if message.content == 'vish!':
        response = random.choice(stack_bot_respostas)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


client.run(TOKEN)
'''