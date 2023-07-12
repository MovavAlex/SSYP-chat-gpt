from paremeters.response_templates import TOO_FAST_RESPONSE_MESSAGE, ERROR_RESPONSE_MESSAGE
from structures.errors import SomethingWentWrong, TooManyRequests
from utils.gpt.image_complete import image_complete


async def get_image_response(prompt: str)->[bool, str, int]:
    try:
        response, token = await image_complete(prompt)
    except TooManyRequests:
        return False, TOO_FAST_RESPONSE_MESSAGE, None
    except SomethingWentWrong:
        return False, ERROR_RESPONSE_MESSAGE, None

    return True, response, token

