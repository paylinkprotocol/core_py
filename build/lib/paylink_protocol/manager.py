from .constants import PLP_ROUTER_ADDRESS, PLP_PURCHASE_TOPIC
from .event import Event
from web3 import Web3
from hexbytes import HexBytes
import time

class PayLinkProtocolManager:
    def __init__(self, rpc_url, app_id):
        self.app_id = app_id
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))

    def subscribe(self):
        app_id_bytes = self.app_id.to_bytes(32, byteorder="big")
        filter_params = {
            "fromBlock": "latest",
            "address": PLP_ROUTER_ADDRESS,
            "topics": [
                PLP_PURCHASE_TOPIC,
                Web3.to_hex(app_id_bytes)
            ]
        }

        event_filter = self.web3.eth.filter(filter_params)
        while True:
            try:
                for log in event_filter.get_new_entries():
                    log_data = HexBytes(log["data"])
                    purchased_token = Web3.to_checksum_address("0x" + log["topics"][2].hex()[-40:])
                    user_id = int.from_bytes(log_data[:32], byteorder="big")
                    purchase_amount = int.from_bytes(log_data[32:64], byteorder="big")
                    customer_user_address = Web3.to_checksum_address("0x" + log_data[64:96].hex()[-40:])

                    event = Event(self.app_id, purchased_token, purchase_amount, user_id, customer_user_address)
                    print(event)
                time.sleep(2)
            except Exception as e:
                print(f"Error in event listener: {e}")
                time.sleep(10)
