from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from game import Game
from time import sleep

updater = ApplicationBuilder().token('TOKEN').build()

async def day2NewYear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{days2NY()}')

async def hi_com(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{hi_command(update.effective_user.first_name)}')

async def message_processing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка сырого текста в чате"""
    if update.message.text[0] != '/':
        if game.gamestatus:
            # запущена игра
            # ход игрока
            try:
                matches = int(update.message.text)
            except:
                await update.message.reply_text('Я не понял ваш ответ. Напишите цифрой, сколько вы берете спичек.')
                return
            if not 0 < matches < 9:
                await update.message.reply_text('можно брать только от 1 до 8 спичек')
                return
            game.action_player(matches)
            if game.check_game_state():
                await update.message.reply_text('Поздравляю вас, вы выиграли')
                game.stop()
                return
            message = f'На столе {game.heap} спичек.'
            await update.message.reply_text(message)
            sleep(1)
            # ход компьютера
            message = f'Я взял {game.action_cpu()} спичек\n'
            await update.message.reply_text(message)
            message = f'На столе {game.heap} спичек.'
            await update.message.reply_text(message)
            sleep(1)
            if game.check_game_state():
                message = f'Я выиграл'
                await update.message.reply_text(message)
                game.stop()
                return
            message = 'Ваш ход'
            await update.message.reply_text(message)
            return

updater.add_handler(CommandHandler('hi', hi_com))
updater.add_handler(CommandHandler('NY', day2NewYear))

game = Game()
print('server start')
updater.run_polling()