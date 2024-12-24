import requests
import telebot 
TOKEN="your bo token here"
bot = telebot.TeleBot(TOKEN)
WEATHER_API_KEY="4b8752f5172cb7f5a8108b919fb15f53" 
def get_weather(city_name):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "en"
}
    res = requests.get(url, params=params)
    if res.status_code == 200:
        data = res.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return f"Weather in {city_name}:\n" \
               f"- Description: {weather}\n" \
               f"- Temperature: {temp}°C\n" \
               f"- Feels Like: {feels_like}°C\n" \
               f"- Humidity: {humidity}%\n" \
               f"- Wind Speed: {wind_speed} m/s"
    else:
        return f"error on city not on api or error in api {res.status_code}"
@bot.message_handler(commands=["start"])        
def welcomee(message):
    bot.reply_to(message, "Hello! I can provide you with the current weather information. Send me a city name.")
@bot.message_handler(func=lambda message: True)
def ggg(message):
    city_name = message.text.strip()
    weather_info = get_weather(city_name)
    bot.reply_to(message, weather_info)
print("bot is listening..........")
bot.infinity_polling()    