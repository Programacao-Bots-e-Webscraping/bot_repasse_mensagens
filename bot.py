from telethon import TelegramClient,sync,events
from time import sleep
import requests
from senhas import api_hash,api_id 

sessao = 'Repassar Mensagem'
  
def main():
    print('Monitoramento iniciado ...')
    client = TelegramClient(sessao, api_id, api_hash)
    @client.on(events.NewMessage(chats = [4118772142))
    async def enviar_mensagem(event):
        if event.media:
            await client.send_file(-4183296275,file = event.media,
                                   caption=event.raw_text.replace('http://www.seinscrevanocanal.com.br','http://www.deixeseulike.com.br'))
        else:
            await client.send_message(-4183296275,event.raw_text.replace('http://www.seinscrevanocanal.com.br','http://www.deixeseulike.com.br'))
    client.start()
    client.run_until_disconnected()
    
main()
