from flask import Flask, render_template, request

app = Flask(__name__)

# Extended English dictionary
kamus = {
    "apple": "a round fruit with red or green skin and a sweet taste",
    "banana": "a long, curved fruit with a yellow skin and soft, sweet, white flesh inside",
    "cat": "a small domesticated carnivorous mammal with soft fur",
    "dog": "a domesticated carnivorous mammal that typically has a long snout and an acute sense of smell",
    "elephant": "a large mammal with a trunk, native to Africa and southern Asia",
    "frog": "a tailless amphibian with a short squat body, moist smooth skin, and very long hind legs",
    "giraffe": "a large African mammal with a very long neck and forelegs",
    "house": "a building for human habitation",
    "ice": "frozen water, a brittle transparent crystalline solid",
    "jaguar": "a large heavily built cat native to Central and South America",
    "kangaroo": "a large plant-eating marsupial with powerful hind legs for leaping, native to Australia",
    "kaleidoscope": "an optical instrument with two or more reflecting surfaces inclined to each other",
    "kayak": "a small, narrow watercraft which is typically propelled by means of a double-bladed paddle",
    "karma": "the sum of a person's actions, viewed as deciding their fate in future existences",
    "lion": "a large carnivorous feline mammal that is native to Africa and India",
    "monkey": "a small to medium-sized primate that typically has a long tail",
    "nest": "a structure or place made or chosen by a bird for laying eggs and sheltering its young",
    "owl": "a nocturnal bird of prey with large forward-facing eyes surrounded by facial disks",
    "panda": "a large bear-like mammal with characteristic black-and-white markings",
    "queen": "the female ruler of an independent state, especially one who inherits the position by right of birth",
    "rabbit": "a burrowing, plant-eating mammal with long ears",
    "snake": "a long, limbless reptile which has no eyelids, a short tail, and jaws that are capable of considerable extension",
    "tiger": "a large cat species found in Asia, known for its striped coat",
    "umbrella": "a device for protection from the rain or sun, consisting of a folding frame covered with fabric",
    "vulture": "a large bird of prey that typically feeds on carrion",
    "wolf": "a wild carnivorous mammal of the dog family, living and hunting in packs",
    "xylophone": "a musical instrument played by striking a row of wooden bars of graduated length with one or more small wooden or plastic mallets",
    "yak": "a large domesticated wild ox with shaggy hair, native to the highlands of Central Asia",
    "zebra": "an African wild horse with black-and-white stripes and an erect mane",
}

# Function to search for words that start with the user's input
def cari_kata_awalan(awalan):
    hasil = {kata: arti for kata, arti in kamus.items() if kata.startswith(awalan.lower())}
    return hasil

# Route for the main page
@app.route("/", methods=["GET", "POST"])
def index():
    hasil = {}
    if request.method == "POST":
        awalan = request.form.get("awalan").lower()
        if awalan:
            hasil = cari_kata_awalan(awalan)
    
    return render_template("index.html", hasil=hasil)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
