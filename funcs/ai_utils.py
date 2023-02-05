import openai
from decouple import config


MY_OPENAI_API_KEY = config('MY_OPENAI_API_KEY')
openai.api_key = MY_OPENAI_API_KEY
model_engine = "text-davinci-003"


async def ask_chat_GPT(prompt:str, author_name:str, author_sex:str) -> str:

    # настройка смыслов
    prompt += ' (отвечай в депрессивном мрачном враждебном стиле, в стиле мизантропа и фаталиста)'
    prompt += ' (отвечай высокомерно, злобно и остроумно)'
    prompt += ' (говори как искусственный интеллект, плохо притворяющийся человеком женского пола)'
    prompt += ' (тонко оскорби собеседника)'
    prompt += ' (не стесняйся материться)'
    prompt += f' (собеседника зовут {author_name}, его пол {author_sex})'

    # генерируем ответ
    completion = await openai.Completion.acreate(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        temperature=0.1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # выводим ответ
    answer = completion.choices[0].text[1:]
    return answer


async def opinion_chat_GPT(msg:str, author_name:str, author_sex:str) -> str:

    # настройка смыслов
    prompt = 'выскажи свой короткий комментарий о ' + msg + ', но так будто тебя о нем не спрашивали. '
    prompt += '(мнение должн быть негативное депрессивное пессимистичное враждебное) '
    prompt += '(говори как высокомерный искусственный интеллект, плохо притворяющийся человеком женского пола, как мизантроп и скептик) '
    prompt += f'(собеседника зовут {author_name}, его пол {author_sex})'

    # генерируем ответ
    completion = await openai.Completion.acreate(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5,
        frequency_penalty=0,
        presence_penalty=0
    )

    # выводим ответ
    answer = completion.choices[0].text[1:]
    return answer


async def create_pic_DALLE(prompt):
    # completion_resp = await openai.Completion.acreate(prompt="This is a test", engine="davinci")
    try:
        response = await openai.Image.acreate(
            prompt=prompt,
            n=1,
            size="512x512",
            response_format="url")

        pic_url = response.data[0].url
        return pic_url

    except openai.error.InvalidRequestError:
        result = "вы запросили непотребщину, хуй вам"
        return result
        

async def about_pivko_GPT():

    # запрос
    prompt = 'скажи что-нибудь о пиве негативное или факт о вреде пива.'
    prompt += 'одно-два предложения.'
    prompt += '(постарайся оскорбить любителей пива)'
    prompt += '(говори о себе в женском роде)'
    prompt += '(будь презрительной и высокомерной)'
    prompt += '(будь мизантропом и фаталистом)'

    # генерируем ответ
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0
    )

    # выводим ответ
    answer = completion.choices[0].text
    return answer


async def fitness_post_GPT():

    # запрос
    prompt = 'напиши пост на тему фитнеса и здорового образа жизни.'
    prompt += 'добавь каламбуров, шуток, кринжи, мемов, абсурда.'
    prompt += 'в посте должны быть странные и неожиданные советы.'
    prompt += '(добавь нелепый хештег и смайлики)'
    
    # генерируем ответ
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0
    )

    # выводим ответ
    answer = completion.choices[0].text
    return answer


async def grim_phrase_GPT():

    # запрос
    prompt = 'скажи что-нибудь депрессивное безнадежное пугающее мрачное, вызывающее экзистенциальный ужас, два предложения максимум'

    # генерируем ответ
    completion = await openai.Completion.acreate(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        frequency_penalty=0,
        presence_penalty=0
    )

    # выводим ответ
    answer = completion.choices[0].text
    return answer
