from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/1054388676416782336/a3tSWj9DGXJAzvb2Rz8beoXrmJwowjdtqeZuVuUqq8KXozprrtnDtKZaRJTKtNxzi900')

embed = DiscordEmbed(title = 'DarkGlanceBot', color = 0xffffff)

webhook.add_embed(embed)

response = webhook.execute()