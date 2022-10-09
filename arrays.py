import csv
old_references= ["POT-94000-FT-42"]
new_references = ["POT-94000-FT-43"]
headers = ["old_references", "new_references"]
dicts = [
    {
     "old_references": old,
     "new_references": new
    }
    for new, old in zip(new_references, old_references)
]
with open('test.csv', 'w') as f:
    writer = csv.DictWriter(f, list[dicts[0]])
    writer.writeheader()
    writer.writerows(dicts)