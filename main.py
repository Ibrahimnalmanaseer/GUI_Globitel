import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from service import generate_action_logic  

class VendorDeviceSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Vendor and Device Selector")

        # Load and resize the logo
        logo_path = "./images/Final-SpeechLog-logo.png"
        try:
            logo_img = Image.open(logo_path)
            logo_img = logo_img.resize((200, 180), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
            self.logo_photo = ImageTk.PhotoImage(logo_img)
        except FileNotFoundError:
            # Handle file not found error
            self.logo_photo = None

        # Vendor dropdown
        vendor_label = tk.Label(self.root, text="Select Vendor:")
        vendor_label.grid(row=1, column=0, padx=1, pady=0, sticky="w")

        vendors = ["Cisco", "Avaya", "Genesys"]
        self.vendor_var = tk.StringVar(value=vendors[0])
        vendor_menu = ttk.Combobox(self.root, textvariable=self.vendor_var, values=vendors)
        vendor_menu.grid(row=1, column=1, padx=1, pady=0, sticky="w")
        vendor_menu.bind("<<ComboboxSelected>>", self.on_vendor_selected)

        # Initialize analytics_var
        self.analytics_var = tk.IntVar(value=0)  # Default to No

        # Initialize other variables
        self.device_var = tk.StringVar()
        self.analytics_option_var = tk.StringVar(value="GPU")

        # Rest of the class...

    def on_vendor_selected(self, event):
        selected_vendor = self.vendor_var.get()

        if selected_vendor == "Cisco":
            devices = ["Cisco CUBE", "Cisco Active", "Cisco SPAN"]
        elif selected_vendor == "Avaya":
            devices = ["Avaya Aura", "Avaya POM"]
        elif selected_vendor == "Genesys":
            devices = ["Genesys Connect", "Genesys PureEngage"]
        else:
            devices = []

        self.device_menu['values'] = devices
        self.device_var.set(devices[0] if devices else "")

    def generate_action(self):
        generate_action_logic(self)  # Call the logic function

    def run(self):
        # Display the logo at the top center
        logo_label = tk.Label(self.root, image=self.logo_photo)
        logo_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

        # Device dropdown
        device_label = tk.Label(self.root, text="Select Recording Type:")
        device_label.grid(row=2, column=0, padx=1, pady=0, sticky="w")

        devices = []  # Initial empty list
        self.device_var = tk.StringVar(value=devices)
        self.device_menu = ttk.Combobox(self.root, textvariable=self.device_var)
        self.device_menu.grid(row=2, column=1, padx=1, pady=0, sticky="w")

        # License type dropdown
        license_type_label = tk.Label(self.root, text="Select License Type:")
        license_type_label.grid(row=3, column=0, padx=1, pady=0, sticky="w")

        license_types = ["Concurrent", "Standard"]
        self.license_type_var = tk.StringVar(value=license_types[0])
        license_type_menu = ttk.Combobox(self.root, textvariable=self.license_type_var, values=license_types)
        license_type_menu.grid(row=3, column=1, padx=1, pady=0, sticky="w")

        # Analytics checkbox
        self.analytics_checkbox = tk.Checkbutton(self.root, text="Analytics Required", variable=self.analytics_var)
        self.analytics_checkbox.grid(row=4, column=1, padx=1, pady=0, sticky="w")

        # Analytics option (GPU or CPU)
        analytics_option_label = tk.Label(self.root, text="Select Analytics Option:")
        analytics_option_label.grid(row=5, column=0, padx=1, pady=0, sticky="w")

        analytics_options = ["GPU", "CPU"]
        self.analytics_option_var = tk.StringVar(value="GPU")  # Default to GPU
        analytics_option_menu = ttk.Combobox(self.root, textvariable=self.analytics_option_var, values=analytics_options)
        analytics_option_menu.grid(row=5, column=1, padx=1, pady=0, sticky="w")

        # Average Call Time entry
        avg_call_time_label = tk.Label(self.root, text="Average Call Time (Seconds):")
        avg_call_time_label.grid(row=6, column=0, padx=1, pady=0, sticky="w")
        self.avg_call_time_var = tk.StringVar()
        avg_call_time_entry = tk.Entry(self.root, textvariable=self.avg_call_time_var)
        avg_call_time_entry.grid(row=6, column=1, padx=1, pady=0, sticky="w")

        # Number of Expected Calls entry
        expected_calls_label = tk.Label(self.root, text="Number of Expected Calls (Per Day):")
        expected_calls_label.grid(row=7, column=0, padx=1, pady=0, sticky="w")
        self.expected_calls_var = tk.StringVar()
        expected_calls_entry = tk.Entry(self.root, textvariable=self.expected_calls_var)
        expected_calls_entry.grid(row=7, column=1, padx=1, pady=0, sticky="w")

        # Number of Agents entry
        agents_label = tk.Label(self.root, text="Number of Agents:")
        agents_label.grid(row=8, column=0, padx=1, pady=0, sticky="w")
        self.agents_var = tk.StringVar()
        agents_entry = tk.Entry(self.root, textvariable=self.agents_var)
        agents_entry.grid(row=8, column=1, padx=1, pady=0, sticky="w")

        # Number of Extensions entry
        extensions_label = tk.Label(self.root, text="Number of Extensions:")
        extensions_label.grid(row=9, column=0, padx=1, pady=0, sticky="w")
        self.extensions_var = tk.StringVar()
        extensions_entry = tk.Entry(self.root, textvariable=self.extensions_var)
        extensions_entry.grid(row=9, column=1, padx=1, pady=0, sticky="w")

        # Checkboxes
        checkbox_label = tk.Label(self.root, text="Options:")
        checkbox_label.grid(row=10, column=0, padx=1, pady=0, sticky="w")

        self.with_dr_var = tk.IntVar()
        with_dr_checkbox = tk.Checkbutton(self.root, text="With DR", variable=self.with_dr_var)
        with_dr_checkbox.grid(row=11, column=0, padx=1, pady=0, sticky="w")

        self.with_backup_var = tk.IntVar()
        with_backup_checkbox = tk.Checkbutton(self.root, text="With Central Web", variable=self.with_backup_var)
        with_backup_checkbox.grid(row=12, column=0, padx=1, pady=0, sticky="w")

        # Generate button
        generate_button = tk.Button(self.root, text="Generate", command=self.generate_action)
        generate_button.grid(row=13, column=0, columnspan=2, pady=10)

        # Configure columns and rows for resizing
        for i in range(1):  # Assuming you have 3 columns
            self.root.columnconfigure(i, weight=0, minsize=20)  # Adjust minsize as needed

        for i in range(13):  # Assuming you have 13 rows
            self.root.rowconfigure(i, weight=0)

        # Start the main loop
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = VendorDeviceSelector(root)
    app.run()
