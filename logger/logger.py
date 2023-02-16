from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed
file_path = None

class logger:
    def complete_log(path, mode, text):
        with open('{}\complete_log.log'.format(path), 'a') as file:
            log = text[:20] + mode + text[20:]
            file.write(log)
    
    def input_kcg(command, path):
        global file_path
        flie_path = path

        author = str(command.message.author)
        text = command.message.content
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/1054388676416782336/a3tSWj9DGXJAzvb2Rz8beoXrmJwowjdtqeZuVuUqq8KXozprrtnDtKZaRJTKtNxzi900')
        embed = DiscordEmbed(title = 'DarkGlanceBot', description = 'KCG Request..', color = 0xffffff)
        embed.add_embed_field(name = f'{author}', value = text, inline = False)
        webhook.add_embed(embed)
        response = webhook.execute()

        with open('{}\kcg_logs\input_kcg.log'.format(path), 'a') as file:
            log = '\n' + date_time + ' ' + author + '  ' + text + '\n'
            file.write(log)
            logger.complete_log(path, '  INPUT  ', log)

    def output_kcg(path, text):
        global file_path
        file_path = path

        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
         
        with open('{}\kcg_logs\output_kcg.log'.format(path), 'a') as file:   
            log = date_time + ' ' + text + '\n'
            file.write(log)
            logger.complete_log(path, ' OUTPUT  ', log + '\n')

    def input_sms_blast(command, path):
        global file_path
        flie_path = path
    
        author = str(command.message.author)
        text = command.message.content
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/1054388676416782336/a3tSWj9DGXJAzvb2Rz8beoXrmJwowjdtqeZuVuUqq8KXozprrtnDtKZaRJTKtNxzi900')
        embed = DiscordEmbed(title = 'DarkGlanceBot', description = 'SMS Blast Request..', color = 0xffffff)
        embed.add_embed_field(name = f'{author}', value = text, inline = False)
        webhook.add_embed(embed)
        response = webhook.execute()

        with open('{}\smsblaster_logs\input_sms_blast.log'.format(path), 'a') as file:
            log = '\n' + date_time + ' ' + author + '  ' + text + '\n'
            file.write(log)
            logger.complete_log(path, '  INPUT  ', log)
    
    def exception_logs(loc, text, path):
        text = str(text)
        print(text)
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        with open('{}\exception_logs.log'.format(path), 'a') as file:   
            log = date_time + ' ' + loc + '|' + text + '\n'
            file.write(log)

        webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/1075077654543347855/xWUZIFQYx4VMMq6bpP-zOww_CGK63xbTWCZCBprNjg36ARJB9DRPRb1rfDd5ujbqp0Tl')
        embed = DiscordEmbed(title = 'DarkGlanceBot', color = 0xffffff)
        embed.add_embed_field(name = f'Exception in {loc}', value = text, inline = False)
        webhook.add_embed(embed)
        response = webhook.execute()
         
        

