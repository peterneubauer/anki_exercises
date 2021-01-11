import genanki

my_model = genanki.Model(
    1376484377,
    "Exercises",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
)

prefix = "Piano_personal"


# A deck contining combinations of 2-5-1 exercises, inspired by the suggestions at https://www.youtube.com/watch?v=-bH30kwMbm0&t=434s&ab_channel=WalkThatBass
def create251():
    my_deck = genanki.Deck(2059400110, f"{prefix}::2-5-1 Exercises")

    for rh in [
        "7th Chords, base form",
        "7th Chords, second inversion",
        "Improv",
        "Keep closest",
    ]:
        for lh in ["Baseline", "Stride base 7th", "Keep closest"]:
            for style in ["Bossa", "Jazz ballad", "Waltz"]:
                for progression in [
                    "2m-5-1",
                    "2dim-5-1min",
                    "6m-2m-5-1-4-7dim-3-6m",
                ]:
                    for movement in ["whole step down", "chromatic down", "up a forth"]:
                        my_note = genanki.Note(
                            model=my_model,
                            fields=[
                                f"<b>Progression:</b>: {progression}<br/><b>LH:</b> {lh}, <b>RH:</b> {rh}<br/><b>Move:</b> {movement}<br/><b>Style:</b> {style}",
                                "Date:             BPM:",
                            ],
                        )
                        my_deck.add_note(my_note)
    genanki.Package(my_deck).write_to_file("piano_2-5-1_exercises.apkg")


# Rythm exercises that combine on-and off beat elements in order to train random combinations
def rythm():

    my_deck = genanki.Deck(2059400111, f"{prefix}::Rythm Exercises")
    legend = "".join([f"{y+1}---" for y in range(0, 4)])
    beat = "".join(["----" for y in range(0, 4)])
    for lh in [
        "Blues shuffle, swing",
    ]:
        for rh in ["I6"]:
            for beat1 in [y * 4 for y in range(0, 4)]:
                for beat2 in [y * 4 + 2 for y in range(0, 4)]:
                    b1 = "".join((beat[:(beat1)], "O", beat[(beat1 + 1) :]))
                    # print(b1)
                    b2 = "".join((b1[:(beat2)], "o", b1[(beat2 + 1) :]))
                    ryt = "|" + "|".join([b2, b2]) + "|"
                    leg = "|" + "|".join([legend, legend]) + "|"
                    print(ryt)
                    print(leg)
                    my_note = genanki.Note(
                        model=my_model,
                        fields=[
                            f"""<b>LH:</b> {lh}, <b>RH:</b> {rh}<br/><b>Rythm</b>
                            <pre>{ryt}</pre>
                            <pre>{leg}</pre>",
                            """,
                            "",
                        ],
                    )
                    my_deck.add_note(my_note)
    genanki.Package(my_deck).write_to_file("rythm_exercises.apkg")


rythm()
create251()
