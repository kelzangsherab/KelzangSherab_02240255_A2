class PokemonCardBinder:
    
    MAX_POKEDEX_NUMBER = 1025
    CARDS_PER_PAGE = 64
    CARDS_PER_ROW = 9
    CARDS_PER_COLUMN = 9

    def __init__(self):
        self.binder = {}
        self.total_cards = 0

    def add_card(self, pokedex_number):
        if not self.is_valid_pokedex_number(pokedex_number):
            print("Invalid Pokedex number. Please enter a number (1-1025).")
            return
        
        if pokedex_number in self.binder:
            print(f"Pokedex {pokedex_number} already exists .")
            return
        
        page_number = self.calculate_page_number()
        position = self.calculate_position()

        self.binder[pokedex_number] = (page_number, position)
        self.total_cards += 1
        print(f"Page: {page_number} - Position: Row {position[0]}, Column {position[1]} Status: Added Pokedex {pokedex_number}")

        if self.total_cards >= self.MAX_POKEDEX_NUMBER:
            print("You have caught them all!!")

    def reset_binder(self):
        confirmation = input("WARNING: This will delete ALL Pokemon cards from the binder. This action cannot be undone. Type CONFIRM to reset or EXIT to return to the Main Menu: ")
        if confirmation == "CONFIRM":
            self.binder.clear()
            self.total_cards = 0
            print("The binder reset was successful! All cards have been removed.")
        else:
            print("Reset cancelled.")

    def display_cards(self):
        if not self.binder:
            print("The binder is empty.")
            print("Total cards in binder: 0")
            print("Completion: 0%")
            return
        
        print("Current Binder Contents:")
        for pokedex_number, (page, position) in self.binder.items():
            print(f"Pokedex {pokedex_number} - Page: {page} Position: Row {position[0]}, Column {position[1]}")
        
        completion_percentage = (self.total_cards / self.MAX_POKEDEX_NUMBER) * 100
        print(f"Total cards in binder: {self.total_cards} - Completion: {completion_percentage:.2f}%")

    def calculate_page_number(self):
        return (self.total_cards // self.CARDS_PER_PAGE) + 1

    def calculate_position(self):
        index = self.total_cards % self.CARDS_PER_PAGE
        row = (index // self.CARDS_PER_ROW) + 1
        column = (index % self.CARDS_PER_ROW) + 1
        return (row, column)

    def is_valid_pokedex_number(self, pokedex_number):
        return 1 <= pokedex_number <= self.MAX_POKEDEX_NUMBER


class MainMenu:
    
    def __init__(self):
        self.binder = PokemonCardBinder()

    def display_menu(self):
        while True:
            print("\nSelect option:")
            print("1. Add Pokémon Card")
            print("2. Reset Binder")
            print("3. View Current Binder")
            print("4. Exit")
            choice = input("Enter option: ")

            if choice == "1":
                try:
                    pokedex_number = int(input("Enter Pokedex number (1-1025): "))
                    self.binder.add_card(pokedex_number)
                except ValueError:
                    print("Invalid input! Please enter a valid integer.")
            elif choice == "2":
                self.binder.reset_binder()
            elif choice == "3":
                self.binder.display_cards()
            elif choice == "4":
                print("Thank you for using Pokémon Card Binder Manager!")
                break
            else:
                print("Invalid choice! try again.")


if __name__ == "__main__":
    MainMenu().display_menu()