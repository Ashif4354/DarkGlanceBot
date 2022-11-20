from datetime import datetime


class logger:
    
    def discord_input_kcg(command, path):
        author = str(command.message.author)
        text = command.message.content
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        with open('{}\discord_input_kcg.txt'.format(path), 'a') as file:

            log = date_time + ' ' + author + '  ' + text + '\n'
            file.write(log)
    def discord_file_output_kcg(path, file_name):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        with open('{}\discord_file_output.txt'.format(path), 'a') as file:            

            log = date_time + ' ' + file_name
            file.write(log)
