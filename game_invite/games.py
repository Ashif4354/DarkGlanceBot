from os import getcwd
from random import randint
import discord

games = {
    'Valorant' : ('valo', 'valorant'),
    'Super Sus' : ('super','super sus', 'supersus'),
}

total_images = {
    'Valorant' : 7,
    'Super Sus': 5
}

def get_image(game_name, path):
    num = randint(1, total_images[game_name])

    game_images = {
        'Valorant' : "{}\images\\valorant ({}).jpg".format(path, num),
        'Super Sus' : "{}\images\Super sus ({}).jpg".format(path, num)   
    }

    return game_images[game_name]
    

async def send_invite(ctx, game_name, path = getcwd()):
    image = get_image(game_name, path)

    embed = discord.Embed(title = 'GAME INVITE',color = 0xffffff)
    pic = discord.File(image, filename = 'temp_photo.png')
    embed.set_image(url = 'attachment://temp_photo.png')
    embed.add_field(name = 'Come on guys', value = f'LETS PLAY {game_name} yoo..', inline = False)
    await ctx.send(embed = embed, file = pic)


#get_image('valorant', path = getcwd())