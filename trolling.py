# ---------------------------------------------------------------------------------
# 鑓塵幗膂蓿f寥寢膃暠瘉甅甃槊槎f碣綮瘋聟碯颱亦尓㍍i:i:i;;:;:: : :
# 澣幗嶌塹傴嫩榛畝皋i袍耘蚌紕欒儼巓襴踟篁f罵f亦尓㍍i:i:i;;:;:: : :
# 漲蔭甃縟諛f麭窶膩I嶮薤篝爰曷樔黎㌢´　　｀ⅷ踟亦尓㍍i:i:i;;:;:: : :
# 蔕漓滿f蕓蟇踴f歙艇艀裲f睚鳫巓襴骸　　　　　贒憊亦尓㍍i:i:i;;:;:: : :
# 榊甃齊爰f懈橈燗殪幢緻I翰儂樔黎夢'”　 　 ,ｨ傾篩縒亦尓㍍i:i:i;;:;:: : :
# 箋聚蜚壊劑薯i暹盥皋袍i耘蚌紕偸′　　　 雫寬I爰曷f亦尓㍍i:i:i;;:;:: : :
# 銕颱麼寰篝螂徑悗f篝嚠篩i縒縡齢　　 　 　 Ⅷ辨f篝I鋗f亦尓㍍i:i:i;;:; : : .
# 碯聟f綴麼辨螢f璟輯駲f迯瓲i軌帶′　　　　　`守I厖孩f奎亦尓㍍i:i:i;;:;:: : : .
# 綮誣撒f曷磔瑩德f幢儂儼巓襴緲′　 　 　 　 　 `守枢i磬廛i亦尓㍍i:i:i;;:;:: : : .
# 慫寫廠徑悗緞f篝嚠篩I縒縡夢'´　　　 　 　 　 　 　 `守峽f徑悗f亦尓㍍i:i:i;;:;:: : : .
# 廛僵I數畝篥I熾龍蚌紕襴緲′　　　　　　　　　　　　　‘守畝皋弊i劍亦尓㍍i:i:i;;:;:: : : .
# 瘧i槲瑩f枢篝磬曷f瓲軌揄′　　　　　　　　　　　　　,gf毯綴徑悗嚠迩忙亦尓㍍i:i:i;;:;::
# 襴罩硼f艇艀裲睚鳫襴鑿緲'　　　　　　　　　　 　 　 奪寔f厦傀揵猯i爾迩忙亦尓㍍i:i:
# 椈棘斐犀耋絎絲絨緲′　　　　　　 　 　 　 　 　 　 　 ”'罨悳萪f蒂渹幇f廏迩忙i亦尓㍍
# 潁樗I瘧德幢i儂巓緲′　　　　　　 　 　 　 　 　 　 r㎡℡〟”'罨椁裂滅楔滄愼愰迩忙亦
# 翦i磅艘溲I搦儼巓登zzz zzz㎜㎜ｧg　 　 緲 g　 　 甯體i爺ゎ｡, ”'罨琥焜毳徭i嵬塰慍絲
# 枢篝磬f曷迯i瓲軌f襴暹 甯幗緲 ,fi'　　 緲',纜｡　　贒i綟碕碚爺ゎ｡ ”'罨皴發傲亂I黹靱
# 緞愾慊嵬嵯欒儼巓襴驫 霤I緲 ,緲　　 ＂,纜穐　　甯絛跨飩i髢馳爺ゎ｡`'等誄I筴碌I畷
# 罩硼I蒻筵硺艇艀i裲睚亀 篳'’,緲　　g亀 Ⅶil齢　　贒罩硼i艇艀裲睚鳫爺靠飭蛸I裘裔
# 椈f棘豢跫跪I衙絎絲絨i爺i㎜iⅣ 　 ,緲i亀 Ⅶ靈,　　甯傅喩I揵揚惹屡絎痙棏敞裔筴敢
# 頬i鞏褂f跫詹雋髢i曷迯瓲軌霤 　 ,緲蔭穐 Ⅶ穐 　 讎椈i棘貅f斐犀耋f絎絲觚f覃黹黍
# 襴蔽戮貲艀舅I肅肄肆槿f蝓Ⅷ 　 緲$慚I穐,疊穐　 甯萪碾f鋗輜靠f誹臧鋩f褂跫詹i雋
# ---------------------------------------------------------------------------------
# 🌐 This project was created https://t.me/I_love_wizzy
# ⚠️ Licensed under the GNU AGPLv3.
# 💢 The owner of this script does not have any responsibility or intellectual property rights in relation to this script.
# ---------------------------------------------------------------------------------
# Name: TrollSpam
# Author: https://t.me/I_love_wizzy
# scope: heroku && hikka
# ---------------------------------------------------------------------------------
__version__ = (1, 0, 0)

