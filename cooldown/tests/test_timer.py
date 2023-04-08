from unittest import TestCase, mock

from cooldown.timer import Timer


@mock.patch("cooldown.timer.get_ticks")
class TestTimer(TestCase):

    def test_create_timer(self, mock_get_ticks):
        mock_get_ticks.return_value = 0
        timer = Timer(1)

        assert timer._time_limit == 1
        assert timer._time_reference == 0

    def test_set_timer(self, mock_get_ticks):
        mock_get_ticks.return_value = 3
        timer = Timer(1)

        mock_get_ticks.return_value = 3
        timer.set_timer()
        assert timer._time_reference == 3

    def test_check_timer(self, mock_get_ticks):
        mock_get_ticks.return_value = 0
        timer = Timer(1)

        mock_get_ticks.return_value = 1
        timer.set_timer()
        assert not timer.check_timer()

        mock_get_ticks.return_value = 3
        assert timer.check_timer()
