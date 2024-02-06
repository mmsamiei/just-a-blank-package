import numpy as np 

def return_hello(name):
    return 'hello ' + name + '!'

def random_tensor(shape):
    """
    Generate a random numpy tensor with given shape.

    Parameters:
    shape (tuple): The shape of the tensor.

    Returns:
    numpy.ndarray: A random tensor with the specified shape.
    """
    return np.random.random(shape)
