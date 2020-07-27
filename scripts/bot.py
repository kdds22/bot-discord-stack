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
        **$opcoes** = Mostra uma lista das principais questões de algum tema do StackOverFlow e algumas especificidades\n\n
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


#TODO: converter o &amp;
#TODO: liberdade de escolher a pagina (questões anteriores/posteriores)
@bot.command(name='opcoes', help='Mostra questionamentos sobre um tema\n- (params: [tema, palavrasChave]\n- Ex.: \'$opcoes python face-recognition,opencv\' )')
async def opcoes(ctx, tema: str, params: str = ''):
    tags = tema
    if params != '':
        spliteed = params.split(',')
        for x in spliteed:
            tags += ';'+x
    SITE = StackAPI('stackoverflow')
    questions = SITE.fetch('questions', sort='activity', tagged=tags)
    #print(len(questions['items']))
    response = 'Total: '+str(len(questions['items']))+'\nMostrando os primeiros resultados...\n\n'
    count = 0
    for x in questions['items']:
        if count >= 10:
            break
        response += str(x['title']).replace('&#39;','\'')+' >> id: ' + str(x['question_id']) + '\n\n'
        #print(str(x['title']).replace('&#39;','\'')+' >> id: ' + str(x['question_id']))
        count += 1

    await ctx.send(response)



bot.run(TOKEN)
