from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

filename = '考卷.RTF'
doc = Rtf15Reader.read( open(filename))
print(PlaintextWriter.write(doc).getvalue())