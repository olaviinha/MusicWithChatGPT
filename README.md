# Music with ChatGPT

Tips and tools for writing music with the aid of ChatGPT. With a loose goal of getting MIDI.

## Additions to Message

These tips work as addition to your freely formed message to ChatGPT, where you ask for any musical notation.

Example message: `Can you write an emotional sci-fi theme`...

- `in ABC notation?`<br>
Produces a copyable block that can be saved as `whatever.abc` using a text editor, and converted to a MIDI file using the [abc2midi notebook](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/abc2midi.ipynb).

- `to a MIDI file using Python Mido?`<br>
Produces a copyable code block that can be copy-pasted directly to [mido2midi notebook](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/mido2midi.ipynb) and executed, saving a MIDI file (providing ChatGPT did it right).<br>
**Note:** you don't have to understand any of the code, all you need to do is copy-paste it.
**Fair warning:** this method is prone to failures (sour code from ChatGPT) and generally sounds like more random notation.

- `one-line chord progression?`<br>
Produces textual chord progression that can be copy-pasted directly to chords2midi notebook (coming soon) and executed, saving a MIDI file.<br>
You may also quickly previewed and edited chord progressions using [Chords Guru Turbo 100a Deluxe](https://ki.gy/cv) (midi export currently offline due to Heroku's recent discontinuation of free tier)

## Tools

- [abc2midi]() – saves ABC notation as MIDI file.
- [mido2midi]() (coming soon) – executes Mido code block (saving as MIDI file, if ChatGPT did it right).
- [chords2midi]() (coming soon) – saves textual chord progression as MIDI file.
- [Chords Guru Turbo 100a Deluxe](https://ki.gy/cv) – quickly preview/edit textual chord progressions.
