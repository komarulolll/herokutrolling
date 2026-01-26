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
# Name: Komarubulling
# Author: https://t.me/I_love_wizzy
# scope: heroku && hikka
# ---------------------------------------------------------------------------------
__version__ = (2, 2, 0)

import json
import aiohttp
import asyncio
from random import choice
from .. import loader, utils

@loader.tds
class KomarubullingMod(loader.Module):
    """Spam insults with @mentions"""
    
    strings = {
        "name": "Komarubulling",
        "loading": "🔄 Loading insults...",
        "error": "❌ Error loading insults",
        "no_args": "⚠️ Usage: .komarutag [time] [@username] [text]",
        "no_user": "⚠️ Specify user with @ or reply",
        "started": "✅ Komarubulling started! Target: @{}\n\nStop with: .komaruoff",
        "stopped": "🛑 Komarubulling stopped",
        "spam_started": "✅ Spam started!\n\nStop with: .komaruoff",
        "insult_sent": "💢 Insult sent",
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db
        self.insults = []
        self.running = False

    async def load_insults(self):
        """Load insults from GitHub"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://raw.githubusercontent.com/komarulolll/herokutrolling/main/insults.json", timeout=5) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        self.insults = data.get("BullText", [])
                        return True
        except:
            pass
        return False

    async def get_username(self, message, args):
        """Get username from message"""
        username = None
        
        if args:
            for arg in args.split():
                if arg.startswith('@'):
                    username = arg[1:]
                    break
        
        if not username:
            reply = await message.get_reply_message()
            if reply:
                user = await self.client.get_entity(reply.sender_id)
                username = getattr(user, 'username', None)
        
        if not username and message.entities:
            for entity in message.entities:
                if hasattr(entity, 'user_id'):
                    try:
                        user = await self.client.get_entity(entity.user_id)
                        username = getattr(user, 'username', None)
                        if username:
                            break
                    except:
                        continue
        
        return username

    @loader.command(
        ru_doc="[time] [@username] [text] - Спам с упоминанием",
        uz_doc="[time] [@username] [text] - Teg bilan spam",
        de_doc="[time] [@username] [text] - Spam mit Erwähnung",
        es_doc="[time] [@username] [text] - Spam con mención",
    )
    async def komarutagcmd(self, message):
        """[time] [@username] [text] - Spam with @mention"""
        args = utils.get_args_raw(message)
        
        if not args:
            await utils.answer(message, self.strings("no_args"))
            return
        
        parts = args.split(' ', 2)
        try:
            time_val = float(parts[0])
        except:
            await utils.answer(message, self.strings("no_args"))
            return
        
        username = None
        custom_text = ""
        
        if len(parts) > 1:
            if parts[1].startswith('@'):
                username = parts[1][1:]
                if len(parts) > 2:
                    custom_text = parts[2] + " "
            else:
                username = await self.get_username(message, args)
                if username:
                    custom_text = ' '.join(parts[1:]) + " "
                else:
                    await utils.answer(message, self.strings("no_user"))
                    return
        
        if not username:
            username = await self.get_username(message, args)
            if not username:
                await utils.answer(message, self.strings("no_user"))
                return

        await utils.answer(message, self.strings("loading"))
        if not self.insults:
            if not await self.load_insults():
                await utils.answer(message, self.strings("error"))
                return
                
        self.running = True
        await utils.answer(message, self.strings("started").format(username))
        
        while self.running and self.insults:
            insult = choice(self.insults)
            msg_text = f"@{username} {custom_text}{insult}"
            await self.client.send_message(message.chat_id, msg_text)
            await asyncio.sleep(time_val)

    @loader.command(
        ru_doc="[time] [text] - Спам без упоминания",
        uz_doc="[time] [text] - Tegsiz spam",
        de_doc="[time] [text] - Spam ohne Erwähnung",
        es_doc="[time] [text] - Spam sin mención",
    )
    async def komaruspamcmd(self, message):
        """[time] [text] - Spam without mention"""
        args = utils.get_args_raw(message)
        
        if not args:
            await utils.answer(message, self.strings("no_args"))
            return
        
        parts = args.split(' ', 1)
        try:
            time_val = float(parts[0])
            custom_text = parts[1] + " " if len(parts) > 1 else ""
        except:
            await utils.answer(message, self.strings("no_args"))
            return

        await utils.answer(message, self.strings("loading"))
        if not self.insults:
            if not await self.load_insults():
                await utils.answer(message, self.strings("error"))
                return

        self.running = True
        await utils.answer(message, self.strings("spam_started"))
        
        while self.running and self.insults:
            insult = choice(self.insults)
            msg_text = f"{custom_text}{insult}"
            await self.client.send_message(message.chat_id, msg_text)
            await asyncio.sleep(time_val)

    @loader.command(
        ru_doc="Отправить одно оскорбление",
        uz_doc="Bitta haqorat yuborish",
        de_doc="Eine Beleidigung senden",
        es_doc="Enviar un insulto",
    )
    async def komarubullcmd(self, message):
        """Send one insult"""
        if not self.insults:
            if not await self.load_insults():
                await utils.answer(message, self.strings("error"))
                return
        
        insult = choice(self.insults)
        await utils.answer(message, insult)

    @loader.command(
        ru_doc="Остановить спам",
        uz_doc="Spamni to'xtatish",
        de_doc="Spam stoppen",
        es_doc="Detener spam",
    )
    async def komaruoffcmd(self, message):
        """Stop spam"""
        self.running = False
        await utils.answer(message, self.strings("stopped"))
