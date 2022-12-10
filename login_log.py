import os
import re
import glob
import config

conf = config.Config()

def getLogin_log():
    filename = glob.glob(conf.log_path + '\ServerGame.*.????.??.??_??.??.??.log')
    filename.sort(key=os.path.getmtime,reverse=True)
    login_players = []
    f = open(filename[0], 'r', encoding='utf-8')   
    data = f.readlines()     
    for str in data:
        if(str.find("ログインしました")!= -1):
            login_player = re.findall(': (.*)がARKにログインしました', str)
            str_login_player = ''.join(login_player)
            login_players.append(str_login_player)
    return login_players

def getLogout_log():
    filename = glob.glob(conf.log_path + '\ServerGame.*.????.??.??_??.??.??.log')
    filename.sort(key=os.path.getmtime,reverse=True)
    f = open(filename[0], 'r', encoding='utf-8')
    data = f.readlines()
    logout_players = []
    for str in data:
        if(str.find("ログアウトしました")!= -1):
            logout_player = re.findall(': (.*)がARKからログアウトしました', str)
            str_logout_player = ''.join(logout_player)
            logout_players.append(str_logout_player)
    return logout_players

def getLogin_player():
    login_players = getLogin_log()
    logout_players = getLogout_log()
    name_str = ''
    for out_player in logout_players:
        if(out_player in login_players):
            login_players.remove(out_player)
    name_str = ', '.join(login_players)
    if(len(login_players)==0):
        name_str = 'オンラインのプレイヤーはいません'
    return name_str