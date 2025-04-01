import webbrowser

allowedActions = {
    "open" : {
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "animepahe": "https://animepahe.ru/",
        "udemy": "https://www.udemy.com/",
    },

    "play" : {
        "willne": "https://youtu.be/TDP9vQqcLvM?si=mxhY0tj2JxJzsEKg",
        "mrballen": "https://youtu.be/SdsoQXoG6OQ?si=_z8iLQvzSjRKm_zE",
        "hasangaming": "https://youtu.be/N2fZYw6wrtE?si=9yiQdpJi78a6sme8",
        "zyox": "https://youtu.be/F3cqjYJKgQw?si=5WCoROlMWJ7DKwMF",
    },
}

action: str = input("Enter action to be done: ").lower()
specifics = action.split(" ")

for i in specifics[1:]:
    webbrowser.open(allowedActions.get(specifics[0]).get(i))