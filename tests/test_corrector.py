import pytest
import pandas as pd

from corrector import calculate_profit, InvalidActionError, StockNumExceedError


class TestCalculateProfit:
    @pytest.fixture(scope='function')
    def stocks(self):
        FEATURE_NAMES = ('open', 'high', 'low', 'close')
        return pd.read_csv('tests/testing_data.csv', names=FEATURE_NAMES)

    @pytest.fixture(scope='function')
    def init_actions(self, stocks):
        return [0] * (len(stocks) - 1)

    def test_buy_and_hold(self, stocks, init_actions):
        actions = init_actions
        actions[0] = 1

        profit = calculate_profit(stocks, actions)
        assert profit == pytest.approx(45.037079)

    def test_sellshort_and_hold(self, stocks, init_actions):
        actions = init_actions
        actions[0] = -1

        profit = calculate_profit(stocks, actions)
        assert profit == pytest.approx(-45.037079)

    def test_holding_more_than_one(self, stocks, init_actions):
        actions = init_actions
        actions[0] = 1
        actions[2] = 1

        with pytest.raises(StockNumExceedError) as err_info:
            profit = calculate_profit(stocks, actions)

        assert err_info.value.args[0] == 'You cannot buy stocks when you hold one'

    def test_selling_short_more_than_one(self, stocks, init_actions):
        actions = init_actions
        actions[0] = -1
        actions[2] = -1

        with pytest.raises(StockNumExceedError) as err_info:
            profit = calculate_profit(stocks, actions)

        assert err_info.value.args[0] == "You cannot sell short stocks when you've already sell short one"

    def test_invalid_action(self, stocks, init_actions):
        actions = init_actions
        actions[0] = 'Invalid'

        with pytest.raises(InvalidActionError) as err_info:
            profit = calculate_profit(stocks, actions)

        assert err_info.value.args[0] == 'Invalid Action'
