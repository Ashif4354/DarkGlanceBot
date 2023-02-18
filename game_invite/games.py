from os import getcwd
from random import randint
import discord

from os import getcwd
from sys import path
path.append(getcwd().rstrip('game_invite'))
from darkglance import *

games_ = {
    'VALORANT' : (('valo', 'valorant'), 7, "{}\images\\valorant ({}).jpg"),
    'SUPER_SUS' : (('super','super sus', 'supersus'), 5, "{}\images\Super sus ({}).jpg"),
    'AMONG_US' : (('among', 'amongus', 'among us'), 4, "{}\images\Among us ({}).jpg")
}

def get_image(game_name, path):
    num = randint(1, games_[game_name][1])
    
    return games_[game_name][2].format(path, num)    

async def send_invite(ctx, game_name, path = getcwd()):
    image = get_image(game_name, path)

    embed = discord.Embed(title = 'GAME INVITE',color = 0xffffff)
    pic = discord.File(image, filename = f'{game_name}.png')
    embed.set_image(url = f'attachment://{game_name}.png')
    embed.add_field(name = 'Come on guys', value = f'LETS PLAY {game_name.replace("_", " ")} yoo..', inline = False)
    await ctx.send(embed = embed, file = pic)

async def game_invite_(ctx):
    global games_
    command = ctx.message.content.split()

    try:
        game_name = command[1]
        
        for game in games_:
            if game_name in games_[game][0]:
                game_name = game
                break
        else:
            raise GameNotAvailable
            
    except IndexError:
        embed = discord.Embed(description = 'No game mentioned', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    except GameNotAvailable:
        embed = discord.Embed(description = 'This game invite not available yet', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    
    await send_invite(ctx, game_name, path = getcwd() + '\game_invite')



#get_image('valorant', path = getcwd())