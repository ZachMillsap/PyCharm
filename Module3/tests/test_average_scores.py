from format_output import average_scores


def test_average(self):
    with mock.patch('builtins.input', side_effect=[85,90,95]):
        assert topic2.average() == 90
