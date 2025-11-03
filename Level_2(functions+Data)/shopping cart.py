# Available items and their prices
items_lst = {
    'book': 40,
    'bags': 200,
    'pen': 10,
    'pencil': 5,
    'eraser': 5,
    'crayons': 20
}

cart = dict()

print("======= Welcome to Online Book Store =======")
print("Here are the items we have:")
for item, price in items_lst.items():
    print(f"{item}: ₹{price}")
print("===========================================\n")

while True:
    item = input("Enter item name to add/remove (or type 'stop' to exit): ").lower()

    if item == 'stop':
        break

    if item not in items_lst:
        print("⚠️ Item not found in store. Please try again.\n")
        continue

    action = input("Type 'add' to add or 'remove' to remove: ").lower()

    # ADD item
    if action == 'add':
        qty = int(input(f"Enter quantity of {item}: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"✅ Added {qty} {item}(s) to your cart.\n")

    # REMOVE item
    elif action == 'remove':
        if item in cart:
            qty = int(input(f"Enter quantity of {item} to remove: "))
            if qty >= cart[item]:
                del cart[item]
                print(f"❌ Removed all {item}(s) from your cart.\n")
            else:
                cart[item] -= qty
                print(f"❌ Removed {qty} {item}(s) from your cart.\n")
        else:
            print(f"⚠️ {item} is not in your cart.\n")

    else:
        print("⚠️ Invalid action. Please type 'add' or 'remove'.\n")

    # Show current cart
    print("🛒 Current Cart:")
    for k, v in cart.items():
        print(f"  {k} x{v} = ₹{items_lst[k] * v}")
    print()

# === Final Summary ===
print("\n======= Your Cart Summary =======")
total = 0
for item, qty in cart.items():
    cost = items_lst[item] * qty
    total += cost
    print(f"{item} x{qty} = ₹{cost}")

print(f"\nTotal before discount: ₹{total}")

# Apply discounts
discount = 0
if total >= 500:
    discount = total * 0.20  # 20%
elif total >= 200:
    discount = total * 0.10  # 10%

final_total = total - discount

print(f"Discount applied: ₹{discount}")
print(f"Final total to pay: ₹{final_total}")
print("=================================")
