from pyrogram import Client, filters

@Client.on_message(filters.command ('start'))
async def cmd_start(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    
    texta = """
๐ฆ๐๐ฎ๐ฟ๐๐ถ๐ป๐ด ๐ซ ๐๐ ๐๐๐๐๐๐๐ฅ โก โ โกโก
      """
    edit = await message.reply_text(texta,message.id)
    textb = """
๐ฆ๐๐ฎ๐ฟ๐๐ถ๐ป๐ด ๐ซ ๐๐ ๐๐๐๐๐๐๐ฅ โก โ โ โก
      """
    edit = await Client.edit_message_text(message.chat.id,edit.id,textb)
    textc = """
๐ฆ๐๐ฎ๐ฟ๐๐ถ๐ป๐ด ๐ซ ๐๐ ๐๐๐๐๐๐๐ฅ โก โ โ โ 
      """
    edit = await Client.edit_message_text(message.chat.id,edit.id,textc)
    textd = f"""
๐๐ฒ๐ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> 

๐ช๐๐๐๐ข๐ ๐ ๐ง๐ข ๐ซ ๐๐ ๐๐๐๐๐๐๐ฅ โก ๐๐ข๐ง. ๐ ๐๐  ๐ ๐๐ ๐๐๐๐๐๐๐ฅ ๐๐ข๐ง ๐ช๐๐ง๐ ๐ ๐๐ก๐ฌ ๐ง๐ข๐ข๐๐ฆ ๐๐ก๐ ๐๐ข๐ ๐ ๐๐ก๐๐ฆ. ๐ ๐๐๐ก ๐๐ข ๐ ๐๐ก๐ฌ ๐ช๐ข๐ฅ๐๐ฆ.

๐ง๐ฌ๐ฃ๐ /register ๐ง๐ข ๐๐ข๐ก๐ง๐๐ก๐จ๐ ๐จ๐ฆ๐๐ก๐ ๐ ๐๐ฅฐ๐ฅฐ

"""
    edit = await Client.edit_message_text(message.chat.id,edit.id,textd)
    await plan_expirychk(user_id)
  except Exception as e:
      print(e)
