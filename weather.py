import requests
import geocoder
from tkinter import Tk, Label, Button, messagebox

def get_location():
    try:
        location = geocoder.ip('me')
        return location.city
    except Exception as e:
        messagebox.showerror("Error", f"Unable to obtain location.\nError: {str(e)}")

def get_temperature(city):
    try:
        url = f"http://wttr.in/{city}?format=%t"
        response = requests.get(url)
        temperature = response.text.strip()
        return temperature
    except Exception as e:
        messagebox.showerror("Error", f"Unable to obtain temperature.\nError: {str(e)}")

def get_temperature_current_location():
    city = get_location()
    if city:
        temperature = get_temperature(city)
        if temperature is not None:
            messagebox.showinfo("Temperature", f"The temperature in {city} is {temperature}")
    else:
        messagebox.showerror("Error", "Unable to obtain current location.")

app = Tk()
app.title("Weather App")

label_city = Label(app, text="The current location will be determined automatically.")
label_city.pack(pady=10)

btn_get_temperature = Button(app, text="Get Current Temperature", command=get_temperature_current_location)
btn_get_temperature.pack(pady=20)

app.mainloop()
