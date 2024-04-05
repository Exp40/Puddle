import Responses, sys, time, random, string


def main():
    print("Hello, my name is Puddle.")
    user_name = input("What should I call you?")
    user_name = name_upper(user_name)
    print(f"{user_name} huh, I like that name")


if __name__ == "__main__":
    main()
