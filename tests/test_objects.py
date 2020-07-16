from pygeo.objects import Point, Vector

# Point.__eq__
def test__point_equal__given_two_equal_points__return_true():
    assert (Point((1, 2, 3)) == Point((1, 2, 3))) is True


def test__point_equal__given_two_not_equal_points__return_false():
    assert (Point((1, 2, 3)) == Point((4, 5, 6))) is False


# Vector.__eq__
def test__vector_equal__given_two_equal_vectors__return_true():
    assert (Vector((1, 2, 3)) == Vector((1, 2, 3))) is True


def test__vector_equal__given_two_not_equal_vectors__return_false():
    assert (Vector((1, 2, 3)) == Vector((4, 5, 6))) is False


# Point.__add__
def test__point_addition__given_point_and_vector__return_correct_point():
    """The result of a vector being added to a point is a point."""
    assert Point((0, 1, 2)) + Vector((3, 4, 5)) == Point((3, 5, 7))


# Point.__radd__
def test__point_right_addition__given_vector_and_point__return_correct_point():
    """The result of a vector being added to a point is a point."""
    assert Vector((0, 1, 2)) + Point((3, 4, 5)) == Point((3, 5, 7))


# Point.__sub__
def test__point_subtraction__given_two_points__return_correct_vector():
    """The result of a point being subtracted from another one is a vector."""
    assert Point((0, 1, 2)) - Point((3, 4, 5)) == Vector((-3, -3, -3))


# Vector.__add__
def test__vector_addition__given_two_vector__return_correct_vector():
    """The result of a vector being added to another one is a vector."""
    assert Vector((0, 1, 2)) + Vector((3, 4, 5)) == Vector((3, 5, 7))


# Vector.__sub__
def test__vector_subtraction__given_two_vectors__return_correct_vector():
    """The result of a vector being subtracted from another one is a vector."""
    assert Vector((0, 1, 2)) - Vector((3, 4, 5)) == Vector((-3, -3, -3))
