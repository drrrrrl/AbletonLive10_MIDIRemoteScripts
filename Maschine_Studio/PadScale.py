# Embedded file name: C:\ProgramData\Ableton\Live 9 Suite\Resources\MIDI Remote Scripts\Maschine_Studio\PadScale.py
# Compiled at: 2016-02-05 11:51:57


class PadScale:
    """ scale """
    __module__ = __name__

    def __init__(self, name, notevalues):
        isinstance(notevalues, tuple)
        self.name = name
        self.notevalues = notevalues
        scale_len = len(self.notevalues)
        rel_range = 16.0 / scale_len
        self.octave_range = int(10 - rel_range + 0.5)
        if self.octave_range < 0:
            self.octave_range = 0

    def to_octave(self, value):
        if self.octave_range == 0:
            return 0
        return int(value * self.octave_range)

    def to_relative(self, value, prev):
        if self.octave_range == 0:
            return prev
        relvalue = value / float(self.octave_range)
        if relvalue > 1.0:
            return 1.0
        if relvalue < 0.0:
            return 0.0
        return relvalue
