#!/usr/bin/env python3
# Created by: Enoch O
# Created on: April 24, 2025
# This code asks the user for their password.


def check_password():
    correct_password = input("Please set your initial password as integers: ")

    try:
        correct_password_int = int(correct_password)
        while True:
            password = int(input("Enter your password: "))
            if password == correct_password_int:
                print("Password accepted. Access granted!")
                break
            else:
                print("Incorrect password. Please try again.")
    except Exception:
        print(" Invalid input, please try again.")


if __name__ == "__main__":
    check_password()
