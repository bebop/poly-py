"""
Package fragment optimally fragments DNA for GoldenGate systems.

Optimal fragmentation is accomplished by using empirical fidelity data derived
by NEB in the paper "Enabling one-pot Golden Gate assemblies of unprecedented
complexity using data-optimized assembly design". We use the BsaI-T4 ligase
data provided in table S1.

Paper link: https://doi.org/10.1371/journal.pone.0238592
Data link: https://doi.org/10.1371/journal.pone.0238592.s001

"""
# python wrapper for package github.com/bebop/poly/synthesis/fragment within overall package fragment
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy build -output=poly/synthesis/fragment -vm=python3 github.com/bebop/poly/synthesis/fragment

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _fragment
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from fragment import fragment
# and then refer to everything using fragment. prefix
# packages imported by this package listed below:




# ---- Types ---


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def NextOverhang(currentOverhangs):
	"""NextOverhang([]str currentOverhangs) str
	
	NextOverhang gets next most efficient overhang to use for a given set of
	overhangs. This is useful for when developing a new set of standard
	overhangs. Note: NextOverhang is biased towards high AT overhangs, but this
	will not affect fidelity at all.
	"""
	return _fragment.fragment_NextOverhang(currentOverhangs.handle)
def SetEfficiency(overhangs):
	"""SetEfficiency([]str overhangs) float
	
	SetEfficiency gets the estimated fidelity rate of a given set of
	GoldenGate overhangs.
	"""
	return _fragment.fragment_SetEfficiency(overhangs.handle)


