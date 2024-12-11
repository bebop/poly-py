# python build stubs for package clone
# File is generated by gopy. Do not edit.
# gopy build -output=poly/clone -vm=python3 github.com/bebop/poly/clone

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

mod = Module('_clone')
mod.add_include('"clone_go.h"')
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
mod.add_function('Slice_Slice_Slice_byte_CTor', retval('int64_t'), [])
mod.add_function('Slice_Slice_Slice_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Slice_Slice_byte_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Slice_Slice_byte_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_Slice_Slice_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Slice_Slice_byte_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_Slice_byte_CTor', retval('int64_t'), [])
mod.add_function('Slice_Slice_byte_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Slice_byte_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Slice_byte_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_Slice_byte_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Slice_byte_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_Slice_int_CTor', retval('int64_t'), [])
mod.add_function('Slice_Slice_int_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Slice_int_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Slice_int_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_Slice_int_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Slice_int_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_Slice_string_CTor', retval('int64_t'), [])
mod.add_function('Slice_Slice_string_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_Slice_string_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_Slice_string_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_Slice_string_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_Slice_string_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_clone_Enzyme_CTor', retval('int64_t'), [])
mod.add_function('Slice_clone_Enzyme_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_clone_Enzyme_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_clone_Enzyme_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_clone_Enzyme_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_clone_Enzyme_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('Slice_clone_Fragment_CTor', retval('int64_t'), [])
mod.add_function('Slice_clone_Fragment_len', retval('int'), [param('int64_t', 'handle')])
mod.add_function('Slice_clone_Fragment_elem', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'idx')])
mod.add_function('Slice_clone_Fragment_subslice', retval('int64_t'), [param('int64_t', 'handle'), param('int', 'st'), param('int', 'ed')])
mod.add_function('Slice_clone_Fragment_set', None, [param('int64_t', 'handle'), param('int', 'idx'), param('int64_t', 'value')])
mod.add_function('Slice_clone_Fragment_append', None, [param('int64_t', 'handle'), param('int64_t', 'value')])
mod.add_function('clone_Part_CTor', retval('int64_t'), [])
mod.add_function('clone_Part_Sequence_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('clone_Part_Sequence_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('clone_Part_Circular_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('clone_Part_Circular_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
mod.add_function('clone_Enzyme_CTor', retval('int64_t'), [])
mod.add_function('clone_Enzyme_Name_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('clone_Enzyme_Name_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('clone_Enzyme_RegexpFor_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('clone_Enzyme_RegexpFor_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('clone_Enzyme_RegexpRev_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('clone_Enzyme_RegexpRev_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('clone_Enzyme_Skip_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('clone_Enzyme_Skip_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('clone_Enzyme_OverheadLength_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('clone_Enzyme_OverheadLength_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('clone_Enzyme_RecognitionSite_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('clone_Enzyme_RecognitionSite_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('clone_EnzymeManager_CTor', retval('int64_t'), [])
add_checked_function(mod, 'clone_EnzymeManager_CutWithEnzymeByName', retval('int64_t'), [param('int64_t', '_handle'), param('int64_t', 'part'), param('bool', 'directional'), param('char*', 'name')])
add_checked_function(mod, 'clone_EnzymeManager_GetEnzymeByName', retval('int64_t'), [param('int64_t', '_handle'), param('char*', 'name')])
mod.add_function('clone_Fragment_CTor', retval('int64_t'), [])
mod.add_function('clone_Fragment_Sequence_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('clone_Fragment_Sequence_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('clone_Fragment_ForwardOverhang_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('clone_Fragment_ForwardOverhang_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('clone_Fragment_ReverseOverhang_Get', retval('char*'), [param('int64_t', 'handle')])
mod.add_function('clone_Fragment_ReverseOverhang_Set', None, [param('int64_t', 'handle'), param('char*', 'val')])
mod.add_function('clone_Overhang_CTor', retval('int64_t'), [])
mod.add_function('clone_Overhang_Length_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('clone_Overhang_Length_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('clone_Overhang_Position_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('clone_Overhang_Position_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
mod.add_function('clone_Overhang_Forward_Get', retval('bool'), [param('int64_t', 'handle')])
mod.add_function('clone_Overhang_Forward_Set', None, [param('int64_t', 'handle'), param('bool', 'val')])
mod.add_function('clone_Overhang_RecognitionSitePlusSkipLength_Get', retval('int64_t'), [param('int64_t', 'handle')])
mod.add_function('clone_Overhang_RecognitionSitePlusSkipLength_Set', None, [param('int64_t', 'handle'), param('int64_t', 'val')])
add_checked_function(mod, 'clone_NewEnzymeManager', retval('int64_t'), [param('int64_t', 'enzymes')])
add_checked_function(mod, 'clone_GetBaseRestrictionEnzymes', retval('int64_t'), [])
add_checked_function(mod, 'clone_CutWithEnzyme', retval('int64_t'), [param('int64_t', 'part'), param('bool', 'directional'), param('int64_t', 'enzyme')])

mod.generate(open('clone.c', 'w'))

