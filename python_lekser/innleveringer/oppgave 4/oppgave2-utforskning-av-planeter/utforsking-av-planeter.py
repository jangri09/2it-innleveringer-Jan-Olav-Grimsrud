import sys
from pathlib import Path

# Legg til mappen oppgave1-romfartoy i søkestien
sys.path.append(str(Path(__file__).parent.parent / "oppgave1-romfartoy"))

from romfartoy import Romfartoy

the_odyssey = Romfartoy("The Odyssey", 10000, 2)
the_odyssey.presenter()
