import base64

from .models import User



CODE_SEPARATOR = '#|#'


def get_referral_code(user):
    """
    Создает код для реферальной ссылки
    """
    
    email = user.email
    id = user.id
    s = email + CODE_SEPARATOR + str(id)
    s = s.encode("UTF-8")
    code = base64.b64encode(s)
    code = code.decode("UTF-8")
    return code

def get_id_in_code(code):
    """
    Извлекает идентификатор пользователя из кода
    """

    code = code.encode("UTF-8")
    s = base64.b64decode(code)
    s = s.decode("UTF-8")
    id = s.split(CODE_SEPARATOR)[-1]
    id = int(id)
    return id

def get_inviting_user(code):
    """
    Возвращяет пользователя из кода
    """

    if code is None:
        return None
    id = get_id_in_code(code)
    try:
        inviting_user = User.objects.get(id=id, is_active=True)
    except User.DoesNotExist:
        inviting_user = None
    return inviting_user
