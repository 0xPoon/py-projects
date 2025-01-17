from hyperliquid.info import Info
from hyperliquid.utils import constants
# import resources

class Connect:

    def __init__(self):
        self.info = Info(constants.MAINNET_API_URL, skip_ws=True) # TESTNET_API_URL

    def print_user_balances(self):
        info = self.info
        print(info.spot_user_state("0x8676F6bD83186D43232b0cD0210Cd86D2f2DFA47"))

connect_to_dapp = Connect()
connect_to_dapp.print_user_balances()