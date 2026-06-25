from tkinter import *

# Menu prices

foods = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Salad": 4.99,
    "Soda": 1.99,
    "Fries": 2.99,
    "Fish": 2.99,
    "Spaghetti": 7.99,
    "Chicken": 6.99,
    "Burrito": 4.99,
    "Taco": 3.99
}

# display selected items

quantity = 1

def select_food(food):
    global quantity
    quantity = 1

    selected_food.set(food)

    name_label.config(text=food)
    price = foods[food]

    price_value.config(text=f"${price:.2f}")
    quantity_label.config(text=str(quantity))
    total_value.config(text=f"${price:.2f}")


def increase():
    global quantity

    quantity += 1
    quantity_label.config(text=str(quantity))

    price = foods[selected_food.get()]
    total = price * quantity

    total_value.config(text=f"${total:.2f}")


def decrease():
    global quantity

    if quantity > 1:
        quantity -= 1

    quantity_label.config(text=str(quantity))

    price = foods[selected_food.get()]
    total = price * quantity

    total_value.config(text=f"${total:.2f}")


# window

root = Tk()
root.title("Chakula menu")
root.geometry("900x550")
root.configure(bg="white")

selected_food = StringVar()
selected_food.set("Burger")

# left frame

left = Frame(root, bg="black", width=250)
left.pack(side=LEFT, fill=Y)

title = Label(left,
              text="Menu",
              font=("Arial",25,"bold"),
              bg="cyan")
title.pack(pady=20)

for food in foods:

    Button(left,
           text=f"{food:<15} ${foods[food]:.2f}",
           width=22,
           height=2,
           font=("Arial",12),
           command=lambda f=food: select_food(f)
           ).pack(pady=5)

# ------------------ RIGHT ------------------

right = Frame(root, bg="red")
right.pack(fill=BOTH, expand=True, padx=20, pady=20)

name_label = Label(right,
                   text="Burger",
                   font=("Arial",28,"bold"),
                   bg="yellow")
name_label.pack(anchor="w")

Label(right,
      text="Price",
      font=("Arial",18),
      bg="gold").pack(anchor="w", pady=(40,0))

price_value = Label(right,
                    text="$5.99",
                    font=("Arial",18,"bold"),
                    bg="gold")

price_value.pack(anchor="e")

Label(right,
      text="Amount",
      font=("Arial",18),
      bg="gold").pack(anchor="w", pady=(25,0))

amount_frame = Frame(right,bg="gold")
amount_frame.pack(anchor="e")

Button(amount_frame,
       text="-",
       font=("Arial",18),
       width=3,
       command=decrease).pack(side=LEFT)

quantity_label = Label(amount_frame,
                       text="1",
                       width=5,
                       font=("Arial",18),
                       bg="gold")

quantity_label.pack(side=LEFT)

Button(amount_frame,
       text="+",
       font=("Arial",18),
       width=3,
       command=increase).pack(side=LEFT)

Label(right,
      text="Total",
      font=("Arial",22,"bold"),
      bg="gold",
      width=20,
      anchor="w").pack(pady=40)

total_value = Label(right,
                    text="$5.99",
                    font=("Arial",22,"bold"),
                    bg="gold")

total_value.pack()

root.mainloop()