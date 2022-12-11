from datetime import datetime
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

        with open('{}\discord_input_kcg.log'.format(path), 'a') as file:
            log = '\n' + date_time + ' ' + author + '  ' + text + '\n'
            file.write(log)
            logger.complete_log(path, '  INPUT  ', log)

    def discord_output_kcg(path, file_name):
        global file_path
        file_path = path

        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
         
        with open('{}\discord_output.log'.format(path), 'a') as file:   
            log = date_time + ' ' + file_name + '\n'
            file.write(log)
            logger.complete_log(path, ' OUTPUT  ', log + '\n')
    
    
