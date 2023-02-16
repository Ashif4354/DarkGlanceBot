import discord
from discord.ext import commands
from Student import student, server_down, NoPhoto
from os import getcwd,remove
from datetime import date, datetime

from sys import path
path.append(getcwd().rstrip('kcg'))
from logger.logger import logger
from darkglance import *

client = commands.Bot(command_prefix = '.')

departments = {
            'ad' : ('ad', 'aids',) , 
            'ae' : ('ae', 'aero', 'aeronautical') ,
            'ao' : ('ao', 'aerospace', 'ase') ,
            'at' : ('at', 'auto', 'automobile') ,
            'ce' : ('ce', 'civil',) ,
            'cs' : ('cs', 'cse','computer'),
            'ec' : ('ec', 'ece'),
            'ee' : ('ee', 'electrical', 'eee'),
            'ei' : ('ei', 'eie', 'instrumentation'),
            'ft' : ('ft', 'fashion'),
            'it' : ('it', 'info'),
            'mc' : ('mc', 'mechatronics', 'mechatronic'),
            'me' : ('me', 'mech', 'mechanical')
            }

fees_url = 'http://studentonlinepayment.kcgcollege.ac.in/'

fees_login_payload = {
    '__EVENTTARGET' : '' ,
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__VIEWSTATE' : '/wEPDwUKMTQ4NjQwMTIzNw9kFgICAw9kFgoCCQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQhjb2xsbmFtZR4ORGF0YVZhbHVlRmllbGQFDGNvbGxlZ2VfY29kZR4LXyFEYXRhQm91bmRnZBAVARlLQ0cgQ29sbGVnZSBvZiBUZWNobm9sb2d5FQECMTMUKwMBZxYBZmQCCw8QZBAVAgtSb2xsIE51bWJlcg9SZWdpc3RlciBOdW1iZXIVAgEwATEUKwMCZ2cWAWZkAg0PD2QWBB4LcGxhY2Vob2xkZXIFC1JvbGwgTnVtYmVyHgxhdXRvY29tcGxldGUFA29mZmQCEQ8PFgIeB1Zpc2libGVoFgIfBAUDb2ZmZAIVDw8WAh8FaGRkZNW+28hPSHWELbHwTZyc+FgrCQj/p6TzJx0gJo3tNhyA', 
    '__VIEWSTATEGENERATOR' : 'CA0B0334',
    '__EVENTVALIDATION' : '/wEdAAa5cfVM3pWzdu9rE2vQn04A1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+c34O/GfAV4V4n0wgFZHr3fbr4+GviYj6YKdFlGPdh5Q23daRHDXkik+zyEsEtmUSg==',
    'rblOnlineAppLoginMode' : '0',
    'txtuname' : None,
    'Button1' : 'Login'
    }


@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to fetch all")

@client.command(aliases = ['fs', 'fetch'])
async def fetchstudents(ctx): #.fetchstudents 2020 cse
    logger.input_kcg(ctx, getcwd().rstrip('kcg') + '\logger') 

    if not await check_auth(ctx, ('owner','admin')):
        return
    command = ctx.message.content.split()

    try:
        if len(command[1]) == 4 and int(command[1]) in range(2012, date.today().year + 1):
            batch = str(int(command[1]) % 100)
        else:
            raise Exception
    except:
        embed = discord.Embed(title = 'Invalid Year / Invalid Input', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    depts = command[2:]
    
    try:
        if depts[0].lower() in ('all', '*'):
            depts = ['all']
            if not await check_auth(ctx, ('owner',), 'You are not authorized to search all departments'):
                return
    except IndexError:
        pass

    depts_ = str(depts).strip("[]").replace("'", ' ')
    embed = discord.Embed(title = 'Fetching started..', description =  f'Batch : {batch}\nDepartments : {depts_}', color = 0xffffff)
    await ctx.send(embed = embed)

    date_time = datetime.now().strftime("%d-%m-%Y %H;%M;%S")

    log_path = f'{getcwd().rstrip("kcg")}\logger\\kcg_logs\\fetchstudlogs\\'

    file = open(f'{log_path}[{date_time}]   {batch} {depts}.log', 'a')
    file.write(f'FETCH LOG for  {batch} {depts}\n')
    file.write(f'Requested by {ctx.message.author}\n\n')

    corrected_depts = []
    length = 0
    traverse_count = 1
    
    try:
        if depts[0] == 'all':
            corrected_depts = departments.keys()
        else:
            for element in depts:
                for dept_ in departments:
                    if element.lower() in departments[dept_]:
                        if dept_ not in corrected_depts:
                            corrected_depts.append(dept_)
    except IndexError:
        pass

    file.write(f'\nCorrected departments  :  {corrected_depts}\n')

    def check_student_rollno(user_id):
        fees_login_payload['txtuname'] = user_id    
        #print(user_id)
        try:
            page = requests.post(fees_url, data = fees_login_payload, timeout = 10)
            if page.url != fees_url:
                return True    
            return False
        except Exception as text:
            logger.exception_logs('dgb/kcg/fetchstud_module/fetchstudents/check_student_rollno LINE117', text, getcwd().rstrip('kcg') + 'logger')
            file.close()
            raise server_down
        
    def add_zero(value, length):
        value_len = len(value)
        req_len = length - value_len
        value = req_len * '0' + value

        return value

    for dept in corrected_depts:  
        student_count = 0          

        file.write(f'\n\nSearching in dept {dept}\n')
        if check_student_rollno(batch + dept + '1'):
            length = 1
            file.write(f"roll number format found out to be  :  {batch + dept + '1'}")
            
        elif check_student_rollno(batch + dept + '01'):
            length = 2
            file.write(f"roll number format found out to be  :  {batch + dept + '01'}")
            
        elif check_student_rollno(batch + dept + '001'):
            length = 3
            file.write(f"roll number format found out to be  :  {batch + dept + '001'}")    

        num = 1
        None_count = 0

        file.write('\n\n')

        while None_count < 5:
            The_roll_no = batch + dept + add_zero(str(num), length)

            student_ = student.get_np(The_roll_no)
            
            if not student_ == None:
                name = student_[0]

                embed = discord.Embed(title = The_roll_no, description = name, color = 0xffffff)
                student_count += 1
                file.write(f'{traverse_count}  {student_count}  {The_roll_no}  {name}')

                if student_[1]:
                    photo = r"{}\temp_pics\{}_photo.png".format(getcwd().rstrip('kcg'), The_roll_no)

                    pic = discord.File(photo, filename = 'temp_photo.png')
                    embed.set_image(url = 'attachment://temp_photo.png')            
            
                    await ctx.send(embed = embed, file = pic)
                    file.write(' (FETCHED)\n')
                    remove(photo)

                else:
                    embed.set_footer(text = 'Photo not found')
                    await ctx.send(embed = embed)
                    file.write('                             (NOT FETCHED)\n')

            else:
                None_count += 1
                file.write(f'{traverse_count}  {The_roll_no}  (no student)\n')
            
            num += 1
            traverse_count += 1
    
    file.close()
    embed = discord.Embed(title = '..FETCHING DONE', color = 0xffffff)
    await ctx.send(embed = embed)

    logger.output_kcg(getcwd().rstrip('kcg') + '\logger', 'Fetch successful')


@client.command()
async def stopbot(ctx):
    logger.input_kcg(ctx, getcwd().rstrip('kcg') + '\logger')
    
    if not await check_auth(ctx, ('owner',)):
        return

    exit(0)










############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################