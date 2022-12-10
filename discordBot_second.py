import asyncio
from discord import Intents, Client, Interaction
from discord.app_commands import CommandTree
import flag
import deal_asm as da
import psu
import login_log as login
import config

class MyClient(Client):

    def __init__(self, intents: Intents) -> None:
        super().__init__(intents=intents)
        self.tree = CommandTree(self)

    async def setup_hook(self) -> None:
         await self.tree.sync()

    async def on_ready(self):
        print(f"login: {self.user.name} [{self.user.id}]")


intents = Intents.default()
client = MyClient(intents=intents)
conf = config.Config()

@client.tree.command()
async def start_server(interaction: Interaction):
    """サーバーを起動します"""
    if(not flag.isServer):
        flag.isServer = True
        await interaction.response.send_message('起動コマンドを受け付けました')
        print("start_serverが入力されました")
        da.start_asm()
    else:
        await interaction.response.send_message('既にサーバーが起動しています')

@client.tree.command()
async def stop_server(interaction: Interaction):
    """サーバーを停止します"""
    if(flag.isServer):
        flag.isServer = False
        await interaction.response.send_message('停止コマンドを受け付けました')
        print("stop_serverが入力されました")
        da.save_world()
        await asyncio.sleep(5)
        da.stop_server()
        await asyncio.sleep(7)
    else:
        await interaction.response.send_message('既にサーバーが停止しています')

@client.tree.command()
async def message_all(interaction: Interaction, message: str):
    """(アルファベットのみ)サーバーに入っている人全員にメッセージを送信します"""
    if(flag.isServer):
        print("message_allが入力されました")
        da.message_all(message)
        await interaction.response.send_message("送信されました")
    else:
        await interaction.response.send_message("サーバーが非稼働です")

@client.tree.command()
async def num_of_players(interaction: Interaction):
    """現在のオンラインのプレイヤー数"""
    if(flag.isServer):
        nop = len(login.getLogin_log())-len(login.getLogout_log())
        await interaction.response.send_message('オンラインのプレイヤーは' + str(nop) + '人です') 
    else:
        await interaction.response.send_message("サーバーが非稼働です")

@client.tree.command()
async def get_players_name(interaction: Interaction):
    """現在のオンラインのプレイヤーの名前"""
    if(flag.isServer):
        await interaction.response.send_message(login.getLogin_player()) 
    else:
        await interaction.response.send_message("サーバーが非稼働です")

@client.tree.command()
async def is_server_change(interaction: Interaction):
    """サーバーの実行状態を手動で切り替えます"""
    if interaction.user.id == conf.admin_discord_id:
        if(flag.isServer):
            flag.isServer = False
        else:
            flag.isServer = True
        await interaction.response.send_message("サーバー起動: " + str(flag.isServer))
    else:
        await interaction.response.send_message('このコマンドは管理者のみ使用可能です')

@client.tree.command()
async def pc_resource(interaction: Interaction):
    """pc負荷確認用"""
    resource = "cpu: " + str(psu.get_cpuuse()) + "%, " + "memory: " + str(psu.get_memoryuse()) + "%"
    await interaction.response.send_message(resource) 

client.run(conf.token)
