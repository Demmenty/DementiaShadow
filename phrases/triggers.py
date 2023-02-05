def pivo_trigger(message):

    if (message.content.startswith('!piv') or
        message.content.startswith('!пив') or
        message.content.startswith('!pennoe') or
        'пиво' in message.content or
        'пивко' in message.content):

        return True


def anime_trigger(message):

    if (message.content.startswith('!anime') or
        message.content.startswith('!аниме') or
        'аниме' in message.content):

        return True


def grim_trigger(message):

    trigger_words = ['реал', 'ебат', 'груст', 'пиздец', 'пздц', 'хрен']

    if any(word in message.content for word in trigger_words):
        
        return True


shadow_triggers = ['@Тень Деменции', 'Тень', 'Тень Деменции',
                'Тень демменции', 'тень демменции', 'тень Деменции',
                'тень деменции','Тень деменции']
abuse_triggers = ['глупый бот', 'Глупый бот', 'плохой бот',
               'Плохой бот', 'тупой бот', 'Тупой бот',
               'глупые боты', 'Глупые боты', 'тупые боты', 'Тупые боты']
