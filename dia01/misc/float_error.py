numero = f"{0.1:.10f}"
# Output: '0.1000000000'

numero = f"{0.1:.20f}"
# Output: '0.10000000000000000555'
# This is the true decimal value of the binary approximation stored for 0.1

# There are many different decimal numbers that share the same approximate binary representation.
# This is why it is important to be careful when comparing floating point numbers.

0.1 + 0.1 + 0.1 == 0.3
# Output: False.


# pylint: disable=all