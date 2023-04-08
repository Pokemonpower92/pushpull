from unittest import TestCase, mock

from cooldown.cooldowns import Cooldowns
from cooldown.timer import Timer


def mock_set_timer_5(self):
    self._time_reference = 5


def mock_set_timer_0(self):
    self._time_reference = 0


@mock.patch.object(Timer, "set_timer", autospec=True)
@mock.patch.object(Timer, "check_timer", autospec=True)
class TestCooldowns(TestCase):

    def setUp(self) -> None:
        self._mock_cooldown_data = {
            "cooldown_1": 1,
            "cooldown_2": 2,
            "cooldown_3": 3
        }

    def test_create_cooldowns(self, mock_check_timer, mock_set_timer):
        # No data specified renders an empty internal cooldown dictionary.
        cooldowns = Cooldowns()
        assert cooldowns._cooldowns == {}

        # Internal cooldown dictionary rendered from mock cooldown data.
        cooldowns = Cooldowns(self._mock_cooldown_data)
        for name, timer in cooldowns._cooldowns.items():
            assert name in self._mock_cooldown_data
            assert timer._time_limit == self._mock_cooldown_data[name]

    def test_check_cooldown(self, mock_check_timer, mock_set_timer):
        mock_set_timer.side_effect = mock_set_timer_0
        cooldowns = Cooldowns(self._mock_cooldown_data)

        for name, _ in self._mock_cooldown_data.items():
            mock_check_timer.return_value = False
            assert not cooldowns.check_cooldown(name)

        mock_set_timer.side_effect = mock_set_timer_5

        for name, _ in self._mock_cooldown_data.items():
            mock_check_timer.return_value = True
            assert cooldowns.check_cooldown(name)

    def test_reset_cooldown(self, mock_check_timer, mock_set_timer):
        mock_set_timer.side_effect = mock_set_timer_5
        cooldowns = Cooldowns(self._mock_cooldown_data)

        for name, timer in cooldowns._cooldowns.items():
            assert name in self._mock_cooldown_data
            assert timer._time_limit == self._mock_cooldown_data[name]
            assert timer._time_reference == 5

        for name, timer in cooldowns._cooldowns.items():
            mock_set_timer.side_effect = mock_set_timer_0
            cooldowns.reset_cooldown(name)
            assert timer._time_reference == 0
