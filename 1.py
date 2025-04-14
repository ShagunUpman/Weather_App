import customtkinter as ctk
import requests
import json
import dotenv

dotenv.load_dotenv()
weather_api_key = "fa78af3aef99d4debd99e54a7f7d0f5b"

app = ctk.CTk()
app.title("Weather App")
app.geometry("300x300")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window_label = ctk.CTkLabel(app, text="Enter City Name:", font=("Comic-Sans", 20))
window_entry = ctk.CTkEntry(app)
window_result = ctk.CTkLabel(app, text="", font=("Comic-Sans", 15))

def get_weather():
    city = window_entry.get()

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        
        response = requests.get(url)
        print("this is response", response)
        data = response.json()
        print("this is data", data)

        if response.status_code == 200:
            temp = data["main"]["temp"]
            window_result.configure(text=f"Current Temp is {temp}℃")
        else:
            window_result.configure(text="City not found")

    except:
        window_result.configure(text="Connection Error")

search_btn = ctk.CTkButton(app, text="Search", command=get_weather)

window_label.pack(pady=10)
window_entry.pack(pady=10)
search_btn.pack(pady=10)
window_result.pack(pady=10)

app.mainloop()
