"""
Package seqhash contains the seqhash algorithm.

This package contains the reference seqhash algorithm.

There is a big problem with current sequence databases - they all use different
identifiers and accession numbers. This means cross-referencing databases is
a complicated exercise, especially as the quantity of databases increases, or if
you need to compare "wild" DNA sequences.

Seqhash is a simple algorithm to produce consistent identifiers for any genetic sequence. The
basic premise of the Seqhash algorithm is to hash sequences with the hash being a robust
cross-database identifier. Sequences themselves shouldn't be used as a database index
(often, they're too big), so a hash based off of a sequence is the next best thing.

Usability wise, you should be able to Seqhash any rotation of a sequence in any direction and
get a consistent hash.

The Seqhash algorithm makes several opinionated design choices, primarily to make working
with Seqhashes more consistent and nice. The Seqhash algorithm only uses a single hash function,
Blake3, and only operates on DNA, RNA, and Protein sequences. These identifiers will be seen
by human beings, so versioning and metadata is attached to the front of the hashes so that
a human operator can quickly identify problems with hashing.

If the sequence is DNA or RNA, the Seqhash algorithm needs to know whether or not the nucleic
acid is circular and/or double stranded. If circular, the sequence is rotated to a deterministic
point. If double stranded, the sequence is compared to its reverse complement, and the lexicographically
minimal sequence is taken (whether or not the min or max is used doesn't matter, just needs to
be consistent).

If the sequence is RNA, the sequence will be converted to DNA before hashing. While the full Seqhash
will still be different between RNA and DNA (due to the metadata string), the hash afterwards will be the same.
This makes it easy to cross reference DNA and RNA sequences. This fact is important for parts of Poly
store that relate to storing and searching large quantities of sequences - deduplication can easily
be used on those Seqhashes to save a lot of space.

For DNA or RNA sequences, only ATUGCYRSWKMBDHVNZ characters are allowed. For Proteins,
only ACDEFGHIKLMNPQRSTVWYUO*BXZ characters are allowed in sequences. Selenocysteine (Sec; U) and pyrrolysine
(Pyl; O) are included in the protein character set - usually U and O don't occur within protein sequences,
but for certain organisms they do, and it is certainly a relevant amino acid for those particular proteins.

A Seqhash is separated into 3 different elements divided by underscores. It looks like the following:

v1_DCD_4b0616d1b3fc632e42d78521deb38b44fba95cca9fde159e01cd567fa996ceb9

The first element is the version tag (v1 for version 1). If there is ever a Seqhash version 2, this tag
will differentiate seqhashes. The second element is the metadata tag, which has 3 letters. The first letter
codes for the sequenceType (D for DNA, R for RNA, and P for Protein). The second letter codes for whether or
not the sequence is circular (C for Circular, L for Linear). The final letter codes for whether or not the
sequence is double stranded (D for Double stranded, S for Single stranded). The final element is the blake3
hash of the sequence (once rotated and complemented, as stated above).

Seqhash is a simple algorithm that allows for much better indexing of genetic sequences than what is
currently available.

"""
# python wrapper for package github.com/bebop/poly/seqhash within overall package poly
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
# from poly import seqhash
# and then refer to everything using seqhash. prefix
# packages imported by this package listed below:

from . import transform



# ---- Types ---


#---- Enums from Go (collections of consts with same type) ---


#---- Constants from Go: Python can only ask that you please don't change these! ---
DNA = "DNA"
PROTEIN = "PROTEIN"
RNA = "RNA"


# ---- Global Variables: can only use functions to access ---


# ---- Interfaces ---


# ---- Structs ---


# ---- Slices ---


# ---- Maps ---


# ---- Constructors ---


# ---- Functions ---
def Hash(sequence, sequenceType, circular, doubleStranded):
	"""Hash(str sequence, str sequenceType, bool circular, bool doubleStranded) str, str
	
	Hash is a function to create Seqhashes, a specific kind of identifier.
	"""
	return _poly.seqhash_Hash(sequence, sequenceType, circular, doubleStranded)
def RotateSequence(sequence):
	"""RotateSequence(str sequence) str
	
	RotateSequence rotates circular sequences to deterministic point.
	"""
	return _poly.seqhash_RotateSequence(sequence)


