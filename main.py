import discord
import random
from decouple import config
from time import sleep
from phrases.triggers import *
from phrases.answers import *
from funcs.utils import *
from funcs.ai_utils import *


DISCORD_TOKEN = config('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)

#уведомление о ВХОДЕ
@client.event
async def on_ready():
    print('Мы вошли как {0.user}'.format(client))

#новый ЧЛЕН
@client.event
async def on_member_join(member):
    print(f'я заметила, что зашел новый член, это {member.name}')
    main_channel = client.get_channel(428262608664264726)
    async with main_channel.typing():
      sleep(5)
      await main_channel.send(f'Ты кто такой, {member.name}? Тебе здесь не рады')
      await member.create_dm()
      await member.dm_channel.send('ты об этом пожалеешь', delete_after=60)

#ЧЛЕН ливает
@client.event
async def on_member_remove(member):
    print(f'я заметила, что {member.name} покинул нас')
    main_channel = client.get_channel(428262608664264726)
    async with main_channel.typing():
      sleep(5)
      await main_channel.send(f'Бог покинул это место. А теперь еще и {member.name}')
      await member.create_dm()
      await member.dm_channel.send('ну и катись', delete_after=60)
    
#прослушка сообщений
@client.event
async def on_message(message):
    # игнор собственных сообщений
    if message.author == client.user:
        return   

    # пиво
    if pivo_trigger(message):
      async with message.channel.typing():
        answer = await about_pivko_GPT()
        await message.channel.send(answer)

    # зож-пост
    elif message.content.startswith('!зож-пост'):
      author_name = get_author_name(message.author)
      if (author_name == 'Demmenty' or author_name == 'Парабола'):
        async with message.channel.typing():
          answer = await fitness_post_GPT()
          await message.channel.send(answer)
      await message.delete()

    # обращения к боту
    elif client.user.mentioned_in(message):
      async with message.channel.typing():
        author_name = get_author_name(message.author)
        author_sex = get_author_sex(author_name)
        msg = message.content.replace('<@955543907213660240>', '')
        # paint + opinion
        if '!нарисуй' in message.content:
          msg = msg.replace('!нарисуй', '')
          pic_url = await create_pic_DALLE(msg)
          answer = await opinion_chat_GPT(msg, author_name, author_sex)
          await message.channel.send(content=pic_url)
          await message.channel.send(answer)
        # opinion
        else:
          answer = await ask_chat_GPT(msg, author_name, author_sex)
          await message.channel.send(message.author.mention + answer)

    # paint picture
    elif message.content.startswith('!нарисуй'):
      async with message.channel.typing():
        prompt = message.content.replace('!нарисуй', '')
        pic_url = await create_pic_DALLE(prompt)
        await message.channel.send(content=pic_url)

    #ответы на глупый_бот    
    elif any(word in message.content for word in abuse_triggers):
      async with message.channel.typing():
        sleep(4)
        await message.channel.send(random.choice(abuse_answers))

    #вызов помощи
    elif message.content.startswith('!help'):
      async with message.channel.typing():
        sleep(3)
        await message.channel.send(f'{message.author.mention}, никто тебе не поможет')
        
    #упоминание имени тени
    elif any(word in message.content for word in shadow_triggers):
      sleep(1)
      await message.channel.send(' :middle_finger: ')

    # случайные мрачные фразы
    elif grim_trigger(message):
      async with message.channel.typing():
        sleep(3)
        answer = await grim_phrase_GPT()
        await message.channel.send(answer)


client.run(DISCORD_TOKEN)
