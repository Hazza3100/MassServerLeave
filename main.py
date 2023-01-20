import os
import requests
from   colorama import *

class Cleaner:
    def __init__(self, token):
        self.guildSum  = 0
        self.dontLeave = ['930833528747347989', '997553221771997322']
        self.token     = token
        self.session   = requests.Session()

    def leave(self):
        try:
            with self.session as session:
                headers = {'authority'         : 'discord.com','accept'            : '*/*','accept-language'   : 'en-GB,en-US;q=0.9,en;q=0.8','authorization'     : self.token,'referer'           : 'https://discord.com','sec-ch-ua'         : '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile'  : '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest'    : 'empty','sec-fetch-mode'    : 'cors','sec-fetch-site'    : 'same-origin','user-agent'        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','x-debug-options'   : 'bugReporterEnabled','x-discord-locale'  : 'en-GB','x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTY4OTcyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',}
                guilds = session.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
                for guild in guilds:
                    if guild['id'] in self.dontLeave:
                        pass
                    else:
                        response = session.delete(f"https://discord.com/api/v9/users/@me/guilds/{str(guild['id'])}", json={'lurking': False,}, headers=headers)
                        if response.status_code == 204:
                            print(f"[{Fore.GREEN}+{Fore.RESET}] Left ['{Fore.YELLOW}{guild['id']}{Fore.RESET}']")
                            self.guildSum += 1
                        else:
                            print(f"[{Fore.RED}-{Fore.RESET}] Error ['{Fore.RED}{guild['id']}{Fore.RESET}']")
                print(f"[{Fore.LIGHTMAGENTA_EX}!{Fore.RESET}] Finished all tasks ['{Fore.YELLOW}{self.guildSum}{Fore.RESET}']")
        except:
            pass

os.system('cls')
Cleaner(input("Account token: ")).leave()
