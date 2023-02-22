#!/usr/bin/env python3

# Prerequisites:
# pip install pychord mido

import os
import sys
import argparse
import random
import mido
from pychord import Chord
from mido import Message, MidiFile, MidiTrack, MetaMessage
  
def main(arguments):  

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--chords', help="Chords as midi notes in format \"60,62|70,73|80,82,84\"", type=str)
    parser.add_argument('--cpb', help="Play per chord", default=1, type=int)
    parser.add_argument('--bpm', help="BPM", default=120, type=int)
    parser.add_argument('--humanize', help="Humanize", default=None)
    parser.add_argument('--octave_shift', '--octave_shift', help="Octave shift", default=0, type=int)
    parser.add_argument('--outfile', help="Output file", type=str)
    args, leftovers = parser.parse_known_args()

    velocity_min = 64
    velocity_max = 84
    tpb = 128
    humanization_amount = 9
    if args.humanize != None: velocity_min = 74
    octave_shift = args.octave_shift or 0

    bar = tpb

    mid = MidiFile(ticks_per_beat=tpb)
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(MetaMessage('time_signature', numerator=4, denominator=4, clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
    track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(args.bpm), time=0))
    
    for i, chord in enumerate(args.chords.split('|')):
      for repeat in range(args.cpb):
        notes = chord.split(',')
        if args.octave_shift != 0: 
          notes = [int(note)+int(args.octave_shift) for note in notes]
        velocity = random.randrange(velocity_min, velocity_max) if velocity_min != velocity_max else velocity_max
        start = 0 if args.humanize == None else random.randint(0, humanization_amount)
        end = bar
        for note in notes:
          track.append(Message('note_on', note=int(note), velocity=velocity, time=start))
        for note in notes:
          track.append(Message('note_off', note=int(note), velocity=tpb-1, time=end))

    mid.save(args.outfile)
    print(args.outfile)
                          
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
