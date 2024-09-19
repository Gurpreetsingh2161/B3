
with open("test_view.csv","r") as file:
    content=file.read()
    rows=content.split("\n")
    for row in rows:
        print(f"row is {row}")
        cols=row.split(",")
        for col in cols:
            print(col)
    print(content)
