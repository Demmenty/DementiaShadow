def koverkanie(text):
  '''Принимает список, в котором один элемент = один символ
     возвращает испорченный текст в виде строки'''
  for i in range(len(text)):
    try:
        if text[i] == 'ы':
            text[i] = 'и'
            continue
        elif text[i] == 'ж':
            text[i] = 'з'
            continue
        elif text[i] == 'з':
            text[i] = 'с'
            continue
        elif text[i] == 'р':
            text[i] = 'л'
            continue
        elif text[i] == 'в':
            text[i] = 'ф'
            continue    
        elif text[i] == 'ш':
            if text[i+1] == 'е':
                text[i] = 'с'
                text[i+1] = 'и'
            else:
                text[i] = 'с'
                continue       
        elif text[i-1] == 'к' and text[i] == 'о':
            text[i] = 'а'
            continue
        elif text[i-1] == 'н' and text[i] == 'е':
            text[i] = 'и'
            continue
        elif text[i-2] == 'т' and text[i-1] == 'ь' and text[i] == 'с':
            text.pop(i-2)
            text.pop(i-2)
            text[i-2] = 'ц'
            continue
        elif text[i-2] == 'у' and text[i-1] == 'д' and text[i] == 'ь':
            text[i-1] = 'т'
            continue
        elif text[i-3] == 'т' and text[i-2] == 'е' and text[i-1] == 'л' and text[i] == 'ь':
            text[i-3] = 'с'
            continue
        elif text[i-3] == 'у' and text[i-2] == 'д' and text[i-1] == 'е' and text[i] == 'т':
            text[i-1] = 'и'
            continue
        elif text[i-1] == 'ч' and text[i] == 'е':
            text[i-1] = 'т'
            continue
        elif text[i-1] == 'ч' and text[i] == 'н':
            text[i-1] = 'т'
            text.insert(i, 'ь')           
            continue
        elif text[i] == 'ц':
            text[i] = 'с'
            continue
        elif text[i] == text[i-1]:
            text.pop(i)
            continue
        elif text[i-1] == 'т' and text[i] == ' ':
            text.insert(i, 'ь')
            continue
        elif text[i-2] == 'т' and text[i-1] == 'с' and text[i] == 'я':
            text.pop(i-2)
            text[i-2] = 'ц'
            continue
        elif text[i-2] == 'щ' and text[i-1] == 'а' and text[i] == 'я':
            text[i-2] = 'с'
            text[i-1] = 'я'
            continue
        elif text[i-2] == 'ч' and text[i-1] == 'т' and text[i] == 'о':
            text[i-2] = 'с'
            continue
        elif text[i-2] == 'г' and text[i-1] == 'д' and text[i] == 'е':
            text.pop(i-2)
            continue
    except IndexError:
        break
  output = ''.join(text) 
  return output


def get_noun_ending(number, one, two, five):
    """Функция возвращает вариант слова с правильным окончанием
       в зависимости от числа
       Нужно передать число и соответствующие варианты
       например: get_noun_ending(4, 'слон', 'слона', 'слонов'))
    """
    n = abs(number)
    n %= 100
    if 20 >= n >= 5:
        return five
    n %= 10
    if n == 1:
        return one
    if 4 >= n >= 2:
        return two
    return five


def delete_mention(text):

    text = text.replace('<@955543907213660240>', '')

    return text
    

def get_author_name(author):

    name = str(author)[:-5]

    if name == "T3n3brate":
        name = "Тенебрейт"

    return name


def get_author_sex(author_name):

    if author_name == "Demmenty":
        author_sex = "женский"
    else:
        author_sex = "мужской"

    return author_sex
