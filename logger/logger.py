from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
file_path = None

class logger:
    def complete_log(path, mode, text):
        with open('{}\complete_log.log'.format(path), 'a') as file:
            log = text[:20] + mode + text[20:]
            file.write(log)
    
    def discord_input_kcg(command, path):
        global file_path
        flie_path = path

        author = str(command.message.author)
        text = command.message.content
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/1054388676416782336/a3tSWj9DGXJAzvb2Rz8beoXrmJwowjdtqeZuVuUqq8KXozprrtnDtKZaRJTKtNxzi900')
        embed = DiscordEmbed(title = 'DarkGlanceBot', description = 'Request recieved..', color = 0xffffff)
        embed.add_embed_field(name = f'{author} requested', value = text, inline = False)
        webhook.add_embed(embed)
        response = webhook.execute()

        with open('{}\discord_input_kcg.log'.format(path), 'a') as file:
            log = '\n' + date_time + ' ' + author + '  ' + text + '\n'
            file.write(log)
            logger.complete_log(path, '  INPUT  ', log)

    def discord_output_kcg(path, text):
        global file_path
        file_path = path

        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
         
        with open('{}\discord_output.log'.format(path), 'a') as file:   
            log = date_time + ' ' + text + '\n'
            file.write(log)
            logger.complete_log(path, ' OUTPUT  ', log + '\n')
    
    
