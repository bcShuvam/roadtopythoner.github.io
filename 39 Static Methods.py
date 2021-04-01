class StaticMethods:
    @staticmethod
    def no_self(string):
        print(f"It dose not use {string} as an argument")

StaticMethods.no_self("Self")