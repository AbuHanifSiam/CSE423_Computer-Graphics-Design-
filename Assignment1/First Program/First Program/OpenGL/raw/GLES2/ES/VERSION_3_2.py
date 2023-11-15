'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_ES_VERSION_3_2'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_ES_VERSION_3_2',error_checker=_errors._error_checker)
GL_BUFFER=_C('GL_BUFFER',0x82E0)
GL_CCW=_C('GL_CCW',0x0901)
GL_CLAMP_TO_BORDER=_C('GL_CLAMP_TO_BORDER',0x812D)
GL_COLORBURN=_C('GL_COLORBURN',0x929A)
GL_COLORDODGE=_C('GL_COLORDODGE',0x9299)
GL_COMPRESSED_RGBA_ASTC_10x10=_C('GL_COMPRESSED_RGBA_ASTC_10x10',0x93BB)
GL_COMPRESSED_RGBA_ASTC_10x5=_C('GL_COMPRESSED_RGBA_ASTC_10x5',0x93B8)
GL_COMPRESSED_RGBA_ASTC_10x6=_C('GL_COMPRESSED_RGBA_ASTC_10x6',0x93B9)
GL_COMPRESSED_RGBA_ASTC_10x8=_C('GL_COMPRESSED_RGBA_ASTC_10x8',0x93BA)
GL_COMPRESSED_RGBA_ASTC_12x10=_C('GL_COMPRESSED_RGBA_ASTC_12x10',0x93BC)
GL_COMPRESSED_RGBA_ASTC_12x12=_C('GL_COMPRESSED_RGBA_ASTC_12x12',0x93BD)
GL_COMPRESSED_RGBA_ASTC_4x4=_C('GL_COMPRESSED_RGBA_ASTC_4x4',0x93B0)
GL_COMPRESSED_RGBA_ASTC_5x4=_C('GL_COMPRESSED_RGBA_ASTC_5x4',0x93B1)
GL_COMPRESSED_RGBA_ASTC_5x5=_C('GL_COMPRESSED_RGBA_ASTC_5x5',0x93B2)
GL_COMPRESSED_RGBA_ASTC_6x5=_C('GL_COMPRESSED_RGBA_ASTC_6x5',0x93B3)
GL_COMPRESSED_RGBA_ASTC_6x6=_C('GL_COMPRESSED_RGBA_ASTC_6x6',0x93B4)
GL_COMPRESSED_RGBA_ASTC_8x5=_C('GL_COMPRESSED_RGBA_ASTC_8x5',0x93B5)
GL_COMPRESSED_RGBA_ASTC_8x6=_C('GL_COMPRESSED_RGBA_ASTC_8x6',0x93B6)
GL_COMPRESSED_RGBA_ASTC_8x8=_C('GL_COMPRESSED_RGBA_ASTC_8x8',0x93B7)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10',0x93DB)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5',0x93D8)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6',0x93D9)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8',0x93DA)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10',0x93DC)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12',0x93DD)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4',0x93D0)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4',0x93D1)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5',0x93D2)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5',0x93D3)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6',0x93D4)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5',0x93D5)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6',0x93D6)
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8=_C('GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8',0x93D7)
GL_CONTEXT_FLAGS=_C('GL_CONTEXT_FLAGS',0x821E)
GL_CONTEXT_FLAG_DEBUG_BIT=_C('GL_CONTEXT_FLAG_DEBUG_BIT',0x00000002)
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT=_C('GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT',0x00000004)
GL_CONTEXT_LOST=_C('GL_CONTEXT_LOST',0x0507)
GL_CW=_C('GL_CW',0x0900)
GL_DARKEN=_C('GL_DARKEN',0x9297)
GL_DEBUG_CALLBACK_FUNCTION=_C('GL_DEBUG_CALLBACK_FUNCTION',0x8244)
GL_DEBUG_CALLBACK_USER_PARAM=_C('GL_DEBUG_CALLBACK_USER_PARAM',0x8245)
GL_DEBUG_GROUP_STACK_DEPTH=_C('GL_DEBUG_GROUP_STACK_DEPTH',0x826D)
GL_DEBUG_LOGGED_MESSAGES=_C('GL_DEBUG_LOGGED_MESSAGES',0x9145)
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH=_C('GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH',0x8243)
GL_DEBUG_OUTPUT=_C('GL_DEBUG_OUTPUT',0x92E0)
GL_DEBUG_OUTPUT_SYNCHRONOUS=_C('GL_DEBUG_OUTPUT_SYNCHRONOUS',0x8242)
GL_DEBUG_SEVERITY_HIGH=_C('GL_DEBUG_SEVERITY_HIGH',0x9146)
GL_DEBUG_SEVERITY_LOW=_C('GL_DEBUG_SEVERITY_LOW',0x9148)
GL_DEBUG_SEVERITY_MEDIUM=_C('GL_DEBUG_SEVERITY_MEDIUM',0x9147)
GL_DEBUG_SEVERITY_NOTIFICATION=_C('GL_DEBUG_SEVERITY_NOTIFICATION',0x826B)
GL_DEBUG_SOURCE_API=_C('GL_DEBUG_SOURCE_API',0x8246)
GL_DEBUG_SOURCE_APPLICATION=_C('GL_DEBUG_SOURCE_APPLICATION',0x824A)
GL_DEBUG_SOURCE_OTHER=_C('GL_DEBUG_SOURCE_OTHER',0x824B)
GL_DEBUG_SOURCE_SHADER_COMPILER=_C('GL_DEBUG_SOURCE_SHADER_COMPILER',0x8248)
GL_DEBUG_SOURCE_THIRD_PARTY=_C('GL_DEBUG_SOURCE_THIRD_PARTY',0x8249)
GL_DEBUG_SOURCE_WINDOW_SYSTEM=_C('GL_DEBUG_SOURCE_WINDOW_SYSTEM',0x8247)
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR=_C('GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR',0x824D)
GL_DEBUG_TYPE_ERROR=_C('GL_DEBUG_TYPE_ERROR',0x824C)
GL_DEBUG_TYPE_MARKER=_C('GL_DEBUG_TYPE_MARKER',0x8268)
GL_DEBUG_TYPE_OTHER=_C('GL_DEBUG_TYPE_OTHER',0x8251)
GL_DEBUG_TYPE_PERFORMANCE=_C('GL_DEBUG_TYPE_PERFORMANCE',0x8250)
GL_DEBUG_TYPE_POP_GROUP=_C('GL_DEBUG_TYPE_POP_GROUP',0x826A)
GL_DEBUG_TYPE_PORTABILITY=_C('GL_DEBUG_TYPE_PORTABILITY',0x824F)
GL_DEBUG_TYPE_PUSH_GROUP=_C('GL_DEBUG_TYPE_PUSH_GROUP',0x8269)
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR=_C('GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR',0x824E)
GL_DIFFERENCE=_C('GL_DIFFERENCE',0x929E)
GL_EQUAL=_C('GL_EQUAL',0x0202)
GL_EXCLUSION=_C('GL_EXCLUSION',0x92A0)
GL_FIRST_VERTEX_CONVENTION=_C('GL_FIRST_VERTEX_CONVENTION',0x8E4D)
GL_FRACTIONAL_EVEN=_C('GL_FRACTIONAL_EVEN',0x8E7C)
GL_FRACTIONAL_ODD=_C('GL_FRACTIONAL_ODD',0x8E7B)
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS=_C('GL_FRAGMENT_INTERPOLATION_OFFSET_BITS',0x8E5D)
GL_FRAMEBUFFER_ATTACHMENT_LAYERED=_C('GL_FRAMEBUFFER_ATTACHMENT_LAYERED',0x8DA7)
GL_FRAMEBUFFER_DEFAULT_LAYERS=_C('GL_FRAMEBUFFER_DEFAULT_LAYERS',0x9312)
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS=_C('GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS',0x8DA8)
GL_GEOMETRY_INPUT_TYPE=_C('GL_GEOMETRY_INPUT_TYPE',0x8917)
GL_GEOMETRY_OUTPUT_TYPE=_C('GL_GEOMETRY_OUTPUT_TYPE',0x8918)
GL_GEOMETRY_SHADER=_C('GL_GEOMETRY_SHADER',0x8DD9)
GL_GEOMETRY_SHADER_BIT=_C('GL_GEOMETRY_SHADER_BIT',0x00000004)
GL_GEOMETRY_SHADER_INVOCATIONS=_C('GL_GEOMETRY_SHADER_INVOCATIONS',0x887F)
GL_GEOMETRY_VERTICES_OUT=_C('GL_GEOMETRY_VERTICES_OUT',0x8916)
GL_GUILTY_CONTEXT_RESET=_C('GL_GUILTY_CONTEXT_RESET',0x8253)
GL_HARDLIGHT=_C('GL_HARDLIGHT',0x929B)
GL_HSL_COLOR=_C('GL_HSL_COLOR',0x92AF)
GL_HSL_HUE=_C('GL_HSL_HUE',0x92AD)
GL_HSL_LUMINOSITY=_C('GL_HSL_LUMINOSITY',0x92B0)
GL_HSL_SATURATION=_C('GL_HSL_SATURATION',0x92AE)
GL_IMAGE_BUFFER=_C('GL_IMAGE_BUFFER',0x9051)
GL_IMAGE_CUBE_MAP_ARRAY=_C('GL_IMAGE_CUBE_MAP_ARRAY',0x9054)
GL_INNOCENT_CONTEXT_RESET=_C('GL_INNOCENT_CONTEXT_RESET',0x8254)
GL_INT_IMAGE_BUFFER=_C('GL_INT_IMAGE_BUFFER',0x905C)
GL_INT_IMAGE_CUBE_MAP_ARRAY=_C('GL_INT_IMAGE_CUBE_MAP_ARRAY',0x905F)
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY=_C('GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY',0x910C)
GL_INT_SAMPLER_BUFFER=_C('GL_INT_SAMPLER_BUFFER',0x8DD0)
GL_INT_SAMPLER_CUBE_MAP_ARRAY=_C('GL_INT_SAMPLER_CUBE_MAP_ARRAY',0x900E)
GL_ISOLINES=_C('GL_ISOLINES',0x8E7A)
GL_IS_PER_PATCH=_C('GL_IS_PER_PATCH',0x92E7)
GL_LAST_VERTEX_CONVENTION=_C('GL_LAST_VERTEX_CONVENTION',0x8E4E)
GL_LAYER_PROVOKING_VERTEX=_C('GL_LAYER_PROVOKING_VERTEX',0x825E)
GL_LIGHTEN=_C('GL_LIGHTEN',0x9298)
GL_LINES_ADJACENCY=_C('GL_LINES_ADJACENCY',0x000A)
GL_LINE_STRIP_ADJACENCY=_C('GL_LINE_STRIP_ADJACENCY',0x000B)
GL_LOSE_CONTEXT_ON_RESET=_C('GL_LOSE_CONTEXT_ON_RESET',0x8252)
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS',0x8A32)
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS',0x8E1E)
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS=_C('GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS',0x8E1F)
GL_MAX_DEBUG_GROUP_STACK_DEPTH=_C('GL_MAX_DEBUG_GROUP_STACK_DEPTH',0x826C)
GL_MAX_DEBUG_LOGGED_MESSAGES=_C('GL_MAX_DEBUG_LOGGED_MESSAGES',0x9144)
GL_MAX_DEBUG_MESSAGE_LENGTH=_C('GL_MAX_DEBUG_MESSAGE_LENGTH',0x9143)
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET=_C('GL_MAX_FRAGMENT_INTERPOLATION_OFFSET',0x8E5C)
GL_MAX_FRAMEBUFFER_LAYERS=_C('GL_MAX_FRAMEBUFFER_LAYERS',0x9317)
GL_MAX_GEOMETRY_ATOMIC_COUNTERS=_C('GL_MAX_GEOMETRY_ATOMIC_COUNTERS',0x92D5)
GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS',0x92CF)
GL_MAX_GEOMETRY_IMAGE_UNIFORMS=_C('GL_MAX_GEOMETRY_IMAGE_UNIFORMS',0x90CD)
GL_MAX_GEOMETRY_INPUT_COMPONENTS=_C('GL_MAX_GEOMETRY_INPUT_COMPONENTS',0x9123)
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS=_C('GL_MAX_GEOMETRY_OUTPUT_COMPONENTS',0x9124)
GL_MAX_GEOMETRY_OUTPUT_VERTICES=_C('GL_MAX_GEOMETRY_OUTPUT_VERTICES',0x8DE0)
GL_MAX_GEOMETRY_SHADER_INVOCATIONS=_C('GL_MAX_GEOMETRY_SHADER_INVOCATIONS',0x8E5A)
GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS=_C('GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS',0x90D7)
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS=_C('GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS',0x8C29)
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS=_C('GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS',0x8DE1)
GL_MAX_GEOMETRY_UNIFORM_BLOCKS=_C('GL_MAX_GEOMETRY_UNIFORM_BLOCKS',0x8A2C)
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS=_C('GL_MAX_GEOMETRY_UNIFORM_COMPONENTS',0x8DDF)
GL_MAX_LABEL_LENGTH=_C('GL_MAX_LABEL_LENGTH',0x82E8)
GL_MAX_PATCH_VERTICES=_C('GL_MAX_PATCH_VERTICES',0x8E7D)
GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS=_C('GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS',0x92D3)
GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS',0x92CD)
GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS=_C('GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS',0x90CB)
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_INPUT_COMPONENTS',0x886C)
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS',0x8E83)
GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS=_C('GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS',0x90D8)
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS=_C('GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS',0x8E81)
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS',0x8E85)
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS=_C('GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS',0x8E89)
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS=_C('GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS',0x8E7F)
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS=_C('GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS',0x92D4)
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS=_C('GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS',0x92CE)
GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS=_C('GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS',0x90CC)
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS',0x886D)
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS',0x8E86)
GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS=_C('GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS',0x90D9)
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS=_C('GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS',0x8E82)
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS=_C('GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS',0x8E8A)
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS=_C('GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS',0x8E80)
GL_MAX_TESS_GEN_LEVEL=_C('GL_MAX_TESS_GEN_LEVEL',0x8E7E)
GL_MAX_TESS_PATCH_COMPONENTS=_C('GL_MAX_TESS_PATCH_COMPONENTS',0x8E84)
GL_MAX_TEXTURE_BUFFER_SIZE=_C('GL_MAX_TEXTURE_BUFFER_SIZE',0x8C2B)
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET=_C('GL_MIN_FRAGMENT_INTERPOLATION_OFFSET',0x8E5B)
GL_MIN_SAMPLE_SHADING_VALUE=_C('GL_MIN_SAMPLE_SHADING_VALUE',0x8C37)
GL_MULTIPLY=_C('GL_MULTIPLY',0x9294)
GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY=_C('GL_MULTISAMPLE_LINE_WIDTH_GRANULARITY',0x9382)
GL_MULTISAMPLE_LINE_WIDTH_RANGE=_C('GL_MULTISAMPLE_LINE_WIDTH_RANGE',0x9381)
GL_NO_ERROR=_C('GL_NO_ERROR',0)
GL_NO_RESET_NOTIFICATION=_C('GL_NO_RESET_NOTIFICATION',0x8261)
GL_OVERLAY=_C('GL_OVERLAY',0x9296)
GL_PATCHES=_C('GL_PATCHES',0x000E)
GL_PATCH_VERTICES=_C('GL_PATCH_VERTICES',0x8E72)
GL_PRIMITIVES_GENERATED=_C('GL_PRIMITIVES_GENERATED',0x8C87)
GL_PRIMITIVE_BOUNDING_BOX=_C('GL_PRIMITIVE_BOUNDING_BOX',0x92BE)
GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED=_C('GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED',0x8221)
GL_PROGRAM=_C('GL_PROGRAM',0x82E2)
GL_PROGRAM_PIPELINE=_C('GL_PROGRAM_PIPELINE',0x82E4)
GL_QUADS=_C('GL_QUADS',0x0007)
GL_QUERY=_C('GL_QUERY',0x82E3)
GL_REFERENCED_BY_GEOMETRY_SHADER=_C('GL_REFERENCED_BY_GEOMETRY_SHADER',0x9309)
GL_REFERENCED_BY_TESS_CONTROL_SHADER=_C('GL_REFERENCED_BY_TESS_CONTROL_SHADER',0x9307)
GL_REFERENCED_BY_TESS_EVALUATION_SHADER=_C('GL_REFERENCED_BY_TESS_EVALUATION_SHADER',0x9308)
GL_RESET_NOTIFICATION_STRATEGY=_C('GL_RESET_NOTIFICATION_STRATEGY',0x8256)
GL_SAMPLER=_C('GL_SAMPLER',0x82E6)
GL_SAMPLER_2D_MULTISAMPLE_ARRAY=_C('GL_SAMPLER_2D_MULTISAMPLE_ARRAY',0x910B)
GL_SAMPLER_BUFFER=_C('GL_SAMPLER_BUFFER',0x8DC2)
GL_SAMPLER_CUBE_MAP_ARRAY=_C('GL_SAMPLER_CUBE_MAP_ARRAY',0x900C)
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW=_C('GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW',0x900D)
GL_SAMPLE_SHADING=_C('GL_SAMPLE_SHADING',0x8C36)
GL_SCREEN=_C('GL_SCREEN',0x9295)
GL_SHADER=_C('GL_SHADER',0x82E1)
GL_SOFTLIGHT=_C('GL_SOFTLIGHT',0x929C)
GL_STACK_OVERFLOW=_C('GL_STACK_OVERFLOW',0x0503)
GL_STACK_UNDERFLOW=_C('GL_STACK_UNDERFLOW',0x0504)
GL_STENCIL_INDEX=_C('GL_STENCIL_INDEX',0x1901)
GL_STENCIL_INDEX8=_C('GL_STENCIL_INDEX8',0x8D48)
GL_TESS_CONTROL_OUTPUT_VERTICES=_C('GL_TESS_CONTROL_OUTPUT_VERTICES',0x8E75)
GL_TESS_CONTROL_SHADER=_C('GL_TESS_CONTROL_SHADER',0x8E88)
GL_TESS_CONTROL_SHADER_BIT=_C('GL_TESS_CONTROL_SHADER_BIT',0x00000008)
GL_TESS_EVALUATION_SHADER=_C('GL_TESS_EVALUATION_SHADER',0x8E87)
GL_TESS_EVALUATION_SHADER_BIT=_C('GL_TESS_EVALUATION_SHADER_BIT',0x00000010)
GL_TESS_GEN_MODE=_C('GL_TESS_GEN_MODE',0x8E76)
GL_TESS_GEN_POINT_MODE=_C('GL_TESS_GEN_POINT_MODE',0x8E79)
GL_TESS_GEN_SPACING=_C('GL_TESS_GEN_SPACING',0x8E77)
GL_TESS_GEN_VERTEX_ORDER=_C('GL_TESS_GEN_VERTEX_ORDER',0x8E78)
GL_TEXTURE_2D_MULTISAMPLE_ARRAY=_C('GL_TEXTURE_2D_MULTISAMPLE_ARRAY',0x9102)
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY=_C('GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY',0x9105)
GL_TEXTURE_BINDING_BUFFER=_C('GL_TEXTURE_BINDING_BUFFER',0x8C2C)
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY=_C('GL_TEXTURE_BINDING_CUBE_MAP_ARRAY',0x900A)
GL_TEXTURE_BORDER_COLOR=_C('GL_TEXTURE_BORDER_COLOR',0x1004)
GL_TEXTURE_BUFFER=_C('GL_TEXTURE_BUFFER',0x8C2A)
GL_TEXTURE_BUFFER_BINDING=_C('GL_TEXTURE_BUFFER_BINDING',0x8C2A)
GL_TEXTURE_BUFFER_DATA_STORE_BINDING=_C('GL_TEXTURE_BUFFER_DATA_STORE_BINDING',0x8C2D)
GL_TEXTURE_BUFFER_OFFSET=_C('GL_TEXTURE_BUFFER_OFFSET',0x919D)
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT=_C('GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT',0x919F)
GL_TEXTURE_BUFFER_SIZE=_C('GL_TEXTURE_BUFFER_SIZE',0x919E)
GL_TEXTURE_CUBE_MAP_ARRAY=_C('GL_TEXTURE_CUBE_MAP_ARRAY',0x9009)
GL_TRIANGLES=_C('GL_TRIANGLES',0x0004)
GL_TRIANGLES_ADJACENCY=_C('GL_TRIANGLES_ADJACENCY',0x000C)
GL_TRIANGLE_STRIP_ADJACENCY=_C('GL_TRIANGLE_STRIP_ADJACENCY',0x000D)
GL_UNDEFINED_VERTEX=_C('GL_UNDEFINED_VERTEX',0x8260)
GL_UNKNOWN_CONTEXT_RESET=_C('GL_UNKNOWN_CONTEXT_RESET',0x8255)
GL_UNSIGNED_INT_IMAGE_BUFFER=_C('GL_UNSIGNED_INT_IMAGE_BUFFER',0x9067)
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY=_C('GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY',0x906A)
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY=_C('GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY',0x910D)
GL_UNSIGNED_INT_SAMPLER_BUFFER=_C('GL_UNSIGNED_INT_SAMPLER_BUFFER',0x8DD8)
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY=_C('GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY',0x900F)
GL_VERTEX_ARRAY=_C('GL_VERTEX_ARRAY',0x8074)
@_f
@_p.types(None,)
def glBlendBarrier():pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBlendEquationSeparatei(buf,modeRGB,modeAlpha):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum)
def glBlendEquationi(buf,mode):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glBlendFuncSeparatei(buf,srcRGB,dstRGB,srcAlpha,dstAlpha):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum)
def glBlendFunci(buf,src,dst):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean,_cs.GLboolean)
def glColorMaski(index,r,g,b,a):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLuint,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei)
def glCopyImageSubData(srcName,srcTarget,srcLevel,srcX,srcY,srcZ,dstName,dstTarget,dstLevel,dstX,dstY,dstZ,srcWidth,srcHeight,srcDepth):pass
@_f
@_p.types(None,_cs.GLDEBUGPROC,ctypes.c_void_p)
def glDebugMessageCallback(callback,userParam):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray,_cs.GLboolean)
def glDebugMessageControl(source,type,severity,count,ids,enabled):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLenum,_cs.GLsizei,arrays.GLcharArray)
def glDebugMessageInsert(source,type,id,severity,length,buf):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDisablei(target,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glDrawElementsBaseVertex(mode,count,type,indices,basevertex):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei,_cs.GLint)
def glDrawElementsInstancedBaseVertex(mode,count,type,indices,instancecount,basevertex):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glDrawRangeElementsBaseVertex(mode,start,end,count,type,indices,basevertex):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glEnablei(target,index):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint)
def glFramebufferTexture(target,attachment,texture,level):pass
@_f
@_p.types(_cs.GLuint,_cs.GLuint,_cs.GLsizei,arrays.GLuintArray,arrays.GLuintArray,arrays.GLuintArray,arrays.GLuintArray,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetDebugMessageLog(count,bufSize,sources,types,ids,severities,lengths,messageLog):pass
@_f
@_p.types(_cs.GLenum,)
def glGetGraphicsResetStatus():pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetObjectLabel(identifier,name,bufSize,length,label):pass
@_f
@_p.types(None,ctypes.c_void_p,_cs.GLsizei,arrays.GLsizeiArray,arrays.GLcharArray)
def glGetObjectPtrLabel(ptr,bufSize,length,label):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLvoidpArray)
def glGetPointerv(pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetSamplerParameterIiv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetSamplerParameterIuiv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetTexParameterIiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glGetTexParameterIuiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLfloatArray)
def glGetnUniformfv(program,location,bufSize,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLintArray)
def glGetnUniformiv(program,location,bufSize,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuintArray)
def glGetnUniformuiv(program,location,bufSize,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLenum,_cs.GLuint)
def glIsEnabledi(target,index):pass
@_f
@_p.types(None,_cs.GLfloat)
def glMinSampleShading(value):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLcharArray)
def glObjectLabel(identifier,name,length,label):pass
@_f
@_p.types(None,ctypes.c_void_p,_cs.GLsizei,arrays.GLcharArray)
def glObjectPtrLabel(ptr,length,label):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPatchParameteri(pname,value):pass
@_f
@_p.types(None,)
def glPopDebugGroup():pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glPrimitiveBoundingBox(minX,minY,minZ,minW,maxX,maxY,maxZ,maxW):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei,arrays.GLcharArray)
def glPushDebugGroup(source,id,length,message):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLenum,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glReadnPixels(x,y,width,height,format,type,bufSize,data):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glSamplerParameterIiv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glSamplerParameterIuiv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint)
def glTexBuffer(target,internalformat,buffer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLintptr,_cs.GLsizeiptr)
def glTexBufferRange(target,internalformat,buffer,offset,size):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glTexParameterIiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLuintArray)
def glTexParameterIuiv(target,pname,params):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTexStorage3DMultisample(target,samples,internalformat,width,height,depth,fixedsamplelocations):pass