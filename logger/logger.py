from datetime import datetime


class logger:
    def discord_input_kcg(command, path, text):
        author = str(command.message.author)
        text = command.message.content
        
        with open('{}\discord_input_kcg.txt'.format(path), 'a') as file:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            log = date_time + ' ' + author + '  ' + text + '\n'
            file.write(log)
