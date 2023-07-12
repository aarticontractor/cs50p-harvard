def main():
    emotion = input()
    print(convert(smiley=emotion), end="")
    # emotion = Great :)
    # or emotion = Sad :(

def convert(smiley):
    smiley = smiley.replace(":)", "🙂")
    smiley = smiley.replace(":(", "🙁")
    smiley = smiley.replace("\n", "")

    return smiley


main()

# great :(
# great 😔

# great :)
# great 😊

# great :) :(
# great 😊 :(
# great 😊 😔