import pytest
from app import weights

@pytest.mark.parametrize("input_data, expected_output", [
    pytest.param([1, 2, 3], [1, 2, 3], id="ascending_order"),
    pytest.param([3, 2, 1], [1, 2, 3], id="descending_order"),
    pytest.param([2, 3, 1], [1, 2, 3], id="random_order"),
    pytest.param([1, 1, 1], [1, 1, 1], id="all_equal"),
    pytest.param([], [], id="empty_list"),
], ids=str)
def test_weights_happy_path(input_data, expected_output):
    result = weights(input_data)

    assert result == expected_output

@pytest.mark.parametrize("input_data, expected_output", [
    pytest.param([float('inf'), 1, 2], [1, 2, float('inf')], id="contains_infinity"),
    pytest.param([float('-inf'), 1, 2], [float('-inf'), 1, 2], id="contains_negative_infinity"),
    pytest.param([1, 2, float('nan')], [1, 2, float('nan')], id="contains_nan"),
    pytest.param([1.0000001, 1.0, 1.0000002], [1.0, 1.0000001, 1.0000002], id="very_close_floats"),
], ids=str)
def test_weights_edge_cases(input_data, expected_output):

    result = weights(input_data)

    assert result == expected_output

@pytest.mark.parametrize("input_data, expected_exception", [
    pytest.param(None, TypeError, id="none_input"),
    pytest.param("not a list", TypeError, id="string_input"),
    pytest.param([1, "two", 3], TypeError, id="mixed_type_list"),
    pytest.param([1, [2], 3], TypeError, id="nested_list"),
], ids=str)
def test_weights_error_cases(input_data, expected_exception):
    with pytest.raises(expected_exception):
        weights(input_data)
