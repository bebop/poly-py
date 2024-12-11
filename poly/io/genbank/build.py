# python build stubs for package genbank
# File is generated by gopy. Do not edit.
# gopy build -output=poly/io/genbank -vm=python3 github.com/bebop/poly/io/genbank

from pybindgen import retval, param, Function, Module
import sys

class CheckedFunction(Function):
    def __init__(self, *a, **kw):
        super(CheckedFunction, self).__init__(*a, **kw)
        self._failure_expression = kw.get('failure_expression', '')
        self._failure_cleanup = kw.get('failure_cleanup', '')

    def set_failure_expression(self, expr):
        self._failure_expression = expr

    def set_failure_cleanup(self, expr):
        self._failure_cleanup = expr

    def generate_call(self):
        super(CheckedFunction, self).generate_call()
        check = "PyErr_Occurred()"
        if self._failure_expression:
            check = "{} && {}".format(self._failure_expression, check)
        failure_cleanup = self._failure_cleanup or None
        self.before_call.write_error_check(check, failure_cleanup)

def add_checked_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

def add_checked_string_function(mod, name, retval, params, failure_expression='', *a, **kw):
    fn = CheckedFunction(name, retval, params, *a, **kw)
    fn.set_failure_cleanup('if (retval != NULL) free(retval);')
    fn.after_call.add_cleanup_code('free(retval);')
    fn.set_failure_expression(failure_expression)
    mod._add_function_obj(fn)
    return fn

