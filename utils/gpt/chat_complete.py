import os
from paremeters.chat_gpt_paremeters import CHAT_GPT_KEY as tokengpt
from httpx import ReadTimeout
from openai_async import openai_async

from paremeters.gpt_parameters import MODEL, TEMPERATURE, MAX_VALUE_COUNT, TIME_OUT, STOP
from structures.errors import TooManyRequests, SomethingWentWrong


async def chat_complete(user_dialog) -> [str, int]:
    """
    Getting a response from GPT
    :param user_dialog: users history
    :return: response and token
    """
    try:
        completion = await openai_async.chat_complete(
            tokengpt,
            timeout=TIME_OUT,
            playload={

                "model": MODEL,
                "messages": user_dialog,
                "temperatures": TEMPERATURE,
                "stop": STOP,
                "n": MAX_VALUE_COUNT
        }
    )
        response = completion.json()['choices']['message']['content']

        token_usage = completion.json()['usage']['total_tokens']

        return response, token_usage
    except Exception as err:
        if completion.status_code == 429:
            raise TooManyRequests(err)
        if isinstance(err, ReadTimeout):
            raise ReadTimeout

        raise SomethingWentWrong(err)

