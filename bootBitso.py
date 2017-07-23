import requests
import telebot
from telegram.ext import Updater
from telegram.ext import CommandHandler


url = "https://api.bitso.com/v3/available_books/"
TOKEN = "316079447:AAFqda8IcsMzHTuADwmA6OMsgGH9de_5-GU"
miBot = telebot.TeleBot(TOKEN)
miBotUpdater = Updater(miBot.token)

def getJsonBitso(url):
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        print("Si hubo respuesta")
    else:
        print("Algo Paso")
    return response.json()

def getBookForMony(urlTicker, book):
    urlTicker = urlTicker + book
    response = requests.get(urlTicker)
    if response.status_code == 200:
        print("Si hubo respuesta")
    else:
        print("Algo Paso")
    return response.json()

def start(bot=miBot, update=miBotUpdater):
    print("Iniciada conversacion: ")
    print update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="Hola Leo, soy tu bot!!!")

def ayuda(bot=miBot, update=miBotUpdater):
    print("Solicita ayuda")
    bot.sendMessage(chat_id=update.message.chat_id, text="/start: Saludo, \n /btc: informacion sobre bitcoin \n /eth: informacion sobre ethert")

def getBtc(bot=miBot, update=miBotUpdater):
    print("Solicita informacion de Bitcoin")
    urlTicker = "https://api.bitso.com/v3/ticker/?book="
    book= "btc_mxn"
    response = getBookForMony(urlTicker, book)
    datesAllMony = response["payload"]
    bitCoint = "Datos desde BITSO (%s)" % (book)
    bidTime = datesAllMony["bid"]
    #date = datesAllMony["created_at"]
    volumen = datesAllMony["volume"]
    high = datesAllMony["high"]
    low = datesAllMony["low"]
    bot.sendMessage(chat_id=update.message.chat_id, text="%s \n  Costo Actual: %s\n Volumen: %s\n high: %s\n low: %s" % (bitCoint, bidTime, volumen, high, low))

def getEth(bot=miBot, update=miBotUpdater):
    print("Solicita informacion de Bitcoin")
    urlTicker = "https://api.bitso.com/v3/ticker/?book="
    book= "eth_mxn"
    response = getBookForMony(urlTicker, book)
    datesAllMony = response["payload"]
    bitCoint = "Datos desde BITSO (%s)" % (book)
    bidTime = datesAllMony["bid"]
    #date = datesAllMony["created_at"]
    volumen = datesAllMony["volume"]
    high = datesAllMony["high"]
    low = datesAllMony["low"]
    bot.sendMessage(chat_id=update.message.chat_id, text="%s \n  Costo Actual: %s\n Volumen: %s\n high: %s\n low: %s" % (bitCoint, bidTime, volumen, high, low))


def getXrp(bot=miBot, update=miBotUpdater):
    print("Solicita informacion de Bitcoin")
    urlTicker = "https://api.bitso.com/v3/ticker/?book="
    book= "xrp_mxn"
    response = getBookForMony(urlTicker, book)
    datesAllMony = response["payload"]
    bitCoint = "Datos desde BITSO (%s)" % (book)
    bidTime = datesAllMony["bid"]
    #date = datesAllMony["created_at"]
    volumen = datesAllMony["volume"]
    high = datesAllMony["high"]
    low = datesAllMony["low"]
    bot.sendMessage(chat_id=update.message.chat_id, text="%s \n  Costo Actual: %s\n Volumen: %s\n high: %s\n low: %s" % (bitCoint, bidTime, volumen, high, low))

if __name__ == '__main__':
    start_handler = CommandHandler('start', start)
    ayuda_handler = CommandHandler('?', ayuda)
    btc_handler = CommandHandler('btc', getBtc)
    eth_handler = CommandHandler('eth', getEth)
    xrp_handler = CommandHandler('xrp', getXrp)

    dispatcher = miBotUpdater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ayuda_handler)
    dispatcher.add_handler(btc_handler)
    dispatcher.add_handler(eth_handler)
    dispatcher.add_handler(xrp_handler)
    miBotUpdater.start_polling()

#def listener(*mensajes):
#    for m in mensajes:
#        chat_id = m.chat.id
#        print m
#        if m.content_type == 'text':
#            text = m.text
#            miBot.send_message(chat_id,"Me copio de tu texto")
#            miBot.send_message(chat_id, text)
#
#
#miBot.set_update_listener(listener) #registrar la funcion listener
#miBot.polling()

while True:
     pass
#book = "btc_mxn"
#response = getJsonBitso(url)
#datesAllMony = response["payload"]
#print(datesAllMony[0]["book"])
#Para saber su minimo y superior en el mercado, no es de mi interes
#for x in datesAllMony:
#    print "La moneda: %s" % (x["book"])
#    print x

#print "*****************************************************"
#datesMony = getBookForMony(urlTicker,book)["payload"]
#print(datesMony)
