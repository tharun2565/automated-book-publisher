def human_edit(text, filename="edited.txt"):
    print("AI output saved in ‘edited.txt’. Open it and make changes.")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    input("Press Enter after you finish editing...")
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

