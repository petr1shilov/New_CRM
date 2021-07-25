import telebot
import sqlite3 

connection = sqlite3.connect('db11.sqlite3')
curcor = connection.cursor()

curcor.execute('''SELECT * FROM user_reqest_user_request''')

list_of_req = curcor.fetchall()

# name =  list_of_req[0][1]
# print(name, sep='\n')

ToKeN = '1416526607:AAEHPU0MF-_Rewh678V30_zeGnhqeF6Sb-Q'
bot = telebot.TeleBot(ToKeN)

keyboard1 = types.ReplyKeyboardMarkup(True,True)
keyboard1.row('открыта', 'в работе', 'закрыта')

@bot.message_handler(commands=['status'])
def send_workers(message):
    bot.send_message(message.chat.id, 'Статусы :', reply_markup=keyboard1)
    

@bot.message_handler(commands=['start'])
def start_message(message):
    
    hi = 'CAACAgEAAxkBAAEBr1df2P6VlaAP4_9matpcidcbL0tyjAACDwEAAjgOghG1zE1_4hSRgh4E'
    bot.send_sticker(message.chat.id, hi)
    bot.send_message(message.chat.id, "Здравытсуйте ,{0.first_name} {0.last_name}!\n Я - Telebot. Нажмите /status , чтобы узнать статус заявки".format(message.from_user, bot.get_me()),
    parse_mode='html')






@bot.message_handler(content_types=['text'])
def get_message(message):
    
    if message.chat.type == 'private':
        if 'открыта' in message.text.lower():
            
            
            for i in list_of_req:
                bot.send_message(message.chat.id, list_of_req)  
                
            
            
        if 'закрыта' in message.text.lower():
            # markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            # kb1 = telebot.types.InlineKeyboardButton('Нет нарушение', callback_data='good')
            # kb2 = telebot.types.InlineKeyboardButton('Есть нарушения', callback_data='bad')
            
            # markup.add(kb1, kb2)

            # bot.send_message(message.chat.id, 'Есть ли нарушение ?', reply_markup=markup)    
            
            # bot.send_chat_action(message.chat.id, 'upload_photo')
            pass
            
            
        if 'в работе' in message.text.lower():
            # markup = telebot.types.InlineKeyboardMarkup(row_width=2)
            # kb1 = telebot.types.InlineKeyboardButton('Нет нарушение', callback_data='good')
            # kb2 = telebot.types.InlineKeyboardButton('Есть нарушения', callback_data='bad')
            
            # markup.add(kb1, kb2)

            # bot.send_message(message.chat.id, 'Есть ли нарушение ?', reply_markup=markup)    
            
            # bot.send_chat_action(message.chat.id, 'upload_photo')
            pass
           


bot.polling(none_stop=True)






# import logging
# import asyncio
# from datetime import datetime
# from test_bd import Bd_actions




# # инициализируем бота
# bot = Bot(token=ToKeN)


# # инициализируем соединение с БД
# db = Bd_actions('db11.sqlite3')



# # Команда активации подписки
# @dp.message_handler(commands=['subscribe'])
# async def subscribe(message: types.Message):
# 	if(not db.subscriber_exists(message.from_user.id)):
		
# 		db.add_subscriber(message.from_user.id)
# 	else:
		
# 		db.update_subscription(message.from_user.id, True)
	
# 	await message.answer("Вы успешно подписались на рассылку!")


# @dp.message_handler(commands=['unsubscribe'])
# async def unsubscribe(message: types.Message):
# 	if(not db.subscriber_exists(message.from_user.id)):
		
# 		db.add_subscriber(message.from_user.id, False)
# 		await message.answer("Вы итак не подписаны.")
# 	else:
		
# 		db.update_subscription(message.from_user.id, False)
# 		await message.answer("Вы успешно отписаны от рассылки.")

# ожидание обновления бд


