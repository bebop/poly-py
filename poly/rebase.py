"""
Package rebase contains a rebase parser for rebase data dump #31.

In order to effectively simulate cloning reactions, we need to know how each
restriction enzyme in the reaction functions. This data can be derived, in
bulk, from the REBASE database.

REBASE is an amazing resource run by New England Biolabs listing essentially
every known restriction enzyme. In particular, this parser parses the REBASE
data dump format #31, which is what Bioperl uses.

https://bioperl.org/howtos/Restriction_Enzyme_Analysis_HOWTO.html
http://rebase.neb.com/rebase/rebase.f31.html

The actual data dump itself is linked here and updated once a month:
http://rebase.neb.com/rebase/link_withrefm

The header of this file gives a wonderful explanation of its structure. Here is the
header with the commercial suppliers format and an example enzyme.

```
REBASE version 104                                              withrefm.104

	=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
	REBASE, The Restriction Enzyme Database   http://rebase.neb.com
	Copyright (c)  Dr. Richard J. Roberts, 2021.   All rights reserved.
	=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Rich Roberts                                                    Mar 31 2021

<ENZYME NAME>   Restriction enzyme name.
<ISOSCHIZOMERS> Other enzymes with this specificity.
<RECOGNITION SEQUENCE>

	These are written from 5' to 3', only one strand being given.
	If the point of cleavage has been determined, the precise site
	is marked with ^.  For enzymes such as HgaI, MboII etc., which
	cleave away from their recognition sequence the cleavage sites
	are indicated in parentheses.

	For example HgaI GACGC (5/10) indicates cleavage as follows:
	                5' GACGCNNNNN^      3'
	                3' CTGCGNNNNNNNNNN^ 5'

	In all cases the recognition sequences are oriented so that
	the cleavage sites lie on their 3' side.

	REBASE Recognition sequences representations use the standard
	abbreviations (Eur. J. Biochem. 150: 1-5, 1985) to represent
	ambiguity.
	                R = G or A
	                Y = C or T
	                M = A or C
	                K = G or T
	                S = G or C
	                W = A or T
	                B = not A (C or G or T)
	                D = not C (A or G or T)
	                H = not G (A or C or T)
	                V = not T (A or C or G)
	                N = A or C or G or T

	ENZYMES WITH UNUSUAL CLEAVAGE PROPERTIES:

	Enzymes that cut on both sides of their recognition sequences,
	such as BcgI, Bsp24I, CjeI and CjePI, have 4 cleavage sites
	each instead of 2.

	Bsp24I
	          5'      ^NNNNNNNNGACNNNNNNTGGNNNNNNNNNNNN^   3'
	          3' ^NNNNNNNNNNNNNCTGNNNNNNACCNNNNNNN^        5'

	This will be described in some REBASE reports as:

	             Bsp24I (8/13)GACNNNNNNTGG(12/7)

<METHYLATION SITE>

	The site of methylation by the cognate methylase when known
	is indicated X(Y) or X,X2(Y,Y2), where X is the base within
	the recognition sequence that is modified.  A negative number
	indicates the complementary strand, numbered from the 5' base
	of that strand, and Y is the specific type of methylation
	involved:
	               (6) = N6-methyladenosine
	               (5) = 5-methylcytosine
	               (4) = N4-methylcytosine

	If the methylation information is different for the 3' strand,
	X2 and Y2 are given as well.

<MICROORGANISM> Organism from which this enzyme had been isolated.
<SOURCE>        Either an individual or a National Culture Collection.
<COMMERCIAL AVAILABILITY>

	Each commercial source of restriction enzymes and/or methylases
	listed in REBASE is assigned a single character abbreviation
	code.  For example:

	K        Takara (1/98)
	M        Boehringer Mannheim (10/97)
	N        New England Biolabs (4/98)

	The date in parentheses indicates the most recent update of
	that organization's listings in REBASE.

<REFERENCES>only the primary references for the isolation and/or purification
of the restriction enzyme or methylase, the determination of the recognition
sequence and cleavage site or the methylation specificity are given.

REBASE codes for commercial sources of enzymes

	B        Life Technologies (3/21)
	C        Minotech Biotechnology (3/21)
	E        Agilent Technologies (8/20)
	I        SibEnzyme Ltd. (3/21)
	J        Nippon Gene Co., Ltd. (3/21)
	K        Takara Bio Inc. (6/18)
	M        Roche Applied Science (4/18)
	N        New England Biolabs (3/21)
	O        Toyobo Biochemicals (8/14)
	Q        Molecular Biology Resources - CHIMERx (3/21)
	R        Promega Corporation (11/20)
	S        Sigma Chemical Corporation (3/21)
	V        Vivantis Technologies (1/18)
	X        EURx Ltd. (1/21)
	Y        SinaClon BioScience Co. (1/18)

<1>AaaI
<2>XmaIII,BseX3I,BsoDI,BstZI,EagI,EclXI,Eco52I,SenPT16I,TauII,Tsp504I
<3>C^GGCCG
<4>
<5>Acetobacter aceti ss aceti
<6>M. Fukaya
<7>
<8>Tagami, H., Tayama, K., Tohyama, T., Fukaya, M., Okumura, H., Kawamura, Y., Horinouchi, S., Beppu, T., (1988) FEMS Microbiol. Lett., vol. 56, pp. 161-166.

```

"""
# python wrapper for package github.com/bebop/poly/io/rebase within overall package poly
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
# from poly import rebase
# and then refer to everything using rebase. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for map map[string]rebase.Enzyme
class Map_string_rebase_Enzyme(go.GoClass):
	""""""
	def __init__(self, *args, **kwargs):
		"""
		handle=A Go-side object is always initialized with an explicit handle=arg
		otherwise parameter is a python list that we copy from
		"""
		self.index = 0
		if len(kwargs) == 1 and 'handle' in kwargs:
			self.handle = kwargs['handle']
			_poly.IncRef(self.handle)
		elif len(args) == 1 and isinstance(args[0], go.GoClass):
			self.handle = args[0].handle
			_poly.IncRef(self.handle)
		else:
			self.handle = _poly.Map_string_rebase_Enzyme_CTor()
			_poly.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Mapping):
					raise TypeError('Map_string_rebase_Enzyme.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_poly.Map_string_rebase_Enzyme_set(self.handle, k, v)
	def __del__(self):
		_poly.DecRef(self.handle)
	def __str__(self):
		s = 'poly.Map_string_rebase_Enzyme len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'poly.Map_string_rebase_Enzyme({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _poly.Map_string_rebase_Enzyme_len(self.handle)
	def __getitem__(self, key):
		return Enzyme(handle=_poly.Map_string_rebase_Enzyme_elem(self.handle, key))
	def __setitem__(self, key, value):
		_poly.Map_string_rebase_Enzyme_set(self.handle, key, value.handle)
	def __delitem__(self, key):
		return _poly.Map_string_rebase_Enzyme_delete(self.handle, key)
	def keys(self):
		return go.Slice_string(handle=_poly.Map_string_rebase_Enzyme_keys(self.handle))
	def values(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append(self[k])
		return vls
	def items(self):
		vls = []
		kys = self.keys()
		for k in kys:
			vls.append((k, self[k]))
		return vls
	def __iter__(self):
		return iter(self.items())
	def __contains__(self, key):
		return _poly.Map_string_rebase_Enzyme_contains(self.handle, key)


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct rebase.Enzyme
class Enzyme(go.GoClass):
	"""Enzyme represents a single enzyme within the Rebase database\n"""
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
			self.handle = _poly.rebase_Enzyme_CTor()
			_poly.IncRef(self.handle)
			if  0 < len(args):
				self.Name = args[0]
			if "Name" in kwargs:
				self.Name = kwargs["Name"]
			if  1 < len(args):
				self.Isoschizomers = args[1]
			if "Isoschizomers" in kwargs:
				self.Isoschizomers = kwargs["Isoschizomers"]
			if  2 < len(args):
				self.RecognitionSequence = args[2]
			if "RecognitionSequence" in kwargs:
				self.RecognitionSequence = kwargs["RecognitionSequence"]
			if  3 < len(args):
				self.MethylationSite = args[3]
			if "MethylationSite" in kwargs:
				self.MethylationSite = kwargs["MethylationSite"]
			if  4 < len(args):
				self.MicroOrganism = args[4]
			if "MicroOrganism" in kwargs:
				self.MicroOrganism = kwargs["MicroOrganism"]
			if  5 < len(args):
				self.Source = args[5]
			if "Source" in kwargs:
				self.Source = kwargs["Source"]
			if  6 < len(args):
				self.CommercialAvailability = args[6]
			if "CommercialAvailability" in kwargs:
				self.CommercialAvailability = kwargs["CommercialAvailability"]
			if  7 < len(args):
				self.References = args[7]
			if "References" in kwargs:
				self.References = kwargs["References"]
	def __del__(self):
		_poly.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'rebase.Enzyme{'
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
		sv = 'rebase.Enzyme ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Name(self):
		return _poly.rebase_Enzyme_Name_Get(self.handle)
	@Name.setter
	def Name(self, value):
		if isinstance(value, go.GoClass):
			_poly.rebase_Enzyme_Name_Set(self.handle, value.handle)
		else:
			_poly.rebase_Enzyme_Name_Set(self.handle, value)
	@property
	def Isoschizomers(self):
		return go.Slice_string(handle=_poly.rebase_Enzyme_Isoschizomers_Get(self.handle))
	@Isoschizomers.setter
	def Isoschizomers(self, value):
		if isinstance(value, go.GoClass):
			_poly.rebase_Enzyme_Isoschizomers_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def RecognitionSequence(self):
		return _poly.rebase_Enzyme_RecognitionSequence_Get(self.handle)
	@RecognitionSequence.setter
	def RecognitionSequence(self, value):
		if isinstance(value, go.GoClass):
			_poly.rebase_Enzyme_RecognitionSequence_Set(self.handle, value.handle)
		else:
			_poly.rebase_Enzyme_RecognitionSequence_Set(self.handle, value)
	@property
	def MethylationSite(self):
		return _poly.rebase_Enzyme_MethylationSite_Get(self.handle)
	@MethylationSite.setter
	def MethylationSite(self, value):
		if isinstance(value, go.GoClass):
			_poly.rebase_Enzyme_MethylationSite_Set(self.handle, value.handle)
		else:
			_poly.rebase_Enzyme_MethylationSite_Set(self.handle, value)
	@property
	def MicroOrganism(self):
		return _poly.rebase_Enzyme_MicroOrganism_Get(self.handle)
	@MicroOrganism.setter
	def MicroOrganism(self, value):
		if isinstance(value, go.GoClass):
			_poly.rebase_Enzyme_MicroOrganism_Set(self.handle, value.handle)
		else:
			_poly.rebase_Enzyme_MicroOrganism_Set(self.handle, value)
	@property
	def Source(self):
		return _poly.rebase_Enzyme_Source_Get(self.handle)
	@Source.setter
	def Source(self, value):
		if isinstance(value, go.GoClass):
			_poly.rebase_Enzyme_Source_Set(self.handle, value.handle)
		else:
			_poly.rebase_Enzyme_Source_Set(self.handle, value)
	@property
	def CommercialAvailability(self):
		return go.Slice_string(handle=_poly.rebase_Enzyme_CommercialAvailability_Get(self.handle))
	@CommercialAvailability.setter
	def CommercialAvailability(self, value):
		if isinstance(value, go.GoClass):
			_poly.rebase_Enzyme_CommercialAvailability_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def References(self):
		return _poly.rebase_Enzyme_References_Get(self.handle)
	@References.setter
	def References(self, value):
		if isinstance(value, go.GoClass):
			_poly.rebase_Enzyme_References_Set(self.handle, value.handle)
		else:
			_poly.rebase_Enzyme_References_Set(self.handle, value)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def Read(path):
	"""Read(str path) object, str
	
	Read returns an enzymeMap from a Rebase data dump
	"""
	return Map_string_rebase_Enzyme(handle=_poly.rebase_Read(path))
def Export(enzymeMap):
	"""Export(object enzymeMap) []int, str
	
	Export returns a json file of the Rebase database
	"""
	return go.Slice_byte(handle=_poly.rebase_Export(enzymeMap.handle))
def Parse(file):
	"""Parse(object file) object, str
	
	Parse parses the Rebase database into a map of enzymes
	"""
	return Map_string_rebase_Enzyme(handle=_poly.rebase_Parse(file.handle))


