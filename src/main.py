import requests


def get_cat_fact():
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        return response.json().get("fact")
    return "No fact found today :("


def main():
    print("Cat Fact: ", get_cat_fact())


if __name__ == "__main__":
    main()
