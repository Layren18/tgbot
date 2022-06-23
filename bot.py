import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

play = ["бумагу", "ножницы", "камень"]

@bot.message_handler(commands = ['start'])
def welcome(message):
	sti = open('stickers/hi.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton ("🎲 Рандомное число")
	item2 = types.KeyboardButton ("😊 Как дела?")
	item3 = types.KeyboardButton ("😂 Анекдот")
	item4 = types.KeyboardButton ("🕹 Камень, ножницы, бумага")

	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n"
									  "Меня зовут <b>{1.first_name}</b>, я создан чтобы тебя развлекать.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup = markup)
	bot.send_message(message.chat.id, "Мои навыки:\n🎲 Рандомное число\n😊 Как дела?\n😂 Анекдот\n🕹 Камень, ножницы, бумага".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup = markup)
	bot.send_message(message.chat.id, "Выбери один из них ниже ↓".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		
		if message.text == '🎲 Рандомное число':
			sti = open('stickers/hm.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)
			bot.send_message(message.chat.id, str(random.randint(0,100)))

		elif message.text == '😊 Как дела?':

			markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
			item2 = types.InlineKeyboardButton("Плохо", callback_data='bad')
			item3 = types.InlineKeyboardButton("Не очень", callback_data='so-so')

			markup.add(item1, item2, item3)

			sti = open('stickers/like.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)
			bot.send_message(message.chat.id, 'Отлично, как у тебя?', reply_markup=markup)

		elif message.text == '😂 Анекдот':

			markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton("1", callback_data='one')
			item2 = types.InlineKeyboardButton("2", callback_data='two')
			item3 = types.InlineKeyboardButton("3", callback_data='three')

			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Выбери анекдот:', reply_markup=markup)

		elif message.text == '🕹 Камень, ножницы, бумага':

			markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton("Камень", callback_data='rock')
			item2 = types.InlineKeyboardButton("Ножницы", callback_data='scissors')
			item3 = types.InlineKeyboardButton("Бумага", callback_data='paper')

			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Давай сыграем в игру "Камень, ножницы, бумага". Выбери ход, а я сделаю свой.', reply_markup=markup)
			sti = open('stickers/play_a_game.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)

		elif message.text == "Да":
			bot.send_message(message.chat.id, "Молодец!")

		elif message.text == "да":
			bot.send_message(message.chat.id, "Молодец!")

		elif message.text == "Нет":
			bot.send_message(message.chat.id, "Ничего, победишь в следующий раз!")

		elif message.text == "нет":
			bot.send_message(message.chat.id, "Ничего, победишь в следующий раз!")

		elif message.text == "Ничья":
			bot.send_message(message.chat.id, "Хорошо, давай сыграем ещё раз!")

		elif message.text == "ничья":
			bot.send_message(message.chat.id, "Хорошо, давай сыграем ещё раз!")

		elif message.text == "/help":
			bot.send_message(message.chat.id, "Мои навыки:\n🎲 Рандомное число\n😊 Как дела?\n😂 Анекдот\n🕹 Камень, ножницы, бумага")

		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'good':
				bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
			elif call.data == 'bad':
				bot.send_message(call.message.chat.id, 'Не расстраивайся! Я уверен, что всё наладится!')
			elif call.data == 'so-so':
				bot.send_message(call.message.chat.id, 'Бывает 😢')

			elif call.data == 'one':			
				bot.send_message(call.message.chat.id, 'В пожарном депо звонит телефон. Дежурный — слушаю. Из трубки голос — Слышь пацаны, в прошлом году посадил коноплю, выросла бестолковая, ни какого кайфа не дает. '
	 			'Дежурный отвечает — Ты придурок, куда звонишь? Звони в наркологию там тебе помогут. И бросает трубку. Минут через двадцать опять звонок — А в этом году посадил, выросла хорошая, нахлобучивает так что крышу сносит!!! '
	 			'Ему ответ — тебе же сказали, звони в наркологию. И опять трубку бросают. Через полчаса снова телефон — Пацаны не бросайте трубку... Я чё звоню... У соседа дом горит... когда приедете, и будете со шлангами бегать... смотрите не потопчите!!!')
				sti = open('stickers/lol_cherry.tgs', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

			elif call.data == 'two':
				bot.send_message(call.message.chat.id, 'Известная авиакомпания нанимает на работу пилота. На это место претендуют немец, американец и русский.\n'
				'Директор компании спрашивает у немца:\n'
				'— Давно летаете?\n'
				'— Три года.\n'
				'— И сколько хотели бы получать?\n'
				'— Три тысячи. Тысячу — мне, тысячу — жене, тысячу — на страховку.\n'
				'Спрашивает у американца:\n'
				'— Давно летаете?\n'
				'— Шесть лет.\n'
				'— И сколько хотели бы получать?\n'
				'— Шесть тысяч. Две — мне, Две — жене, Две — на страховку.\n'
				'Спрашивает у русского:\n'
				'— А вы давно летаете?\n'
				'— Боже упаси, я и летать-то толком не умею, и высоты боюсь. А получать хочу девять тысяч.\n'
				'— ?!\n'
				'— Ну как-же: три — мне, три — вам…\n'
				'Директор авиакомпании совсем обалдел:\n'
				'— Стоп, а летать кто будет?\n'
				'— Как кто — немец, он же за три согласен!\n')
				sti = open('stickers/lol_fox.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

			elif call.data == 'three':
				bot.send_message(call.message.chat.id, 'Проходит соревнование «кто больше выпьет». Соревнуются русский, немец и американец.\nВедущий:\n'
				'— Первый американец! Он будет пить виски стопками. Одна… две… пять… десять… Всё! Сломался американский спортсмен!\n'
				'— Второй немец! Он будет пить пиво кружками. Одна… две… пять… десять… пятнадцать… Всё! Сломался, сломался немецкий спортсмен!\n'
				'— Теперь русский! Он пьёт водку ковшами. Один… два… пять… десять… двадцать… тридцать… Всё, сломался! Сломался ковш у русского спортсмена!')
				sti = open('stickers/lol_putin.webp', 'rb')
				bot.send_sticker(call.message.chat.id, sti)

			elif call.data == 'rock':
				bot.send_message(call.message.chat.id, "Я выбираю " + random.choice(play) + '. А ты выбрал(a) камень. Удалось победить меня? Напиши да, нет или ничья')
			elif call.data == 'scissors':
				bot.send_message(call.message.chat.id, "Я выбираю " + random.choice(play) + '. А ты выбрал(a) ножницы. Удалось победить меня? Напиши да, нет или ничья')
			elif call.data == 'paper':
				bot.send_message(call.message.chat.id, "Я выбираю " + random.choice(play) + '. А ты выбрал(a) бумагу. Удалось победить меня? Напиши да, нет или ничья')

							# remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тут что-то было!",
				reply_markup=None)
			# show alert
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
				text="Подождите, пожалуйста, мы тут ещё немножко поколдуем.")

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)