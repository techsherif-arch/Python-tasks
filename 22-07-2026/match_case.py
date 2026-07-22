number = input("Enter your Emergency")
match number:
    case "police":
        print("Dial",100,"For Help")
    case "fire":
        print("Dial",101,"For Help")
    case "ambulance":
        print("Dial",108,"For Help")
    case "womenhelp":
        print("Dial",1091,"For Help")
    case _:
        print("Invalid Emergency")
