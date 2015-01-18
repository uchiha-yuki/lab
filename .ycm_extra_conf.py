# This file is NOT licensed under the GPLv3, which is the license for the rest
# of YouCompleteMe.
#
# Here's the license text for this file:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

import os
import ycm_core

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
flags = [
'-Wall',
'-Wextra',
'-Werror',
# '-Wc++98-compat',
'-Wno-long-long',
'-Wno-variadic-macros',
'-fexceptions',
'-DNDEBUG',
# You 100% do NOT need -DUSE_CLANG_COMPLETER in your flags; only the YCM
# source code needs it.
# '-DUSE_CLANG_COMPLETER',
# THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
# language to use when compiling headers. So it will guess. Badly. So C++
# headers will be compiled as C headers. You don't want that so ALWAYS specify
# a "-std=<something>".
# For a C project, you would set this to something like 'c99' instead of
# 'c++11'.
'-std=c++11',
# ...and the same thing goes for the magic -x option which specifies the
# language that the files to be compiled are written in. This is mostly
# relevant for c++ headers.
# For a C project, you would set this to 'c' instead of 'c++'.
'-x',
'c++',
# '-isystem',
# '../BoostParts',
# '-isystem',
# This path will only work on OS X, but extra paths that don't exist are not
# harmful
# '/System/Library/Frameworks/Python.framework/Headers',
# '-isystem',
# '../llvm/include',
# '-isystem',
# '../llvm/tools/clang/include',
'-I',
'./src',
'-I',
'./build/src',
# '-I',
# './ClangCompleter',
# '-isystem',
# './tests/gmock/gtest',
# '-isystem',
# './tests/gmock/gtest/include',
# '-isystem',
# './tests/gmock',
# '-isystem',
# './tests/gmock/include',
# '-isystem',
# '/usr/include',
# '-isystem',
# '/usr/local/include',
# '-isystem',
# '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1',
# '-isystem',
# '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include',
'./src/caffe/common.cpp',
'./src/caffe/util/upgrade_proto.cpp',
'./src/caffe/util/io.cpp',
'./src/caffe/util/benchmark.cpp',
'./src/caffe/util/insert_splits.cpp',
'./src/caffe/util/math_functions.cpp',
'./src/caffe/util/im2col.cpp',
'./src/caffe/layer_factory.cpp',
'./src/caffe/test/test_common.cpp',
'./src/caffe/test/test_threshold_layer.cpp',
'./src/caffe/test/test_softmax_layer.cpp',
'./src/caffe/test/test_power_layer.cpp',
'./src/caffe/test/test_internal_thread.cpp',
'./src/caffe/test/test_concat_layer.cpp',
'./src/caffe/test/test_data_layer.cpp',
'./src/caffe/test/test_argmax_layer.cpp',
'./src/caffe/test/test_flatten_layer.cpp',
'./src/caffe/test/test_upgrade_proto.cpp',
'./src/caffe/test/test_lrn_layer.cpp',
'./src/caffe/test/test_stochastic_pooling.cpp',
'./src/caffe/test/test_infogain_loss_layer.cpp',
'./src/caffe/test/test_neuron_layer.cpp',
'./src/caffe/test/test_memory_data_layer.cpp',
'./src/caffe/test/test_mvn_layer.cpp',
'./src/caffe/test/test_caffe_main.cpp',
'./src/caffe/test/test_contrastive_loss_layer.cpp',
'./src/caffe/test/test_net.cpp',
'./src/caffe/test/test_blob.cpp',
'./src/caffe/test/test_filler.cpp',
'./src/caffe/test/test_inner_product_layer.cpp',
'./src/caffe/test/test_image_data_layer.cpp',
'./src/caffe/test/test_dummy_data_layer.cpp',
'./src/caffe/test/test_hdf5_output_layer.cpp',
'./src/caffe/test/test_random_number_generator.cpp',
'./src/caffe/test/test_multinomial_logistic_loss_layer.cpp',
'./src/caffe/test/test_util_blas.cpp',
'./src/caffe/test/test_gradient_based_solver.cpp',
'./src/caffe/test/test_slice_layer.cpp',
'./src/caffe/test/test_sigmoid_cross_entropy_loss_layer.cpp',
'./src/caffe/test/test_platform.cpp',
'./src/caffe/test/test_softmax_with_loss_layer.cpp',
'./src/caffe/test/test_im2col_layer.cpp',
'./src/caffe/test/test_convolution_layer.cpp',
'./src/caffe/test/test_hdf5data_layer.cpp',
'./src/caffe/test/test_accuracy_layer.cpp',
'./src/caffe/test/test_hinge_loss_layer.cpp',
'./src/caffe/test/test_euclidean_loss_layer.cpp',
'./src/caffe/test/test_solver.cpp',
'./src/caffe/test/test_math_functions.cpp',
'./src/caffe/test/test_split_layer.cpp',
'./src/caffe/test/test_benchmark.cpp',
'./src/caffe/test/test_eltwise_layer.cpp',
'./src/caffe/test/test_maxpool_dropout_layers.cpp',
'./src/caffe/test/test_pooling_layer.cpp',
'./src/caffe/test/test_syncedmem.cpp',
'./src/caffe/test/test_protobuf.cpp',
'./src/caffe/syncedmem.cpp',
'./src/caffe/internal_thread.cpp',
'./src/caffe/layers/slice_layer.cpp',
'./src/caffe/layers/data_layer.cpp',
'./src/caffe/layers/split_layer.cpp',
'./src/caffe/layers/eltwise_layer.cpp',
'./src/caffe/layers/dummy_data_layer.cpp',
'./src/caffe/layers/concat_layer.cpp',
'./src/caffe/layers/softmax_layer.cpp',
'./src/caffe/layers/cudnn_conv_layer.cpp',
'./src/caffe/layers/lrn_layer.cpp',
'./src/caffe/layers/image_data_layer.cpp',
'./src/caffe/layers/argmax_layer.cpp',
'./src/caffe/layers/threshold_layer.cpp',
'./src/caffe/layers/dropout_layer.cpp',
'./src/caffe/layers/sigmoid_cross_entropy_loss_layer.cpp',
'./src/caffe/layers/pooling_layer.cpp',
'./src/caffe/layers/accuracy_layer.cpp',
'./src/caffe/layers/window_data_layer.cpp',
'./src/caffe/layers/mvn_layer.cpp',
'./src/caffe/layers/sigmoid_layer.cpp',
'./src/caffe/layers/im2col_layer.cpp',
'./src/caffe/layers/cudnn_sigmoid_layer.cpp',
'./src/caffe/layers/euclidean_loss_layer.cpp',
'./src/caffe/layers/inner_product_layer.cpp',
'./src/caffe/layers/neuron_layer.cpp',
'./src/caffe/layers/bnll_layer.cpp',
'./src/caffe/layers/cudnn_tanh_layer.cpp',
'./src/caffe/layers/tanh_layer.cpp',
'./src/caffe/layers/relu_layer.cpp',
'./src/caffe/layers/memory_data_layer.cpp',
'./src/caffe/layers/hdf5_data_layer.cpp',
'./src/caffe/layers/infogain_loss_layer.cpp',
'./src/caffe/layers/flatten_layer.cpp',
'./src/caffe/layers/hinge_loss_layer.cpp',
'./src/caffe/layers/cudnn_softmax_layer.cpp',
'./src/caffe/layers/cudnn_relu_layer.cpp',
'./src/caffe/layers/multinomial_logistic_loss_layer.cpp',
'./src/caffe/layers/softmax_loss_layer.cpp',
'./src/caffe/layers/contrastive_loss_layer.cpp',
'./src/caffe/layers/conv_layer.cpp',
'./src/caffe/layers/hdf5_output_layer.cpp',
'./src/caffe/layers/absval_layer.cpp',
'./src/caffe/layers/base_data_layer.cpp',
'./src/caffe/layers/silence_layer.cpp',
'./src/caffe/layers/loss_layer.cpp',
'./src/caffe/layers/cudnn_pooling_layer.cpp',
'./src/caffe/layers/power_layer.cpp',
'./src/caffe/data_transformer.cpp',
'./src/caffe/net.cpp',
'./src/caffe/blob.cpp',
'./src/caffe/solver.cpp',
'./src/gtest/gtest-all.cpp',
'./tools/convert_imageset.cpp',
'./tools/dump_network.cpp',
'./tools/test_net.cpp',
'./tools/compute_image_mean.cpp',
'./tools/device_query.cpp',
'./tools/caffe.cpp',
'./tools/upgrade_net_proto_text.cpp',
'./tools/train_net.cpp',
'./tools/net_speed_benchmark.cpp',
'./tools/finetune_net.cpp',
'./tools/extract_features.cpp',
'./tools/upgrade_net_proto_binary.cpp',
'./build/src/caffe/proto/caffe.pb.cc',
'./build/src/caffe/proto/caffe_pretty_print.pb.cc',]


# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# You can get CMake to generate this file for you by adding:
#   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
# to your CMakeLists.txt file.
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags. Notice that YCM itself uses that approach.
compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )


def FlagsForFile( filename, **kwargs ):
  if database:
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

    # NOTE: This is just for YouCompleteMe; it's highly likely that your project
    # does NOT need to remove the stdlib flag. DO NOT USE THIS IN YOUR
    # ycm_extra_conf IF YOU'RE NOT 100% SURE YOU NEED IT.
    # try:
    #   final_flags.remove( '-stdlib=libc++' )
    # except ValueError:
    #   pass
  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