import json
import aiohttp
import asyncio
import re
from random import choice
from telethon.tl.types import Message, Use
from .. import loader, utils

@loader.tds
class KomarubullingMod(loader.Module):
    """Module for insults, make the interlocutor depressed."""

    strings = {
        "name": "Komarubulling",
        "error_key": "<b><i>Error: Key 'BullText' not found.</i></b>",
        "error_decoding": "<b><i>Error: The JSON could not be decoded.</i></b>",
        "error_uploading_data": "<b><i>Error loading data</i></b>",
        "error_valid_args": "<b><i>Please enter valid arguments!</i></b>",
        "error_user": "<b><i>Please specify a user to tag (reply or mention)!</i></b>",
        "launched": "<b><i>Komarubulling launched!</i></b>\n\n<b><i>Use <code>{prefix}komaruoff</code> to stop the attack.</i></b>",
        "launched_tag": "<b><i>Komarubulling with tag launched! Target: @{username}</i></b>\n\n<b><i>Use <code>{prefix}komaruoff</code> to stop the attack.</i></b>",
        "stopped": "<b><i>Komarubulling has stopped.</i></b>",
    }

    strings_ru = {
        "error_key": "<b><i>Error: ключ 'BullText' не найден.</i></b>",
        "error_decoding": "<b><i>Error: не удалось декодировать JSON.</i></b>",
        "error_uploading_data": "<b><i>Ошибка при загрузке данных</i></b>",
        "error_valid_args": "<b><i>Введите корректные аргументы!</i></b>",
        "error_user": "<b><i>Укажите пользователя для тега (ответом или упоминанием)!</i></b>",
        "launched": "<b><i>Komarubulling запущен!</i></b>\n\n<b><i>Используйте <code>{prefix}komaruoff</code>, чтобы остановить атаку.</i></b>",
        "launched_tag": "<b><i>Komarubulling с тегом запущен! Цель: @{username}</i></b>\n\n<b><i>Используйте <code>{prefix}komaruoff</code>, чтобы остановить атаку.</i></b>",
        "stopped": "<b><i>Komarubulling остановлен.</i></b>",
    }

    strings_uz = {
        "error_key": "<b><i>Error: 'BullText' калити топилмади.</i></b>",
        "error_decoding": "<b><i>Error: JSON декодлаш муваффақиятли амалга ошмади.</i></b>",
        "error_uploading_data": "<b><i>Маълумотлар юклаб олинмади</i></b>",
        "error_valid_args": "<b><i>Iltimos, to'g'ri dalillarni kiriting!</i></b>",
        "error_user": "<b><i>Iltimos, teglash uchun foydalanuvchini ko'rsating (javob yoki eslatma)!</i></b>",
        "launched": "<b><i>Komarubulling ishga tushirildi!</i></b>\n\n<b><i>Hujumni toʻxtatish uchun <code>{prefix}komaruoff</code> dan foydalaning.</i></b>",
        "launched_tag": "<b><i>Teg bilan Komarubulling ishga tushirildi! Maqsad: @{username}</i></b>\n\n<b><i>Hujumni toʻxtatish uchun <code>{prefix}komaruoff</code> dan foydalaning.</i></b>",
        "stopped": "<b><i>Komarubulling to'xtadi.</i></b>",
    }

    strings_de = {
        "error_key": "<b><i>Error: Der Schlüssel 'BullText' wurde nicht gefunden.</i></b>",
        "error_decoding": "<b><i>Error: JSON konnte nicht decodiert werden.</i></b>",
        "error_uploading_data": "<b><i>Fehler beim Hochladen der Daten</i></b>",
        "error_valid_args": "<b><i>Bitte geben Sie gültige Argumente ein!</i></b>",
        "error_user": "<b><i>Bitte geben Sie einen zu markierenden Benutzer an (Antwort oder Erwähnung)!</i></b>",
        "launched": "<b><i>Komarubulling gestartet!</i></b>\n\n<b><i>Verwenden Sie <code>{prefix}komaruoff</code>, um den Angriff zu stoppen.</i></b>",
        "launched_tag": "<b><i>Komarubulling mit Tag gestartet! Ziel: @{username}</i></b>\n\n<b><i>Verwenden Sie <code>{prefix}komaruoff</code>, um den Angriff zu stoppen.</i></b>",
        "stopped": "<b><i>Komarubulling hat angehalten.</i></b>",
    }

    strings_es = {
        "error_key": "<b><i>Error: No se encontró la clave 'BullText'.</i></b>",
        "error_decoding": "<b><i>Error: No se pudo decodificar JSON.</i></b>",
        "error_uploading_data": "<b><i>Error al cargar los datos</i></b>",
        "error_valid_args": "<b><i>¡Por favor ingrese argumentos válidos!</i></b>",
        "error_user": "<b><i>¡Especifique un usuario para etiquetar (responder o mencionar)!</i></b>",
        "launched": "<b><i>¡Komarubulling lanzado!</i></b>\n\n<b><i>Utiliza <code>{prefix}komaruoff</code> para detener el ataque.</i></b>",
        "launched_tag": "<b><i>¡Komarubulling con etiqueta lanzado! Objetivo: @{username}</i></b>\n\n<b><i>Utiliza <code>{prefix}komaruoff</code> para detener el ataque.</i></b>",
        "stopped": "<b><i>Komarubulling se ha detenido.</i></b>",
    }

    async def get_insults_data(self):
        url = "https://raw.githubusercontent.com/komarulolll/herokutrolling/main/insults.json"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        text = await response.text()
                        data = json.loads(text)
                        return data
                    else:
                        return None
        except Exception as e:
            print(f"Error loading insults: {e}")
            return None

    async def get_user_username(self, message, args):
        username = None
        
        if args:
            for arg in args:
                if arg.startswith('@'):
                    username = arg.lstrip('@')
                    break
        
        if not username:
            reply = await message.get_reply_message()
            if reply and reply.sender_id:
                try:
                    user = await message.client.get_entity(reply.sender_id)
                    if hasattr(user, 'username') and user.username:
                        username = user.username
                except:
                    pass
        
        if not username:
            try:
                if message.entities:
                    for entity in message.entities:
                        if hasattr(entity, 'user_id'):
                            user = await message.client.get_entity(entity.user_id)
                            if hasattr(user, 'username') and user.username:
                                username = user.username
                            break
            except:
                pass
        
        return username

    async def komarubullcmd(self, message):
        data = await self.get_insults_data()
        
        if data is None:
            await utils.answer(message, self.strings("error_uploading_data"))
            return
            
        if "BullText" in data and isinstance(data["BullText"], list) and data["BullText"]:
            text = choice(data["BullText"])
            await utils.answer(message, text)
        else:
            await utils.answer(message, self.strings("error_key"))

    async def komaruspamcmd(self, message):
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, self.strings("error_valid_args"))
            return

        parts = args.split(' ', 1)
        try:
            time = float(parts[0])
            text = parts[1] + " " if len(parts) > 1 else ""
        except ValueError:
            await utils.answer(message, self.strings("error_valid_args"))
            return

        data = await self.get_insults_data()
        if data is None:
            await utils.answer(message, self.strings("error_uploading_data"))
            return
            
        if not ("BullText" in data and isinstance(data["BullText"], list) and data["BullText"]):
            await utils.answer(message, self.strings("error_key"))
            return

        self.db.set(self.strings["name"], "state", True)
        await utils.answer(message, self.strings("launched").format(prefix=self.get_prefix()))
        
        while self.db.get(self.strings["name"], "state"):
            bull_text = choice(data["BullText"])
            await message.respond(text + bull_text)
            await asyncio.sleep(time)

    async def komarutagcmd(self, message):
        """[time] [@username] [text] - Spam insults with @mention at start"""
        args = utils.get_args_raw(message)

        if not args:
            await utils.answer(message, self.strings("error_valid_args"))
            return

        parts = args.split(' ', 2)
        
        try:
            time = float(parts[0])
        except ValueError:
            await utils.answer(message, self.strings("error_valid_args"))
            return

        username = None
        text = ""
        
        if len(parts) > 1:
            if parts[1].startswith('@'):
                username = parts[1].lstrip('@')
                if len(parts) > 2:
                    text = parts[2] + " "
            else:
                text = ' '.join(parts[1:]) + " "

        if not username:
            username = await self.get_user_username(message, parts[1:] if len(parts) > 1 else [])
        
        if not username:
            await utils.answer(message, self.strings("error_user"))
            return

        data = await self.get_insults_data()
        if data is None:
            await utils.answer(message, self.strings("error_uploading_data"))
            return
            
        if not ("BullText" in data and isinstance(data["BullText"], list) and data["BullText"]):
            await utils.answer(message, self.strings("error_key"))
            return

        self.db.set(self.strings["name"], "state", True)
        await utils.answer(
            message, 
            self.strings("launched_tag").format(
                prefix=self.get_prefix(),
                username=username
            )
        )
        
        while self.db.get(self.strings["name"], "state"):
            bull_text = choice(data["BullText"])
            message_text = f"@{username} {text}{bull_text}"
            await message.respond(message_text)
            await asyncio.sleep(time)

    async def komaruoffcmd(self, message):
        """Stop the insults"""
        self.db.set(self.strings["name"], "state", False)
        await utils.answer(message, self.strings("stopped"))
        return
