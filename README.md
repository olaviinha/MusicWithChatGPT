# Writing music with ChatGPT

Tips and tools for experimenting with writing music with the aid of [ChatGPT](https://ai.com). And with a loose goal of getting it as MIDI.

If you have tips, [please share](https://github.com/olaviinha/MusicWithChatGPT/discussions)!

## Additions to Message ("prompt")

These tips work as addition to your freely formed message to ChatGPT, where you ask for any musical notation. These tips usually result in notation only, meaning the converted MIDI file will be piano-only. Asking ChatGPT to produce notation with different instruments (such as drums) that would translate to MIDI seems hard and prone to failure so far.

Example messages: `Can you write an emotional sci-fi theme `...

- `in ABC notation?`<br>
Produces a copyable ABC notation block that can be copy-pasted to [abc2midi notebook](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/abc2midi.ipynb), which will convert it to a MIDI file and provide an instant download. So far this is the best method.

- `chord progression?`<br>
Produces textual chord progression that can be copy-pasted to [chords2midi notebook](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/chords2midi.ipynb), which will convert it to a MIDI file and provide an instant download.<br>
You may also quickly preview and edit provided chord progressions by copy-pasting them to [Chords Guru Turbo 100a Deluxe](https://ki.gy/cv) instead (midi export currently offline).

- `to a MIDI file using Python Mido?`<br>
Produces a copyable code block that can be copy-pasted directly to [mido2midi notebook](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/mido2midi.ipynb) and executed, saving a MIDI file (providing ChatGPT did it right).<br>
**Note:** you don't have to understand any of the code, all you need to do is copy-paste it.<br>
**Fair warning:** this method is prone to failures (sour code from ChatGPT) and generally sounds like more random notation.

You may additionally want to make your request more specific by adding more sentences to your prompt, such as `It should be in A major. It should have a verse, a bridge and a chorus.`

## Tools

- [abc2midi](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/abc2midi.ipynb) – saves ABC notation as MIDI file.
- [chords2midi](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/chords2midi.ipynb) – saves textual chord progression as MIDI file.
- [mido2midi](https://colab.research.google.com/github/olaviinha/MusicWithChatGPT/blob/main/mido2midi.ipynb) – executes Mido code block, thus saving a MIDI file.
- [Chords Guru Turbo 100a Deluxe](https://ki.gy/cv) – quickly preview/edit textual chord progressions.
