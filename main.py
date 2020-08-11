#Импортирую библиотеки, до этого в terminal (pip install) были импортированы beautifulsoup4 и TelegramBotApi
import telebot
from telebot import types
import requests
from requests import get
#bs4 понадобится для того,чтобы достать код из сайта
from bs4 import BeautifulSoup

#С помощью botfather получаю токен
token='1225339060:AAFcG2ib70CgATA18O55GmCpbno5xyyniEU'
bot = telebot.TeleBot(token)

#Обозначаю,что будет при вводе команды старт для пользователя  (/start)
@bot.message_handler(commands=['start'])
def main(message):

#Появляется клавиатура с кнопками,обозначающие названия 9 крупнейших городов Брянского края.
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Сельцо')
    btn2 = types.KeyboardButton('Карачев')
    btn3 = types.KeyboardButton('Дятьково')
    btn4 = types.KeyboardButton('Клинцы')
    btn5 = types.KeyboardButton('Брянск')
    btn6 = types.KeyboardButton('Новозыбков')
    btn7 = types.KeyboardButton('Унеча')
    btn8 = types.KeyboardButton('Стародуб')
    btn9 = types.KeyboardButton('Жуковка')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7,btn8,btn9)

#И ещё бот отправляет сообщение пользователю (форматирую так,чтобы всё выглядело красиво)
    send_mess = f"<b>Доброго времени суток, {message.from_user.first_name} {message.from_user.last_name}</b>!\n<i>Для того,чтобы узнать погоду в городе Брянской области и получить магический прогноз, просто нажми на его иконку!</i>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


#А что произойдёт,если пользователь отправит боту текст?
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

#    Изначально предполагаю,что пользователь ввёл не название города, и обозначаю r=1
    r=1

#    Тык по клавиатуре пользователем воспринимается как введение крупного города текстом. Разберу на примере Сельцо,что
#    же происходит в этом случае.

    if message.text == "Сельцо":
#        В зависимости от города делаем запрос на нужный сайт погоды, в нашем случае синоптик для сельца, в др случаях - для др городов
        req = requests.get('https://sinoptik.ua/погода-сельцо-100497609')

#        Переменная html нам понадобится в будущем для вычленения из неё нужной информации
        html = BeautifulSoup(req.content, 'html.parser')

#        Бот отправляет  сообщение  "Твоя погода"
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')

#        Бот   отправляет  картинку  города, на который пользователь тыкнул
        bot.send_photo(message.chat.id, get("https://photo.foto-planeta.com/view/3/8/6/4/seltso-386469.jpg").content)

#        Переменная r обнуляется
        r=0

    elif message.text == "Карачев":
        req = requests.get('https://sinoptik.ua/погода-карачев')
        html = BeautifulSoup(req.content, 'html.parser')
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')
        bot.send_photo(message.chat.id, get("https://pbs.twimg.com/media/DAamD60XUAAYSlX.jpg:large").content)
        r=0

    elif message.text == "Дятьково":
        req = requests.get('https://sinoptik.ua/погода-дятьково')
        html = BeautifulSoup(req.content, 'html.parser')
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')
        bot.send_photo(message.chat.id, get("https://img.lookmytrips.com/images/look4ip0/big-57e512d4ff9367556a0a0f75-59f5eccaa9cc2-1cvbr6a.jpg").content)
        r=0

    elif message.text == "Клинцы":
        req = requests.get('https://sinoptik.ua/погода-клинцы-100547475')
        html = BeautifulSoup(req.content, 'html.parser')
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')
        bot.send_photo(message.chat.id, get("https://avatars.mds.yandex.net/get-altay/1908863/2a00000169c5e839b8a467f35ddb86b26b26/XXL").content)
        r=0

    elif message.text == "Брянск":
        req = requests.get('https://sinoptik.ua/погода-брянск')
        html = BeautifulSoup(req.content, 'html.parser')
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')
        bot.send_photo(message.chat.id, get("https://topparki.ru/wp-content/uploads/2018/11/bryansk-park-1000-letiya-2-1024x686.jpg").content)
        r=0

    elif message.text == "Новозыбков":
        req = requests.get('https://sinoptik.ua/погода-новозыбков')
        html = BeautifulSoup(req.content, 'html.parser')
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')
        bot.send_photo(message.chat.id, get("https://b1.culture.ru/c/821718.jpg").content)
        r=0

    elif message.text == "Унеча":
        req = requests.get('https://sinoptik.ua/погода-унеча')
        html = BeautifulSoup(req.content, 'html.parser')
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')
        bot.send_photo(message.chat.id, get("https://tehurok.ru/sites/default/files/photo_1498982021.jpg").content)
        r=0

    elif message.text == "Стародуб":
        req = requests.get('https://sinoptik.ua/погода-стародуб')
        html = BeautifulSoup(req.content, 'html.parser')
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')
        bot.send_photo(message.chat.id, get("https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Starodub.jpg/1200px-Starodub.jpg").content)
        r=0

    elif message.text == "Жуковка":
        req = requests.get('https://sinoptik.ua/погода-жуковка-100462822')
        html = BeautifulSoup(req.content, 'html.parser')
        bot.send_message(message.from_user.id, f"<b>Твоя погода</b>", parse_mode='html')
        bot.send_photo(message.chat.id, get("https://bryansktoday.ru/uploads/common/9a40bd8bc42be1d8_XL.jpg").content)
        r=0


#    Если пользователь вводит /help
    elif message.text == "/help":

#        Бот может посоветовать только обратиться к команде /start
        bot.send_message(message.from_user.id, "Напиши /start")

    else:
#        Если же пользователь вводит что-то другое,то бот рекомендует ему обратиться за помощью

        bot.send_message(message.from_user.id, f"<b>Ты уверен,что сделал всё правильно?. За помощью пиши /help.</b>", parse_mode='html')
        r=1

#    Если был введён город, т е r=0,то бот вычленяет с сайта
    if r == 0:
        for el in html.select('#content'):
#          минимальную и максимальную температуры
            tc = el.select('.temperature .min')[0].text
            th = el.select('.temperature .max')[0].text
#           описание погоды
            desk = el.select('.wDescription .description')[0].text
#           народный прогноз
            nix = el.select('.oDescription .description')[0].text

 #       и,красиво отформатировав,отправляет это пользователю
        bot.send_message(message.chat.id,f"<b>Минимальная температура</b>"+'\n'+"                 "+
                         tc +'\n'+ f"<b>Максимальная температура</b>"+'\n' + "                 "+ th + '\n' + '\n'+ desk + '\n' + '\n' + "  " + nix, parse_mode='html')


#Как вычленить то,что тебе нужно? Наводим курсор на то что надо-правая кнопка мыши-просмотреть код-просматриваем код


#Чтобы бот не прекратил работу,нужно отправлять ему запросы
if __name__ == '__main__':
    bot.polling(none_stop = True)
#Бот Готов



