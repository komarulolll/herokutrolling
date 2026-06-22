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
__version__ = (1, 1, 0)

import json
import aiohttp
import asyncio
from random import choice
from .. import loader, utils
from telethon.tl.types import Message

@loader.tds
class KomarubullingMod(loader.Module):
    """Module for insults, make the interlocutor depressed."""

    strings = {
        "name": "Komarubulling",
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.is_active = False

    @loader.command(
        ru_doc="[текст] - Оскорбить собеседника с вашим текстом",
        uz_doc="[matn] - Suhbatdoshingizni sizning matningiz bilan haqorat qiling",
        de_doc="[text] - Beleidigen Sie Ihren Gesprächspartner mit Ihrem Text",
        es_doc="[texto] - Insulta a tu interlocutor con tu texto",
    )
    async def komarubull(self, message: Message):
        """[text] - Insult with your text added"""
        url = "https://raw.githubusercontent.com/komarulolll/herokutrolling/main/insults.json"
        args = utils.get_args(message)
        custom_text = ' '.join(args) + ' ' if args else ''
        
        await message.delete()
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_text = await response.text()
                    try:
                        data = json.loads(response_text)
                        if "BullText" in data and isinstance(data["BullText"], list) and data["BullText"]:
                            text = custom_text + choice(data["BullText"])
                            await self.client.send_message(
                                message.chat_id,
                                text
                            )
                    except:
                        pass

    @loader.command(
        ru_doc="[time] [text] - Спам оскорблениями с вашим текстом",
        uz_doc="[time] [text] - Sizning matningiz bilan haqorat spam",
        de_doc="[time] [text] - Spam mit Beleidigungen und Ihrem Text",
        es_doc="[time] [texto] - Spam con insultos y tu texto",
    )
    async def komaruspam(self, message: Message):
        """[time] [text] - Spam with your text added to insults"""
        url = "https://raw.githubusercontent.com/komarulolll/herokutrolling/main/insults.json"
        args = utils.get_args(message)

        if not args:
            await message.delete()
            return
        
        await message.delete()
        
        try:
            time = float(args[0])
            custom_text = ' '.join(args[1:]) + ' ' if len(args) > 1 else ''
        except:
            return
        
        self.is_active = True
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_text = await response.text()
                    try:
                        data = json.loads(response_text)
                        if "BullText" in data and isinstance(data["BullText"], list) and data["BullText"]:
                            while self.is_active:
                                text = custom_text + choice(data["BullText"])
                                await self.client.send_message(
                                    message.chat_id,
                                    text
                                )
                                await asyncio.sleep(time)
                    except:
                        pass

    @loader.command(
        ru_doc="Остановить оскорбления",
        uz_doc="Haqoratlarni to'xtating",
        de_doc="Hört auf mit den Beleidigungen",
        es_doc="basta de insultos",
    )
    async def komaruoff(self, message: Message):
        """Stop the insults"""
        self.is_active = False
        await message.delete()
