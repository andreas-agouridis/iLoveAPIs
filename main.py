import tkinter as tk
from tkinter import ttk, messagebox
from auth import verify_pin, setup_pin
from storage import load_apis, save_api, test_api

class ILOVEAPIsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("iLoveAPIs")
        self.root.geometry("700x450")

        self.pin = self.login()

        self.apis = load_apis(self.pin)

        self.create_ui()

    def login(self):
        pin_window = tk.Toplevel()
        pin_window.title("PIN Login")
        pin_window.geometry("300x180")
        pin_window.grab_set()

        tk.Label(pin_window, text="Enter PIN").pack(pady=10)

        pin_entry = tk.Entry(pin_window, show="*")
        pin_entry.pack()

        result = {"pin": None}

        def submit():
            pin = pin_entry.get()

            if verify_pin(pin):
                result["pin"] = pin
                pin_window.destroy()
            else:
                if setup_pin(pin):
                    result["pin"] = pin
                    pin_window.destroy()
                else:
                    messagebox.showerror("Error", "Wrong PIN")

        tk.Button(pin_window, text="Enter", command=submit).pack(pady=10)

        self.root.wait_window(pin_window)
        return result["pin"]

    def create_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(frame, text="API Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(frame, width=25)
        self.name_entry.grid(row=0, column=1)

        tk.Label(frame, text="API URL").grid(row=1, column=0)
        self.url_entry = tk.Entry(frame, width=40)
        self.url_entry.grid(row=1, column=1)

        tk.Label(frame, text="API Key").grid(row=2, column=0)
        self.key_entry = tk.Entry(frame, width=40, show="*")
        self.key_entry.grid(row=2, column=1)

        ttk.Button(frame, text="Add API", command=self.add_api).grid(row=3, column=0, pady=10)
        ttk.Button(frame, text="Test API", command=self.test_selected).grid(row=3, column=1)

        self.tree = ttk.Treeview(frame, columns=("Name", "URL"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("URL", text="URL")
        self.tree.grid(row=4, column=0, columnspan=2, sticky="nsew")

        for api in self.apis:
            self.tree.insert("", "end", values=(api["name"], api["url"]))

    def add_api(self):
        name = self.name_entry.get()
        url = self.url_entry.get()
        key = self.key_entry.get()

        if not name or not url:
            messagebox.showerror("Error", "Fill fields")
            return

        api = {
            "name": name,
            "url": url,
            "key": key
        }

        save_api(api, self.pin)
        self.tree.insert("", "end", values=(name, url))

        self.name_entry.delete(0, tk.END)
        self.url_entry.delete(0, tk.END)
        self.key_entry.delete(0, tk.END)

    def test_selected(self):
        selected = self.tree.selection()

        if not selected:
            return

        item = self.tree.item(selected[0])
        url = item["values"][1]

        works, status = test_api(url)

        if works:
            messagebox.showinfo("API Test", f"API Works ({status})")
        else:
            messagebox.showerror("API Test", f"Failed ({status})")


root = tk.Tk()
app = ILOVEAPIsApp(root)
root.mainloop()
