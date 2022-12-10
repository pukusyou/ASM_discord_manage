import configparser
import re

class Config:

    def __init__(self):
        config_ini = configparser.ConfigParser()
        config_ini.read('config.ini', encoding='utf-8')
        self.config = config_ini['setting']

    @property
    def token(self):
        return self.config.get('token')

    @property
    def admin_discord_id(self):
        return self.config.getint('admin_discord_id')

    @property
    def admin_password(self):
        return self.config.get('admin_password')

    @property
    def rcon_port(self):
        return self.config.getint('rcon_port')
    
    @property
    def comandline_path(self):
        return self.config.get('comandline_path')

    @property
    def log_path(self):
        log_str = self.config.get('log_path')
        if(log_str == ''):
            logpath = re.findall(r'(.*)Binaries', self.comandline_path)
            log_str = logpath[0] + 'Saved\Logs'
        return log_str
