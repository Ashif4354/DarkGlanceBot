from os import getcwd
from random import randint
import discord

games = {
    'VALORANT' : (('valo', 'valorant'), 7, "{}\images\\valorant ({}).jpg"),
    'SUPER_SUS' : (('super','super sus', 'supersus'), 5, "{}\images\Super sus ({}).jpg"),
    'AMONG_US' : (('among', 'amongus', 'among us'), 4, "{}\images\Among us ({}).jpg")
}

def get_image(game_name, path):
    num = randint(1, games[game_name][1])
    
    return games[game_name][2].format(path, num)    

async def send_invite(ctx, game_name, path = getcwd()):
    image = get_image(game_name, path)

    embed = discord.Embed(title = 'GAME INVITE',color = 0xffffff)
    pic = discord.File(image, filename = f'{game_name}.png')
    embed.set_image(url = f'attachment://{game_name}.png')
    embed.add_field(name = 'Come on guys', value = f'LETS PLAY {game_name.replace("_", " ")} yoo..', inline = False)
    await ctx.send(embed = embed, file = pic)


#get_image('valorant', path = getcwd())