"""
Package fastq contains fastq parsers and writers.

Fastq is a flat text file format developed in ~2000 to store nucleotide
sequencing data. While similar to fastq, fastq has a few differences. First,
the sequence identifier begins with @ instead of >, and includes quality
values for a sequence.

This package provides a parser and writer for working with Fastq formatted
sequencing data.

"""
# python wrapper for package github.com/bebop/poly/io/fastq within overall package poly
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
# from poly import fastq
# and then refer to everything using fastq. prefix
# packages imported by this package listed below:




# ---- Types ---

# Python type for slice []fastq.Fastq
class Slice_fastq_Fastq(go.GoClass):
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
			self.handle = _poly.Slice_fastq_Fastq_CTor()
			_poly.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Iterable):
					raise TypeError('Slice_fastq_Fastq.__init__ takes a sequence as argument')
				for elt in args[0]:
					self.append(elt)
	def __del__(self):
		_poly.DecRef(self.handle)
	def __str__(self):
		s = 'fastq.Slice_fastq_Fastq len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' ['
		if len(self) < 120:
			s += ', '.join(map(str, self)) + ']'
		return s
	def __repr__(self):
		return 'fastq.Slice_fastq_Fastq([' + ', '.join(map(str, self)) + '])'
	def __len__(self):
		return _poly.Slice_fastq_Fastq_len(self.handle)
	def __getitem__(self, key):
		if isinstance(key, slice):
			if key.step == None or key.step == 1:
				st = key.start
				ed = key.stop
				if st == None:
					st = 0
				if ed == None:
					ed = _poly.Slice_fastq_Fastq_len(self.handle)
				return Slice_fastq_Fastq(handle=_poly.Slice_fastq_Fastq_subslice(self.handle, st, ed))
			return [self[ii] for ii in range(*key.indices(len(self)))]
		elif isinstance(key, int):
			if key < 0:
				key += len(self)
			if key < 0 or key >= len(self):
				raise IndexError('slice index out of range')
			return Fastq(handle=_poly.Slice_fastq_Fastq_elem(self.handle, key))
		else:
			raise TypeError('slice index invalid type')
	def __setitem__(self, idx, value):
		if idx < 0:
			idx += len(self)
		if idx < len(self):
			_poly.Slice_fastq_Fastq_set(self.handle, idx, value.handle)
			return
		raise IndexError('slice index out of range')
	def __iadd__(self, value):
		if not isinstance(value, _collections_abc.Iterable):
			raise TypeError('Slice_fastq_Fastq.__iadd__ takes a sequence as argument')
		for elt in value:
			self.append(elt)
		return self
	def __iter__(self):
		self.index = 0
		return self
	def __next__(self):
		if self.index < len(self):
			rv = Fastq(handle=_poly.Slice_fastq_Fastq_elem(self.handle, self.index))
			self.index = self.index + 1
			return rv
		raise StopIteration
	def append(self, value):
		_poly.Slice_fastq_Fastq_append(self.handle, value.handle)
	def copy(self, src):
		""" copy emulates the go copy function, copying elements into this list from source list, up to min of size of each list """
		mx = min(len(self), len(src))
		for i in range(mx):
			self[i] = src[i]

# Python type for map map[string]string
class Map_string_string(go.GoClass):
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
			self.handle = _poly.Map_string_string_CTor()
			_poly.IncRef(self.handle)
			if len(args) > 0:
				if not isinstance(args[0], _collections_abc.Mapping):
					raise TypeError('Map_string_string.__init__ takes a mapping as argument')
				for k, v in args[0].items():
					_poly.Map_string_string_set(self.handle, k, v)
	def __del__(self):
		_poly.DecRef(self.handle)
	def __str__(self):
		s = 'poly.Map_string_string len: ' + str(len(self)) + ' handle: ' + str(self.handle) + ' {'
		if len(self) < 120:
			for k, v in self.items():
				s += str(k) + '=' + str(v) + ', '
		return s + '}'
	def __repr__(self):
		s = 'poly.Map_string_string({'
		for k, v in self.items():
			s += str(k) + '=' + str(v) + ', '
		return s + '})'
	def __len__(self):
		return _poly.Map_string_string_len(self.handle)
	def __getitem__(self, key):
		return _poly.Map_string_string_elem(self.handle, key)
	def __setitem__(self, key, value):
		_poly.Map_string_string_set(self.handle, key, value)
	def __delitem__(self, key):
		return _poly.Map_string_string_delete(self.handle, key)
	def keys(self):
		return go.Slice_string(handle=_poly.Map_string_string_keys(self.handle))
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
		return _poly.Map_string_string_contains(self.handle, key)


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---

# Python type for struct fastq.Fastq
class Fastq(go.GoClass):
	"""Fastq is a struct representing a single Fastq file element with an Identifier, its corresponding sequence, its quality score, and any optional pieces of data.\n"""
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
			self.handle = _poly.fastq_Fastq_CTor()
			_poly.IncRef(self.handle)
			if  0 < len(args):
				self.Identifier = args[0]
			if "Identifier" in kwargs:
				self.Identifier = kwargs["Identifier"]
			if  1 < len(args):
				self.Optionals = args[1]
			if "Optionals" in kwargs:
				self.Optionals = kwargs["Optionals"]
			if  2 < len(args):
				self.Sequence = args[2]
			if "Sequence" in kwargs:
				self.Sequence = kwargs["Sequence"]
			if  3 < len(args):
				self.Quality = args[3]
			if "Quality" in kwargs:
				self.Quality = kwargs["Quality"]
	def __del__(self):
		_poly.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'fastq.Fastq{'
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
		sv = 'fastq.Fastq ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	@property
	def Identifier(self):
		return _poly.fastq_Fastq_Identifier_Get(self.handle)
	@Identifier.setter
	def Identifier(self, value):
		if isinstance(value, go.GoClass):
			_poly.fastq_Fastq_Identifier_Set(self.handle, value.handle)
		else:
			_poly.fastq_Fastq_Identifier_Set(self.handle, value)
	@property
	def Optionals(self):
		return Map_string_string(handle=_poly.fastq_Fastq_Optionals_Get(self.handle))
	@Optionals.setter
	def Optionals(self, value):
		if isinstance(value, go.GoClass):
			_poly.fastq_Fastq_Optionals_Set(self.handle, value.handle)
		else:
			raise TypeError("supplied argument type {t} is not a go.GoClass".format(t=type(value)))
	@property
	def Sequence(self):
		return _poly.fastq_Fastq_Sequence_Get(self.handle)
	@Sequence.setter
	def Sequence(self, value):
		if isinstance(value, go.GoClass):
			_poly.fastq_Fastq_Sequence_Set(self.handle, value.handle)
		else:
			_poly.fastq_Fastq_Sequence_Set(self.handle, value)
	@property
	def Quality(self):
		return _poly.fastq_Fastq_Quality_Get(self.handle)
	@Quality.setter
	def Quality(self, value):
		if isinstance(value, go.GoClass):
			_poly.fastq_Fastq_Quality_Set(self.handle, value.handle)
		else:
			_poly.fastq_Fastq_Quality_Set(self.handle, value)

# Python type for struct fastq.Parser
class Parser(go.GoClass):
	"""Parser is a flexible parser that provides ample\ncontrol over reading fastq-formatted sequences.\nIt is initialized with NewParser.\n"""
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
			self.handle = _poly.fastq_Parser_CTor()
			_poly.IncRef(self.handle)
	def __del__(self):
		_poly.DecRef(self.handle)
	def __str__(self):
		pr = [(p, getattr(self, p)) for p in dir(self) if not p.startswith('__')]
		sv = 'fastq.Parser{'
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
		sv = 'fastq.Parser ( '
		for v in pr:
			if not callable(v[1]):
				sv += v[0] + '=' + str(v[1]) + ', '
		return sv + ')'
	def ParseAll(self):
		"""ParseAll() []object, str
		
		ParseAll parses all sequences in underlying reader only returning non-EOF errors.
		It returns all valid fastq sequences up to error if encountered.
		"""
		return Slice_fastq_Fastq(handle=_poly.fastq_Parser_ParseAll(self.handle))
	def ParseN(self, maxSequences):
		"""ParseN(int maxSequences) []object fastqs, str err
		
		ParseN parses up to maxSequences fastq sequences from the Parser's underlying reader.
		ParseN does not return EOF if encountered.
		If an non-EOF error is encountered it returns it and all correctly parsed sequences up to then.
		"""
		return Slice_fastq_Fastq(handle=_poly.fastq_Parser_ParseN(self.handle, maxSequences))
	def Reset(self, r, goRun=False):
		"""Reset(object r) 
		
		Reset discards all data in buffer and resets state.
		"""
		_poly.fastq_Parser_Reset(self.handle, r.handle, goRun)


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---
def NewParser(r, maxLineSize):
	"""NewParser(object r, int maxLineSize) object
	
	NewParser returns a Parser that uses r as the source
	from which to parse fastq formatted sequences.
	"""
	return Parser(handle=_poly.fastq_NewParser(r.handle, maxLineSize))


# ---- Functions ---
def Parse(r):
	"""Parse(object r) []object, str"""
	return Slice_fastq_Fastq(handle=_poly.fastq_Parse(r.handle))
def Read(path):
	"""Read(str path) []object, str"""
	return Slice_fastq_Fastq(handle=_poly.fastq_Read(path))
def ReadGz(path):
	"""ReadGz(str path) []object, str"""
	return Slice_fastq_Fastq(handle=_poly.fastq_ReadGz(path))
def Write(fastqs, path):
	"""Write([]object fastqs, str path) str
	
	Write writes a fastq array to a file.
	"""
	return _poly.fastq_Write(fastqs.handle, path)
def Build(fastqs):
	"""Build([]object fastqs) []int, str
	
	Build converts a Fastqs array into a byte array to be written to a file.
	"""
	return go.Slice_byte(handle=_poly.fastq_Build(fastqs.handle))


