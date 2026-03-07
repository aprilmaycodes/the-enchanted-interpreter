# Sigil 1: The Traveling Merchant

*The first sigil of the room is carved into the wall above the supply shelves — faint, but present. A strip of parchment is pinned beside it with a list of current stock. Beneath it, the merchant's posted prices.*

*You'll need to figure out what to buy, what it'll cost, and make sure you're not overpaying.*

---

## Objective

The merchant is coming in a few days. Using the current stock levels and the merchant's prices, calculate your order and the total cost after the discount.

You've been left the following information:

**Current Inventory:**
```
Healing Herb Bundles: 3
Moon Salt Jars: 1
Empty Potion Vials: 7
```

Grandma's notes said the cellar should always have at least:
```
Healing Herb Bundles: 10
Moon Salt Jars: 5
Potion Vials: 24
```

**Merchant's Prices:**
```
Healing Herbs — 4 gold per bundle
Moon Salt — 6 gold per jar
Potion Vial Packs — sold in packs of 5 for 9 gold
Individual Vials - 2 gold per vial
```

**Discount:** 12 gold off the total

**Tax:** 8% of the total - be sure he applies this after the discount

---

Your program should:

1. Calculate the quantity of each item to purchase
2. Calculate the cost of each item
3. Apply the discount and tax to get the final total
4. Print a formatted order summary

## Expected Output
```
Order Summary

Healing herb bundles: 7 at $28
Moon Salt Jars: 4 at $24
Potion vial packs: 3 at $27
Individual potion vials: 2 at $4

Subtotal: $83
After discount: $71
Final total after tax: $76.68
```

---

## Tips
- Think carefully about which operations you need and in what order
- `//` and `%` may come in handy depending on your quantities
---

## Solution
A sample solution is available [here](solution.py). Give it a genuine try before peeking — the magic only works if **you** do the work.

---
