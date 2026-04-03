import requests

def get_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Could not fetch a joke."

if __name__ == "__main__":
    print(get_random_joke())