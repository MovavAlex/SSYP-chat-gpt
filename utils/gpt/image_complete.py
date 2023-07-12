from openai_async import openai_async
from paremeters.gpt_parameters import TIME_OUT,MAX_VALUE_COUNT,IMAGE_SIZE,IMAGE_TOKEN_COUNT
from structures.errors import SomethingWentWrong, TooManyRequests

async def image_complete(prompt: str,) -> [str,int]:
    try:
        complete = openai_async.generate_img(
        timeout=TIME_OUT,
        payload={
            'prompt': prompt,
            'n': MAX_VALUE_COUNT,
            'size': IMAGE_SIZE
        }
    )
        response = complete.json()["data"][0]['url']
        return response, IMAGE_TOKEN_COUNT
    except Exception as error:
        if complete.status_code == 429:
            raise TooManyRequests(error)
        else:
            raise SomethingWentWrong(error)



