#TODO 2 Zaprojektować funkcję dodawania, odejmowania, mnozenia, dzielenia, procentów
import main
class Functions:



    def sum(self, user1, user2):
        suma = user1 + user2
        return suma

    def diffrence(self, user1, user2):
        diff = user1 - user2
        return diff

    def multiplication(self, user1, user2):
        multiplication = user1 * user2
        return multiplication

    def division(self, user1, user2):
        division = user1 / user2
        return division

    def restart(self):
        restart = input("Do you want to restart calculator ? Y/N  ")
        if restart in ["y", "Y"]:
            print("Here we go again  ")
            return True
        elif restart in ["n", "N"]:
            return False
        else:
            print("You type wrong letter")
            return True

    def press(num):
        main.expression = main.expression + str(num)
        return main.expression


