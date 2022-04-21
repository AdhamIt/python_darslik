const Telegram = require("node-telegram-bot-api")

const token = "5266879331:AAHI5C_qtQfSDA0xElAY5-ztKF5R0R10cLQ"

const bot = new Telegram(token, {polling: true})

filename = "BQACAgIAAxkBAAMbYmEy32-ktoPS7LeBbjJB4V25eaQAAkoWAALaTwlL4tqagu3ZctAkBA"

qushiqlar = ["ummon", "benom", "shoxrux", "sia"]

// bot.on("message", function(msg){
//     console.log(msg);
//     bot.sendMessage(msg.from.id, `Sizning ismingiz ${msg.chat.first_name} sizning yozgan matningiz ${msg.text}`)
//     bot.on("document", function(msg){
//         console.log(msg);
//         bot.sendMessage(msg.from.id, "Sizning filingiz saqlandi.")
//     })
//     bot.sendDocument(msg.from.id, filename)
// })
bot.onText(/\music/, msg =>{
    chatId= msg.from.id;
    setInterval(()=>{
        bot.sendMessage(chatId, "Honandani kiriting")
    },1500)
    bot.sendMessage(chatId, "Ashulachi nomini kiriting: ")
    bot.on("message", msg =>{
        text = msg.text
        if (qushiqlar.filter(ms => ms == text) !=0){
            bot.sendMessage(chatId, text)
        }
        else{
            bot.sendMessage(chatId, "Bunday musiqa mavjud emas")
        }
    })

})