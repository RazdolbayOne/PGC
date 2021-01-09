import tkinter as tk
import webbrowser

WINDOW_WIDTH = 300
WINDOW_HEIGHT=200
#window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))

def current_price_of_tesla(event):
    webbrowser.open_new_tab('https://duckduckgo.com/?q=current+price+of+tesla+shares&ia=stock')

def current_price_of_bitcoin(event):
    webbrowser.open_new_tab('https://www.coinbase.com/price/bitcoin')


window=tk.Tk()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
window.title("GCP")

#alocated
allocated_label = tk.Label(text = "Allocated", font=("Times new roman",10))
allocated_label.grid(column=0,row=2)

allocated_amount = tk.StringVar()
allocated_amount_entry = tk.Entry(window, textvariable=allocated_amount)
allocated_amount_entry.grid(column=0,row=3)


#buyed then stock was
buyed_label = tk.Label(text = "Buyed at price", font=("Times new roman",10))
buyed_label.grid(column=3,row=2)

buyed_stock_price = tk.StringVar()
buyed_stock_entry = tk.Entry(window, textvariable=buyed_stock_price)
buyed_stock_entry.grid(column=3,row=3)

#current stock price
current_stock_label = tk.Label(text = "current stock", font=("Times new roman",10))
current_stock_label.grid(column=0,row=4)

current_stock_price = tk.StringVar()
current_stock_price_entry = tk.Entry(window, textvariable=current_stock_price)
current_stock_price_entry.grid(column=0,row=5)

#buttons to manualy get info about current prices
button_for_tesla=tk.Button(window, text="Tesla", bg="orange")
button_for_tesla.grid(column=1, row=1)
button_for_bitcoin=tk.Button(window, text="Bitcoin", bg="pink")
button_for_bitcoin.grid(column=3, row=1)

#for button to calc current profit
profit_calc_button=tk.Button(window, text="CALC_CURRENT_PROFIT", bg="blue")
profit_calc_button.grid(column=0, row=6)

button_for_tesla.bind("<Button-1>", current_price_of_tesla)
button_for_bitcoin.bind("<Button-1>", current_price_of_bitcoin)

window.mainloop()
