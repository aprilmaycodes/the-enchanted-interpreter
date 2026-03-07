# Current inventory
current_herb_bundles = 3
current_salt_jars = 1
current_vials = 7

# Required amounts
herb_bundle_goal = 10
salt_jar_goal = 5
vial_goal = 24

# Merchant info
herbs_price = 4
salt_price = 6
vial_packs_price = 9
vial_price = 2

vials_per_pack= 5

discount = 12
tax = 0.08

# Determining how much to buy
herbs_to_buy = herb_bundle_goal - current_herb_bundles
salt_to_buy = salt_jar_goal - current_salt_jars
# This one is trickier - determine how many we need
vials_packs_needed = vial_goal - current_vials
# Then determine how many packs we can get
packs_to_buy = vials_packs_needed // vials_per_pack
# Then, how many more individual vials we need to get to the goal amount
vials_to_buy = vials_packs_needed % vials_per_pack

# determine totals
herbs_total = herbs_to_buy * herbs_price
salt_total = salt_to_buy * salt_price
packs_total = packs_to_buy * vial_packs_price
vials_total = vials_to_buy * vial_price

subtotal = herbs_total + salt_total + packs_total + vials_total

# Apply discount and tax
after_discount = subtotal - discount
tax_amount = after_discount * tax
final_total = after_discount + tax_amount


# Print order summary
print("Order Summary\n")

print(f"Healing herb bundles: {herbs_to_buy} for ${herbs_total}")
print(f"Moon Salt Jars: {salt_to_buy} for ${salt_total}")
print(f"Potion vial packs: {packs_to_buy} for ${packs_total}")
print(f"Individual potion vials: {vials_to_buy} for ${vials_total}\n")

print(f"Subtotal: ${subtotal}")
print(f"After discount: ${after_discount}")
print(f"Final total after tax: ${final_total}")