print("📞 Call Outcome Analyzer Started\n")

call_logs = []

while True:
    print("1. Add call outcome")
    print("2. Analyze outcomes")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        outcome = input("Enter call outcome: ")
        call_logs.append(outcome)
        print("✅ Outcome recorded\n")

    elif choice == "2":
        summary = {
            "successful": 0,
            "follow_up": 0,
            "failed": 0
        }

        for call in call_logs:
            text = call.lower()
            if "paid" in text or "settled" in text:
                summary["successful"] += 1
            elif "later" in text or "callback" in text:
                summary["follow_up"] += 1
            else:
                summary["failed"] += 1

        print("\n📊 Call Outcome Summary")
        for key, value in summary.items():
            print(f"{key.replace('_',' ').title()}: {value}")
        print()

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid option\n")
