import requests
#Добавление текста на проверку
text = ""# проверяемый текст
user_key = "9d2bdc987b55f14eb4bdd9ad82f16a8e"# пользовательский ключ
exceptdomain = ""# исключаемые домены
text_uid = ""# uid добавленного текста
error_code = 0# код ошибки
error_desc = ""# описание ошибки

try:
    request = {
        'text' :"",
        'userkey': '9d2bdc987b55f14eb4bdd9ad82f16a8e',
        'method':  'get_packages_info'
    }
    response = requests.post('https://api.text.ru/account', data = request).json()
    print(response)
    # Будет выведено:
    # {u'size': 24698146}
except requests.exceptions.RequestException as ex:
    print('ERROR: %s' % ex)