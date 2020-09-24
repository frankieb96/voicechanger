from pyo import *


server = Server().boot()

mic = Input().play().out()


# White noise generator
n = Noise(1)
n.ctrl()

# Common cutoff frequency control
freq = Sig(1000)
freq.ctrl([SLMap(50, 5000, "lin", "value", 1000)], title="Cutoff Frequency")

# Three different lowpass filters
tone = Tone(mic, freq)
butlp = ButLP(mic + n, freq)
mooglp = MoogLP(mic, freq)

# Interpolates between input objects to produce a single output
sel = Selector([tone, butlp, mooglp]).out()
sel.ctrl(title="Filter selector (0=Tone, 1=ButLP, 2=MoogLP)")

# Displays the spectrum contents of the chosen source
sp = Spectrum(sel)

server.gui(locals())