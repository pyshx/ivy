# global
import tensorflow as tf
from tensorflow.python.types.core import Tensor
import typing

# local
import ivy


def bitwise_and(x1: Tensor,
                x2: Tensor)\
        -> Tensor:
    return tf.bitwise.bitwise_and(x1, x2)


def ceil(x: Tensor)\
        -> Tensor:
    if 'int' in str(x.dtype):
        return x
    return tf.math.ceil(x)


def isfinite(x: Tensor) \
        -> Tensor:
    if ivy.is_int_dtype(x):
        return tf.ones_like(x, tf.bool)
    return tf.math.is_finite(x)


def _tf_cast(x: Tensor, dtype: tf.dtypes.DType) -> Tensor:
    try:
        return tf.cast(x, dtype)
    except ValueError:
        return x


def _cast_for_binary_op(x1: Tensor, x2: Tensor)\
        -> typing.Tuple[typing.Union[Tensor, int, float, bool], typing.Union[Tensor, int, float, bool]]:
    x1_bits = ivy.functional.backends.tensorflow.core.general.dtype_bits(x1.dtype)
    if isinstance(x2, (int, float, bool)):
        return x1, x2
    x2_bits = ivy.functional.backends.tensorflow.core.general.dtype_bits(x2.dtype)
    if x1_bits > x2_bits:
        x2 = _tf_cast(x2, x1.dtype)
    elif x2_bits > x1_bits:
        x1 = _tf_cast(x1, x2.dtype)
    return x1, x2


def equal(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.math.equal(x1, x2)


def less_equal(x1: Tensor, x2: Tensor)\
        -> Tensor:
    x1, x2 = _cast_for_binary_op(x1, x2)
    return tf.math.less_equal(x1, x2)


def asinh(x: Tensor) \
        -> Tensor:
    return tf.asinh(x)


def sqrt(x: Tensor)\
        -> Tensor:
    if x.dtype == 'float32':
        x_64 = tf.cast(x, tf.float64)
        return tf.cast(tf.sqrt(x_64), x.dtype)
    return  tf.math.sqrt(x)



def cosh(x: Tensor) \
        -> Tensor:
    return tf.cosh(x)


def log2(x: Tensor) \
        -> Tensor:
    return tf.experimental.numpy.log2(x)


def log1p(x: Tensor) \
        -> Tensor:
    return tf.experimental.numpy.log1p(x)


def isnan(x: Tensor)\
        -> Tensor:
    if ivy.is_int_dtype(x):
        return tf.zeros_like(x, tf.bool)
    return tf.math.is_nan(x)


def less(x1: Tensor, x2: Tensor)\
        -> Tensor:
    if hasattr(x1, 'dtype') and hasattr(x2, 'dtype'):
        promoted_type = tf.experimental.numpy.promote_types(x1.dtype, x2.dtype)
        x1 = tf.cast(x1, promoted_type)
        x2 = tf.cast(x2, promoted_type)
    return tf.math.less(x1, x2)


def cos(x: Tensor)\
        -> Tensor:
    return tf.cos(x)


def logical_not(x: Tensor)\
        -> Tensor:
    return tf.logical_not(tf.cast(x, tf.bool))


def acosh(x: Tensor) \
        -> Tensor:
    return tf.acosh(x)

  
def sin(x: Tensor)\
        -> Tensor:
    return tf.sin(x)


def negative(x: Tensor) -> Tensor:
    if x.dtype in [tf.uint8, tf.uint16, tf.uint32, tf.uint64]:
        return tf.cast(tf.negative(tf.cast(x, tf.float32)), x.dtype)
    return tf.negative(x)
