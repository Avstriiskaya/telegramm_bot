#библиотеки, которые загружаем из вне
import telebot
import random
TOKEN = '5481154354:AAGWssrMQCcn04LOvYWvNYZLgYQnr-m_DvY'

from telebot import types
from random import choice

file = open('support.txt', 'r', encoding='utf-8')
support = file.read().split('\n')
file.close()


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('hello.gif', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("😺 Мой репозиторий")
	item2 = types.KeyboardButton("📧 Написать на почту")
	item3 = types.KeyboardButton("😊 VK")
	item4 = types.KeyboardButton("👧 Инстаграмм")
	item5 = types.KeyboardButton("🤟 Сайт визитка")
	item6 = types.KeyboardButton("☎️Написать в личку")
	item7 = types.KeyboardButton("Нужна поддержка?❤️")



	markup.add(item1, item2, item3, item4, item5, item6, item7)

	bot.send_message(message.chat.id, "Приветствую Вас в моем ботике 😇, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

# fruit = ['яблоко', 'банан', 'груша', 'персик']


#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '😺 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/Avstriiskaya')
		elif message.text == '📧 Написать на почту':
			bot.send_message(message.chat.id, 'lidia.vasu@gmail.com')
		elif message.text == '😊 VK':
			bot.send_message(message.chat.id, 'https://vk.com/l.avstriyskaya')
		elif message.text == '👧 Инстаграмм':
			bot.send_message(message.chat.id, 'https://instagram.com/lidia_avs')
		elif message.text == '🤟 Сайт визитка':
			bot.send_message(message.chat.id, 'https://avstriiskaya.github.io/')
		elif message.text == '☎️Написать в личку':
			bot.send_message(message.chat.id, 'https://t.me/Lidiya_Avstriyskaya')
		elif message.text == 'Нужна поддержка?❤️':
			bot.send_message(message.chat.id, random.choice(support))
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
