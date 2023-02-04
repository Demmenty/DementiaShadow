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

    trigger_words = ['реал', 'ебат']

    if any(word in message.content for word in trigger_words):
        
        return True
