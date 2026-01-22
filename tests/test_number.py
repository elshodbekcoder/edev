
from edev import is_prime, prime_factors, prime_divisor_count

def test_is_prime():
    assert is_prime(2)
    assert is_prime(13)
    assert not is_prime(1)
    assert not is_prime(15)

def test_prime_factors():
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(7) == [7]

def test_prime_divisor_count():
    assert prime_divisor_count(1) == 0
    assert prime_divisor_count(12) == 2
    assert prime_divisor_count(60) == 3