mod = Module('_genbank')
mod.add_include('"genbank_go.h"')
mod.add_function('GoPyInit', None, [])
mod.add_function('DecRef', None, [param('int64_t', 'handle')])
mod.add_function('IncRef', None, [param('int64_t', 'handle')])
mod.add_function('NumHandles', retval('int'), [])
mod.add_function('Slice_bool_CTor', retval('int64_t'), [])
mod.add_function('Slice_bool_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_bool_elem', retval('bool'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_bool_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_bool_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('bool', 'value')])
mod.add_function('Slice_bool_append', None, [param('int64_t', 'handle'), param('bool', 'value')])
mod.add_function('Slice_byte_CTor', retval('int64_t'), [])
mod.add_function('Slice_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_byte_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_byte_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_byte_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_byte_from_bytes', retval('int64_t'), [param('PyObject*', 'o', transfer_ownership=False)])
mod.add_function('Slice_byte_to_bytes', retval('PyObject*', caller_owns_return=True), [param('int64_t', 'handle')])
mod.add_function('Slice_error_CTor', retval('int64_t'), [])
mod.add_function('Slice_error_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_error_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_error_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_error_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_error_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_float32_CTor', retval('int64_t'), [])
mod.add_function('Slice_float32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float32_elem', retval('float'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('float', 'value')])
mod.add_function('Slice_float32_append', None, [param('int64_t', 'handle'), param('float', 'value')])
mod.add_function('Slice_float64_CTor', retval('int64_t'), [])
mod.add_function('Slice_float64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_float64_elem', retval('double'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_float64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_float64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('double', 'value')])
mod.add_function('Slice_float64_append', None, [param('int64_t', 'handle'), param('double', 'value')])
mod.add_function('Slice_int_CTor', retval('int64_t'), [])
mod.add_function('Slice_int_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int16_CTor', retval('int64_t'), [])
mod.add_function('Slice_int16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int16_elem', retval('int16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int16_t', 'value')])
mod.add_function('Slice_int16_append', None, [param('int64_t', 'handle'), param('int16_t', 'value')])
mod.add_function('Slice_int32_CTor', retval('int64_t'), [])
mod.add_function('Slice_int32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int32_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_int32_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_int64_CTor', retval('int64_t'), [])
mod.add_function('Slice_int64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int64_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_int64_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_int8_CTor', retval('int64_t'), [])
mod.add_function('Slice_int8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_int8_elem', retval('int8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_int8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_int8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int8_t', 'value')])
mod.add_function('Slice_int8_append', None, [param('int64_t', 'handle'), param('int8_t', 'value')])
mod.add_function('Slice_rune_CTor', retval('int64_t'), [])
mod.add_function('Slice_rune_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_rune_elem', retval('int32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_rune_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_rune_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int32_t', 'value')])
mod.add_function('Slice_rune_append', None, [param('int64_t', 'handle'), param('int32_t', 'value')])
mod.add_function('Slice_string_CTor', retval('int64_t'), [])
mod.add_function('Slice_string_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_string_elem', retval('char*'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_string_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_string_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('char*', 'value')])
mod.add_function('Slice_string_append', None, [param('int64_t', 'handle'), param('char*', 'value')])
mod.add_function('Slice_uint_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint16_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint16_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint16_elem', retval('uint16_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint16_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint16_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint16_t', 'value')])
mod.add_function('Slice_uint16_append', None, [param('int64_t', 'handle'), param('uint16_t', 'value')])
mod.add_function('Slice_uint32_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint32_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint32_elem', retval('uint32_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint32_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint32_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint32_t', 'value')])
mod.add_function('Slice_uint32_append', None, [param('int64_t', 'handle'), param('uint32_t', 'value')])
mod.add_function('Slice_uint64_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint64_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint64_elem', retval('uint64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint64_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint64_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint64_t', 'value')])
mod.add_function('Slice_uint64_append', None, [param('int64_t', 'handle'), param('uint64_t', 'value')])
mod.add_function('Slice_uint8_CTor', retval('int64_t'), [])
mod.add_function('Slice_uint8_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_uint8_elem', retval('uint8_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_uint8_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_uint8_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('uint8_t', 'value')])
mod.add_function('Slice_uint8_append', None, [param('int64_t', 'handle'), param('uint8_t', 'value')])
mod.add_function('Slice_genbank_BaseCount_CTor', retval('int64_t'), [])
mod.add_function('Slice_genbank_BaseCount_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_genbank_BaseCount_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_genbank_BaseCount_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_genbank_BaseCount_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_BaseCount_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_Feature_CTor', retval('int64_t'), [])
mod.add_function('Slice_genbank_Feature_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_genbank_Feature_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_genbank_Feature_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_genbank_Feature_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_Feature_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_Genbank_CTor', retval('int64_t'), [])
mod.add_function('Slice_genbank_Genbank_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_genbank_Genbank_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_genbank_Genbank_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_genbank_Genbank_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_Genbank_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_Location_CTor', retval('int64_t'), [])
mod.add_function('Slice_genbank_Location_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_genbank_Location_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_genbank_Location_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_genbank_Location_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_Location_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_Reference_CTor', retval('int64_t'), [])
mod.add_function('Slice_genbank_Reference_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_genbank_Reference_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_genbank_Reference_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_genbank_Reference_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_genbank_Reference_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Map_string_string_CTor', retval('int64_t'), [])
mod.add_function('Map_string_string_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Map_string_string_elem', retval('char*'), [param('int64_t', 'handle'), param('char*', '_ky')])
mod.add_function('Map_string_string_contains', retval('bool'), [param('int64_t', 'handle'), param('char*', '_ky')])
mod.add_function('Map_string_string_set', None, [param('int64_t', 'handle'), param('char*', 'key'), param('char*', 'value')])
mod.add_function('Map_string_string_delete', None, [param('int64_t', 'handle'), param('char*', '_ky')])
mod.add_function('Map_string_string_keys', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Locus_CTor', retval('int64_t'), [])
mod.add_function('genbank_Locus_Name_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Locus_Name_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Locus_SequenceLength_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Locus_SequenceLength_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Locus_MoleculeType_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Locus_MoleculeType_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Locus_GenbankDivision_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Locus_GenbankDivision_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Locus_ModificationDate_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Locus_ModificationDate_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Locus_SequenceCoding_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Locus_SequenceCoding_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Locus_Circular_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('genbank_Locus_Circular_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
mod.add_function('genbank_Meta_CTor', retval('int64_t'), [])
mod.add_function('genbank_Meta_Date_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Date_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_Definition_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Definition_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_Accession_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Accession_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_Version_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Version_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_Keywords_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Keywords_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_Organism_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Organism_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_Source_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Source_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_Taxonomy_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Taxonomy_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Meta_Origin_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Origin_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_Locus_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Locus_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Meta_References_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_References_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Meta_BaseCount_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_BaseCount_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Meta_Other_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Other_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Meta_Name_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_Name_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_SequenceHash_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_SequenceHash_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Meta_SequenceHashFunction_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Meta_SequenceHashFunction_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Reference_CTor', retval('int64_t'), [])
mod.add_function('genbank_Reference_Authors_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Reference_Authors_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Reference_Title_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Reference_Title_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Reference_Journal_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Reference_Journal_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Reference_PubMed_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Reference_PubMed_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Reference_Remark_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Reference_Remark_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Reference_Range_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Reference_Range_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Reference_Consortium_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Reference_Consortium_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_BaseCount_CTor', retval('int64_t'), [])
mod.add_function('genbank_BaseCount_Base_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_BaseCount_Base_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_BaseCount_Count_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_BaseCount_Count_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Feature_CTor', retval('int64_t'), [])
mod.add_function('genbank_Feature_Type_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Feature_Type_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Feature_Description_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Feature_Description_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Feature_Attributes_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Feature_Attributes_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Feature_SequenceHash_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Feature_SequenceHash_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Feature_SequenceHashFunction_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Feature_SequenceHashFunction_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Feature_Sequence_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Feature_Sequence_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Feature_Location_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Feature_Location_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Feature_ParentSequence_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Feature_ParentSequence_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_string_function(mod, 'genbank_Feature_GetSequence', retval('char*'), [param('int64_t', '_handle')])
mod.add_function('genbank_Genbank_CTor', retval('int64_t'), [])
mod.add_function('genbank_Genbank_Meta_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Genbank_Meta_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Genbank_Features_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Genbank_Features_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Genbank_Sequence_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Genbank_Sequence_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
add_checked_function(mod, 'genbank_Genbank_AddFeature', retval('char*'), [param('int64_t', '_handle'), param('int64_t', 'feature')])
mod.add_function('genbank_Location_CTor', retval('int64_t'), [])
mod.add_function('genbank_Location_Start_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Location_Start_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Location_End_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Location_End_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('genbank_Location_Complement_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('genbank_Location_Complement_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
mod.add_function('genbank_Location_Join_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('genbank_Location_Join_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
mod.add_function('genbank_Location_FivePrimePartial_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('genbank_Location_FivePrimePartial_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
mod.add_function('genbank_Location_ThreePrimePartial_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('genbank_Location_ThreePrimePartial_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
mod.add_function('genbank_Location_GbkLocationString_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('genbank_Location_GbkLocationString_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('genbank_Location_SubLocations_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('genbank_Location_SubLocations_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'genbank_Parse', retval('int64_t'), [param('int64_t', 'r')])
add_checked_function(mod, 'genbank_Read', retval('int64_t'), [param('char*', 'path')])
add_checked_function(mod, 'genbank_ReadMultiNth', retval('int64_t'), [param('char*', 'path'), param('int64_t', 'count')])
add_checked_function(mod, 'genbank_Build', retval('int64_t'), [param('int64_t', 'gbk')])
add_checked_function(mod, 'genbank_BuildMulti', retval('int64_t'), [param('int64_t', 'sequences')])
add_checked_function(mod, 'genbank_ParseMulti', retval('int64_t'), [param('int64_t', 'r')])
add_checked_function(mod, 'genbank_ParseMultiNth', retval('int64_t'), [param('int64_t', 'r'), param('int64_t', 'count')])
add_checked_function(mod, 'genbank_ReadMulti', retval('int64_t'), [param('char*', 'path')])
add_checked_function(mod, 'genbank_Write', retval('char*'), [param('int64_t', 'sequences'), param('char*', 'path')])
add_checked_function(mod, 'genbank_WriteMulti', retval('char*'), [param('int64_t', 'sequences'), param('char*', 'path')])
add_checked_string_function(mod, 'genbank_BuildFeatureString', retval('char*'), [param('int64_t', 'feature')])
add_checked_string_function(mod, 'genbank_BuildLocationString', retval('char*'), [param('int64_t', 'location')])

mod.generate(open('genbank.c', 'w'))

