import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import threading
import time
import os


ctk.set_appearance_mode("Dark") 

class AutumnQRPro(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Stardew Fall QR")
        self.geometry("500x750")
        self.logo_path = None
        self.animating = False

        # ---BACKGROUND SETUP---
        bg_image_path = "background.png"
        if os.path.exists(bg_image_path):
            bg_image = Image.open(bg_image_path)

            self.bg_photo = ctk.CTkImage(light_image=bg_image, dark_image=bg_image, size=(500, 750))
            self.bg_label = ctk.CTkLabel(self, image=self.bg_photo, text="")
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # --- MAIN CONTAINER ---
        self.main_frame = ctk.CTkFrame(
            self, 
            fg_color="transparent", 
            border_width=3, 
            border_color="#8B4513" 
        )
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.9)
        self.main_frame.grid_columnconfigure(0, weight=1)


        self.title_label = ctk.CTkLabel(
            self.main_frame, text="🍂 HARVEST QR", 
            font=ctk.CTkFont(family="Georgia", size=32, weight="bold"),
            text_color="#F39C12" 
        )
        self.title_label.grid(row=0, column=0, pady=(40, 5))

        # URL Entry with semi-dark background
        self.url_entry = ctk.CTkEntry(
            self.main_frame, placeholder_text="Enter link to harvest...", 
            width=300, height=45, border_color="#D35400", fg_color="#2D1E17"
        )
        self.url_entry.grid(row=1, column=0, pady=20)
        self.url_entry.bind('<Return>', lambda e: self.start_process())

        self.logo_btn = ctk.CTkButton(
            self.main_frame, text="🎁 Add Logo (Gift)", 
            fg_color="#3E2723", border_width=2, border_color="#E67E22",
            hover_color="#5D4037", command=self.pick_logo
        )
        self.logo_btn.grid(row=2, column=0, pady=10)
        
        self.submit_btn = ctk.CTkButton(
            self.main_frame, text="Ship QR Code", 
            font=ctk.CTkFont(size=18, weight="bold"), 
            fg_color="#D35400", hover_color="#A04000",
            height=55, width=200, command=self.start_process
        )
        self.submit_btn.grid(row=3, column=0, pady=30)

        self.loading_label = ctk.CTkLabel(self.main_frame, text="", font=("Arial", 16), text_color="#F1C40F")
        self.loading_label.grid(row=4, column=0)

        # Preview Frame 
        self.preview_frame = ctk.CTkFrame(
            self.main_frame, width=220, height=220, 
            fg_color="#2D1E17", border_width=2, border_color="#F39C12"
        )
        self.preview_frame.grid(row=5, column=0, pady=10)
        self.preview_frame.grid_propagate(False)

        self.preview_display = ctk.CTkLabel(self.preview_frame, text="Shipment Preview")
        self.preview_display.place(relx=0.5, rely=0.5, anchor="center")

    def animate_loading(self, angle=0):
        if self.animating:
            chars = ["🍂", "🎃", "🌽", "🍎"]
            char = chars[angle % len(chars)]
            self.loading_label.configure(text=f"{char} Brewing in the Keg...")
            self.after(200, lambda: self.animate_loading(angle + 1))

    def pick_logo(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if path:
            self.logo_path = path
            messagebox.showinfo("Item Added", "Logo selected for the shipment!")

    def start_process(self):
        if not self.url_entry.get():
            messagebox.showwarning("Empty Box", "You can't ship an empty crate! Enter a URL.")
            return
        self.submit_btn.configure(state="disabled")
        self.animating = True
        self.animate_loading()
        threading.Thread(target=self.generate_qr, daemon=True).start()

    def generate_qr(self):
        time.sleep(2) 
        data = self.url_entry.get()
        save_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Harvested QR")
        
        if save_path:
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(
                image_factory=StyledPilImage,
                color_mask=RadialGradiantColorMask(
                    back_color=(45, 30, 23),      # Deep Wood Brown
                    center_color=(255, 165, 0),   # Bright Pumpkin Orange
                    edge_color=(139, 69, 19)      # Saddle Brown
                ),
                module_drawer=RoundedModuleDrawer(),
                embedded_image_path=self.logo_path if self.logo_path else None
            )
            img.save(save_path)
            

            preview_img = img.resize((200, 200))
            self.tk_preview = ctk.CTkImage(light_image=preview_img, dark_image=preview_img, size=(200, 200))
            
            self.after(0, lambda: self.finish_process(True))
        else:
            self.after(0, lambda: self.finish_process(False))

    def finish_process(self, success):
        self.animating = False
        self.loading_label.configure(text="")
        self.submit_btn.configure(state="normal")
        if success:
            self.preview_display.configure(image=self.tk_preview, text="")
            messagebox.showinfo("Success", "The harvest is ready for shipment!")

if __name__ == "__main__":
    app = AutumnQRPro()
    app.mainloop()