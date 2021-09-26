import discord
import os
import datetime
import shutil
import inputimeout
import  asyncio
from inputimeout import inputimeout, TimeoutOccurred
from colorama import init, Fore

print(Fore.GREEN + f"[-] INSIRA SUA TOKEN ABAIXO: [-]")
token = input(Fore.RED + "[-]      Token: " + Fore.RESET)

width = shutil.get_terminal_size().columns


print(" ")
print(Fore.RED + f"PREFIXO")
prefix = (".")


os.system('cls')

msg = f""".d8888. d88888b  .o88b.  .d88b.  d8b   db d8888b. 
88'  YP 88'     d8P  Y8 .8P  Y8. 888o  88 88  `8D 
`8bo.   88ooooo 8P      88    88 88V8o 88 88   88 
  `Y8b. 88~~~~~ 8b      88    88 88 V8o88 88   88 
db   8D 88.     Y8b  d8 `8b  d8' 88  V888 88  .8D 
`8888Y' Y88888P  `Y88P'  `Y88P'  VP   V8P Y8888D
"""

print(" ")
class MyClient(discord.Client):
  async def on_connect(self):
    os.system('clear')
    print(Fore.RED + msg)
    print(Fore.RED + "[-] ----------------------------- / ---------------------------- [-]".center(width))
    print(Fore.YELLOW + f"[-] SISTEMA DELETE MESSAGES - POWERED BY: @Second 爱#9649 [-]".center(width))
    print(Fore.RED + f"[-] PREFIXO - AJUDA = {prefix}help [-]".center(width))
    print("     ")
    print(Fore.RED + "[-] ----------------------------- / ---------------------------- [-]".center(width))
    print("     ")
    

  async def on_message(self, message):
    if message.author != client.user:
      return
    if message.content == f"{prefix}help":
      await help(message)
    if message.content == f"{prefix}cl":
      await channelclear(message)


async def logout(message):
  await message.delete()
  await client.logout()
  print(f"\n Cliente Logado com Sucesso!")


async def help(message):
  await message.delete()
  emHelp = discord.Embed(
    description = f"""
**
[-] {prefix}help
Mostra esta mensagem.
 
[-] {prefix}cl
Limpar suas mensagens no canal.
**
    """, colour=0x9400D3)
    
  emHelp.set_author(name = "Comandos", icon_url = client.user.avatar_url, url = "https://media.discordapp.net/attachments/820955486606196736/832416377444499506/36b87512eb2ac4dd49550b6c00a2c86a.png")
  emHelp.set_footer(text = "Powered By Second#0044")
  try:
    await message.channel.send(embed = emHelp)
  except:
    await message.channel.send(
    f"""
**
[-] {prefix}help
Mostra esta mensagem.
 
[-] {prefix}cl
Limpar suas mensagens no canal.
**
""",
     delete_after = 30
    )

async def channelclear(message):
  await message.delete()
  print(Fore.RED + f"Deletando mensagens, Por favor aguarde...")
  async for message in message.channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      await asyncio.sleep(0.5)
      await message.delete()
      print(f"{Fore.CYAN} [-] {message}{Fore.RESET}\n ")
  print(Fore.RED + "Tarefa Concluida!\n")

client = MyClient()
try:
  client.run(token, bot = False)
except discord.LoginFailure:
  print(f"Falha no login [Invalid token]")
except discord.HTTPException:
  print(f"Falha no login! [Unknown Error]")