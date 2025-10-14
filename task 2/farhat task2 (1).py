movies = [
    ("Sunshine of the Spotless Mind", 2000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean", 37900000),
    ("Avengers: Age of Ultron", 200000000),
    ("Avengers: Endgame", 365000000)
]


total = 2000000 + 4500000 + 37900000 + 200000000 + 365000000
average = total / 5

high_budget = []
for movie, budget in movies:
    if budget > average:
        high_budget.append((movie, budget))

print(f"Average budget: ${average:,.2f}")
print("High budget movies:")
for movie, budget in high_budget:
    print(f"- {movie}: ${budget:,}")