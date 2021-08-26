def convert_emojis(message):
    words = message.split(" ")
    emojis = {
        ":)": "HAPPY",
        ":(": "SAD",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(convert_emojis(message))
