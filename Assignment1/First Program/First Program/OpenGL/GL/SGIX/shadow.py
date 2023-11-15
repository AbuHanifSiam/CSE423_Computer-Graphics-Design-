'''OpenGL extension SGIX.shadow

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.shadow to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines two new operations to be performed on texture
	values before they are passed on to the filtering subsystem.  These
	operations perform either a <= or >= test on the value from texture
	memory and the iterated R value, and return 1.0 or 0.0 if the test
	passes or fails, respectively.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/shadow.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.shadow import *
from OpenGL.raw.GL.SGIX.shadow import _EXTENSION_NAME

def glInitShadowSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION