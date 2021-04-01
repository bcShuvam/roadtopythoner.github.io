try:
    f = open("Dose_not.txt")

except Exception as e:
    print(f"This is Exceptional error {e}")

except EOFError as e:
    print(f"This is EOF Error {e}")

except IOError as e:
    print(f"This is IO error {e}")

else:
    print("It runs only if there is not except error")

finally:
    print("It runs any way after execution of try , except , else .")

