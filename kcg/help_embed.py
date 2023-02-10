import discord

value_name =  'Fetches the Name of the student \nThis command can be used by all user'
value_marks = 'Fetches Marks of the student \nThis command can be used by all users'
value_registernumber = 'Fetches Register number of the student \nThis command can be used by all users'
value_rollnumber = 'Fetches Roll number of the student \nThis command can be used by all users'
value_dob =  'Fetches the Date of birth of the student \nThis command can be used by authorized users only'
value_photo = 'Fetches the Photo of the student \nThis command can be used by authorized users only'
value_details = 'Fetches Details of the student \nThis command can be used by authorized users only'
value_all = 'Fetches All details of the student(photo, details, marks) together \nThis command can be used by authorized users only'
value_search = 'Searches for students with keyword \nThis command can be used by authorized users only'
value_np = 'Fetches the Name and Photo of the student \nThis command can be used by authorized users only'

embed_description = '''All available commands
Note : This BOT can only handle one request at a time
Some request may take longer time to fetch data because dob cracking is a lengthy process
So Please wait.. It wont take more than a minute in most cases

ALL THE COMMANDS ARE LISTED BELOW'''

help_embed = discord.Embed(title = 'DarkGlanceBot Help',color = 0xffffff, description  = embed_description)
help_embed.add_field(name = '.kcgstudent name <reg_no / roll_no>', value = value_name, inline = False)
help_embed.add_field(name = '.kcgstudent marks <reg_no / roll_no>', value = value_marks, inline = False)
help_embed.add_field(name = '.kcgstudent registernumber <reg_no / roll_no>', value = value_registernumber, inline = False)
help_embed.add_field(name = '.kcgstudent rollnumber <reg_no / roll_no>', value = value_rollnumber, inline = False)
help_embed.add_field(name = '.kcgstudent dob <reg_no / roll_no>', value = value_dob, inline = False)
help_embed.add_field(name = '.kcgstudent photo <reg_no / roll_no>', value = value_photo, inline = False)
help_embed.add_field(name = '.kcgstudent namephoto <reg_no / roll_no>', value = value_np, inline = False)
help_embed.add_field(name = '.kcgstudent details <reg_no / roll_no>', value = value_details, inline = False)
help_embed.add_field(name = '.kcgstudent all <reg_no / roll_no>', value = value_all, inline = False)
help_embed.add_field(name = '.kcgsearch <year> <keyword> <department>', value = value_search, inline = False)
help_embed.set_footer(text = 'DarkGlanceBOT is just made for educational/testing purpose, So please don\'t misuse')