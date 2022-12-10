from mcrcon import MCRcon
import config
import subprocess

conf = config.Config()
comandline_path = conf.comandline_path
admin_password = conf.admin_password
rcon_port = conf.rcon_port

def start_asm():
    subprocess.Popen(comandline_path,shell=True)

def stop_server():
    with MCRcon("localhost", admin_password, rcon_port) as mcr:
        mcr.command("DoExit")

def message_all(message):
    with MCRcon("localhost", admin_password, rcon_port) as mcr:
        str = "Broadcast " + message
        print(str)
        mcr.command(str)

def save_world():
    with MCRcon("localhost", admin_password, rcon_port) as mcr:
        mcr.command("SaveWorld")