# Music with ChatGPT

Tips and tools for experimenting with writing music with the aid of ChatGPT, with a goal of ending up with MIDI notation.

## Message tips

These tips work as addition to your freely formed message, where you ask for any musical notation.

Example message: `Can you write an emotional sci-fi theme`...

- `in ABC notation?`<br>
Produces a copyable block that can be saved as `whatever.abc` and converted to MIDI using the [abc2midi notebook](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/abc2midi.ipynb).

- `in ABC notation that can be converted to MIDI using abc2midi?`<br>
Same as above, but less likely to contain errors.

- `using Python Mido?`<br>
Produces a copyable code block that can be executed using the [mido2midi notebook]() (coming soon). Note that you don't have to understand any of the code, all you need to do is copy/paste it.

- `chord progression?`<br>
Produces textual chord progression that can be converted to MIDI using the [chords2midi notebook]() (coming soon).<br>
You may also quickly previewed and edited chord progressions using [Chords Guru Turbo 100a Deluxe](https://ki.gy/cv).

## Tools

- [abc2midi]() – saves ABC notation as MIDI file.
- [mido2midi]() (coming soon) – executes Mido code block (saving as MIDI file, if ChatGPT did it right).
- [chords2midi]() (coming soon) – saves textual chord progression as MIDI file.
- [Chords Guru Turbo 100a Deluxe](https://ki.gy/cv) – quickly preview/edit textual chord progressions.
