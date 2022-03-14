from discord_webhook import DiscordWebhook, DiscordEmbed

url = "https://discord.com/api/webhooks/879777116927950858/zLDTtIJRZ-LlFTLQvMfOD-4K2WNzMy26BWIDjhGKvu3ey4sGwBkEMo8aEwbctR-x-s2B"

webhook = DiscordWebhook(url=url)


embed = DiscordEmbed(
    title="Embed Title", description="Your Embed Description", color='03b2f8'
)
embed.set_author(
    name="Author Name",
    url="https://github.com/lovvskillz",
    icon_url="https://avatars0.githubusercontent.com/u/14542790",
)
embed.set_footer(text="Embed Footer Text")
embed.set_timestamp()
# Set `inline=False` for the embed field to occupy the whole line
embed.add_embed_field(name="Type", value="Lorem ipsum", inline=False)
embed.add_embed_field(name="Site", value="dolor sit", inline=False)
embed.add_embed_field(name="Sizes", value="amet consetetur")
embed.add_embed_field(name="QT", value="sadipscing elitr")
embed.add_embed_field(name="Links", value="sadipscing elitr")

webhook.add_embed(embed)
response = webhook.execute()
