def show_menu():
    print("\n===== MENU =====")
    print("1. Greet")
    print("2. Add Numbers")
    print("3. Exit")
    print("================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            print(f"Hello, {name}!")
        elif choice == '2':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"Sum: {a + b}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
