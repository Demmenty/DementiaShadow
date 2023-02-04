{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "096ead3f",
   "metadata": {},
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "Cannot close a running event loop",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\discord\\client.py:713\u001b[0m, in \u001b[0;36mClient.run\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    712\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 713\u001b[0m     \u001b[43mloop\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun_forever\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    714\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\asyncio\\base_events.py:585\u001b[0m, in \u001b[0;36mBaseEventLoop.run_forever\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    584\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_closed()\n\u001b[1;32m--> 585\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_check_running\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    586\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_set_coroutine_origin_tracking(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_debug)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\asyncio\\base_events.py:577\u001b[0m, in \u001b[0;36mBaseEventLoop._check_running\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    576\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_running():\n\u001b[1;32m--> 577\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mThis event loop is already running\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m    578\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[1;31mRuntimeError\u001b[0m: This event loop is already running",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\discord\\client.py:90\u001b[0m, in \u001b[0;36m_cleanup_loop\u001b[1;34m(loop)\u001b[0m\n\u001b[0;32m     89\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m---> 90\u001b[0m     \u001b[43m_cancel_tasks\u001b[49m\u001b[43m(\u001b[49m\u001b[43mloop\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     91\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m sys\u001b[38;5;241m.\u001b[39mversion_info \u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m (\u001b[38;5;241m3\u001b[39m, \u001b[38;5;241m6\u001b[39m):\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\discord\\client.py:75\u001b[0m, in \u001b[0;36m_cancel_tasks\u001b[1;34m(loop)\u001b[0m\n\u001b[0;32m     73\u001b[0m     task\u001b[38;5;241m.\u001b[39mcancel()\n\u001b[1;32m---> 75\u001b[0m \u001b[43mloop\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun_until_complete\u001b[49m\u001b[43m(\u001b[49m\u001b[43masyncio\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgather\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mtasks\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mreturn_exceptions\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mTrue\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     76\u001b[0m log\u001b[38;5;241m.\u001b[39minfo(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAll tasks finished cancelling.\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\asyncio\\base_events.py:617\u001b[0m, in \u001b[0;36mBaseEventLoop.run_until_complete\u001b[1;34m(self, future)\u001b[0m\n\u001b[0;32m    616\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_closed()\n\u001b[1;32m--> 617\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_check_running\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    619\u001b[0m new_task \u001b[38;5;241m=\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m futures\u001b[38;5;241m.\u001b[39misfuture(future)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\asyncio\\base_events.py:577\u001b[0m, in \u001b[0;36mBaseEventLoop._check_running\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    576\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_running():\n\u001b[1;32m--> 577\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mThis event loop is already running\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m    578\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[1;31mRuntimeError\u001b[0m: This event loop is already running",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Input \u001b[1;32mIn [12]\u001b[0m, in \u001b[0;36m<cell line: 19>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     15\u001b[0m     author \u001b[38;5;241m=\u001b[39m ctx\u001b[38;5;241m.\u001b[39mmessage\u001b[38;5;241m.\u001b[39mauthor \u001b[38;5;66;03m# Объявляем переменную author и записываем туда информацию об авторе.\u001b[39;00m\n\u001b[0;32m     17\u001b[0m     \u001b[38;5;28;01mawait\u001b[39;00m ctx\u001b[38;5;241m.\u001b[39msend(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mHello, \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mauthor\u001b[38;5;241m.\u001b[39mmention\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m!\u001b[39m\u001b[38;5;124m'\u001b[39m) \u001b[38;5;66;03m# Выводим сообщение с упоминанием автора, обращаясь к переменной author.\u001b[39;00m\n\u001b[1;32m---> 19\u001b[0m \u001b[43mbot\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43msettings\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mtoken\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\discord\\client.py:719\u001b[0m, in \u001b[0;36mClient.run\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m    717\u001b[0m     future\u001b[38;5;241m.\u001b[39mremove_done_callback(stop_loop_on_completion)\n\u001b[0;32m    718\u001b[0m     log\u001b[38;5;241m.\u001b[39minfo(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mCleaning up tasks.\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m--> 719\u001b[0m     \u001b[43m_cleanup_loop\u001b[49m\u001b[43m(\u001b[49m\u001b[43mloop\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    721\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m future\u001b[38;5;241m.\u001b[39mcancelled():\n\u001b[0;32m    722\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\discord\\client.py:95\u001b[0m, in \u001b[0;36m_cleanup_loop\u001b[1;34m(loop)\u001b[0m\n\u001b[0;32m     93\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m     94\u001b[0m     log\u001b[38;5;241m.\u001b[39minfo(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClosing the event loop.\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m---> 95\u001b[0m     \u001b[43mloop\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mclose\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python310\\lib\\asyncio\\selector_events.py:89\u001b[0m, in \u001b[0;36mBaseSelectorEventLoop.close\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     87\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mclose\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[0;32m     88\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_running():\n\u001b[1;32m---> 89\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCannot close a running event loop\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     90\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_closed():\n\u001b[0;32m     91\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m\n",
      "\u001b[1;31mRuntimeError\u001b[0m: Cannot close a running event loop"
     ]
    }
   ],
   "source": [
    "import discord\n",
    "from discord.ext import commands\n",
    "\n",
    "settings = {\n",
    "    'token': 'OTU1NTQzOTA3MjEzNjYwMjQw.YjjNnA.D_BiJ-tNEvCxXXRixTJq2wjvFz8',\n",
    "    'bot': 'Тень Деменции',\n",
    "    'id': 955531621321281548,\n",
    "    'prefix': '!'\n",
    "}\n",
    "\n",
    "bot = commands.Bot(command_prefix = settings['prefix'])\n",
    "\n",
    "@bot.command() \n",
    "async def hello(ctx): # Создаём функцию и передаём аргумент ctx.\n",
    "    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.\n",
    "\n",
    "    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.\n",
    "    \n",
    "bot.run(settings['token'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d9cbb28",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
