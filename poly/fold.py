"""
Package fold is a package for folding DNA and RNA sequences into secondary structures.

This package provides everything you need to fold a DNA or RNA sequence into a secondary structure
and get the minimum free energy of the structure. Most of the code was ported from the
python SeqFold package by Lattice Automation and Joshua Timmons but we hope to have a
linear fold algorithm in the near future.

Biological context:

DNA, RNA, and proteins all fold. Protein is a particularly tricky thing to predict
partially because there are so many more amino acids than there are nucleotides.

ACG(T/U) vs. ACDEFGHIKLMNPQRSTVWY (20 amino acids)

These folding predictions help us understand how to design primers, guide RNAs, and
other nucleic acid sequences that fold into a particular structure.

Fortunately for us, DNA and RNA are much easier to predict because there are only 4 nucleotides
and the rules for folding are much more well defined.

Each function has citations to the original papers that describe the algorithms used.
Most of the algorithms used in this package are based on the work of Zuker and Stiegler, 1981
but we're hoping to add more algorithms in the near future such as linear fold.

TTFN,
Tim

"""
# python wrapper for package github.com/bebop/poly/fold within overall package poly
# This is what you import to use the package.
# File is generated by gopy. Do not edit.
# gopy pkg -vm=python3 github.com/bebop/poly

# the following is required to enable dlopen to open the _go.so file
import os,sys,inspect,collections
try:
	import collections.abc as _collections_abc
except ImportError:
	_collections_abc = collections

cwd = os.getcwd()
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(currentdir)
from . import _poly
from . import go

os.chdir(cwd)

# to use this code in your end-user python file, import it as follows:
# from poly import fold
# and then refer to everything using fold. prefix
# packages imported by this package listed below:

from . import transform
from . import checks



# ---- Types ---


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct fold.Result
class Result(go.GoClass):
	"""Result holds the resulting structures of the folded s\n"""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameters can be unnamed in order of field names or named fields
		in which case a new Go object is constructed first
		"""
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_poly.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_poly.IncRef(self.handle)
		else:
			self.handle = _poly.fold_Result_CTor()
			_poly.IncRef(self.handle)
	def __del__(self):
		_poly.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'fold.Result{'
		first = True
		for v in pr:
			if callable(v[1]):
				continue
			if first:
				first = False
			else:
				sv += ', '
			sv += v[0] + '=' + str(v[1])
		return sv + '}'
	def __repr__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'fold.Result ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def DotBracket(self):
		"""DotBracket() str
		
		DotBracket returns the dot-bracket notation of the secondary nucleic acid
		structure resulting from folding a sequence.
		
		Dot-bracket notation, consisting in a balanced parentheses string composed
		by a three-character alphabet {.,(,)}, that can be unambiguously converted
		in the RNA secondary structure. See example_test.go for a small example.
		"""
		return _poly.fold_Result_DotBracket(self.handle)
	def MinimumFreeEnergy(self):
		"""MinimumFreeEnergy() float
		
		MinimumFreeEnergy return just the delta G of the structures resulting from
		folding a sequence.
		
		Returns the minimum free energy of the folded sequence
		"""
		return _poly.fold_Result_MinimumFreeEnergy(self.handle)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def Zuker(seq, temp):
	"""Zuker(str seq, float temp) object, str
	
	Zuker folds the DNA sequence and return the lowest free energy score.
	
	Based on the approach described in:
	Zuker and Stiegler, 1981
	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC326673/pdf/nar00394-0137.pdf
	
	If the sequence is 50 or more bp long, "isolated" matching bp
	are ignored in pairedMinimumFreeEnergyV(start,end). This is based on an approach described in:
	Mathews, Sabina, Zuker and Turner, 1999
	https://www.ncbi.nlm.nih.gov/pubmed/10329189
	Args:
	
		seq: The sequence to Fold
		temp: The temperature the Fold takes place in, in Celsius
	
	Returns a slice of NucleicAcidStructure with the energy and description,
	i.e. stacks, bulges, hairpins, etc.
	"""
	return Result(handle=_poly.fold_Zuker(seq, temp))


# ---- Functions ---


