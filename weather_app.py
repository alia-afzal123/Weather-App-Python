# weather_app.py
import tkinter as tk
from tkinter import ttk, messagebox
from api import get_weather
from utils import get_weather_icon

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Weather App")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        
        # Unit selection (Celsius/Fahrenheit)
        self.unit_var = tk.StringVar(value="celsius")
        
        # UI banate hain
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title = tk.Label(
            self.root, 
            text="🌍 Live Weather App", 
            font=("Arial", 24, "bold"),
            fg="#2c3e50"
        )
        title.pack(pady=20)
        
        # City input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="City Name:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        
        self.city_entry = tk.Entry(input_frame, font=("Arial", 14), width=20)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        
        # Unit selection
        unit_frame = tk.Frame(self.root)
        unit_frame.pack(pady=5)
        
        tk.Radiobutton(
            unit_frame, text="Celsius (°C)", 
            variable=self.unit_var, value="celsius"
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(
            unit_frame, text="Fahrenheit (°F)", 
            variable=self.unit_var, value="fahrenheit"
        ).pack(side=tk.LEFT, padx=10)
        
        # Search button
        self.search_btn = tk.Button(
            self.root, 
            text="🔍 Get Weather", 
            font=("Arial", 14, "bold"),
            bg="#3498db", 
            fg="white",
            command=self.search_weather
        )
        self.search_btn.pack(pady=10)
        
        # Weather display frame
        self.display_frame = tk.Frame(self.root, relief=tk.RIDGE, bd=2)
        self.display_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        # Initial message
        self.show_initial_message()
        
        # Enter press se bhi search ho
        self.city_entry.bind("<Return>", lambda event: self.search_weather())
    
    def show_initial_message(self):
        self.clear_display()
        msg = tk.Label(
            self.display_frame,
            text="Enter a city name\nand click 'Get Weather' 🌍",
            font=("Arial", 14),
            fg="gray"
        )
        msg.pack(expand=True, pady=50)
    
    def clear_display(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()
    
    def search_weather(self):
        city = self.city_entry.get().strip()
        unit = self.unit_var.get()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name!")
            return
        
        # Disable button while loading
        self.search_btn.config(state=tk.DISABLED, text="⏳ Loading...")
        self.root.update()
        
        # API call
        weather_data = get_weather(city, unit)
        
        # Enable button again
        self.search_btn.config(state=tk.NORMAL, text="🔍 Get Weather")
        
        if weather_data["success"]:
            self.show_weather(weather_data)
        else:
            self.show_error(weather_data["error"])
    
    def show_weather(self, data):
        self.clear_display()
        
        # Weather icon emoji
        icon = get_weather_icon(data["weather_main"])
        
        # City name
        city_label = tk.Label(
            self.display_frame,
            text=f"{icon} {data['city']} {icon}",
            font=("Arial", 22, "bold"),
            fg="#2c3e50"
        )
        city_label.pack(pady=10)
        
        # Temperature (big font)
        temp_label = tk.Label(
            self.display_frame,
            text=f"{data['temperature']}{data['unit']}",
            font=("Arial", 48, "bold"),
            fg="#e67e22"
        )
        temp_label.pack(pady=5)
        
        # Weather description
        desc_label = tk.Label(
            self.display_frame,
            text=data["weather_desc"].title(),
            font=("Arial", 14),
            fg="#7f8c8d"
        )
        desc_label.pack()
        
        # Feels like
        feels_label = tk.Label(
            self.display_frame,
            text=f"Feels like: {data['feels_like']}{data['unit']}",
            font=("Arial", 11)
        )
        feels_label.pack(pady=5)
        
        # Separator
        tk.Frame(self.display_frame, height=2, bg="#bdc3c7").pack(fill=tk.X, pady=10, padx=20)
        
        # Details frame
        details_frame = tk.Frame(self.display_frame)
        details_frame.pack(pady=10)
        
        # Humidity
        humidity_label = tk.Label(
            details_frame,
            text=f"💧 Humidity: {data['humidity']}%",
            font=("Arial", 12)
        )
        humidity_label.grid(row=0, column=0, padx=20, pady=5)
        
        # Wind speed
        wind_label = tk.Label(
            details_frame,
            text=f"💨 Wind: {data['wind_speed']} m/s",
            font=("Arial", 12)
        )
        wind_label.grid(row=0, column=1, padx=20, pady=5)
    
    def show_error(self, error_msg):
        self.clear_display()
        error_label = tk.Label(
            self.display_frame,
            text=f"❌ {error_msg}",
            font=("Arial", 14),
            fg="red"
        )
        error_label.pack(expand=True, pady=50)

# ========== RUN THE APP ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop() 