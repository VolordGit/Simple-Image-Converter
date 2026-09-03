from PIL import Image
import tkinter as tk
from tkinter import filedialog




def convert_image(input_path, output_format):
    with Image.open(input_path) as img:
        output_path = input_path.rsplit('.', 1)[0] + '.' + output_format.lower()
        img.save(output_path, output_format)
        print(f"Image converted and saved as: {output_path}")



root = tk.Tk()
root.withdraw()

input_path = filedialog.askopenfilename(
    title="Select an image file",
    filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp"), ("All files", "*.*")]
)


print(f"Selected file: {input_path}")
print()
output_format = input("Enter the desired output format (e.g., 'JPEG', 'PNG', 'BMP'): ").upper()
print(f"Output format: {output_format}")



convert_image(input_path, output_format)





    

