from aiogram.utils import executor
from create_bot import dp
from Utils.txt_to_json import convert_txt_to_json
from date_base import sql_lite

async def on_my_startup(_):
    convert_txt_to_json()
    print('Бот онлайн')
    sql_lite.sql_start()


from Handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)


other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_my_startup)
