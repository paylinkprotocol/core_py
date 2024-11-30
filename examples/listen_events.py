from paylink_protocol import PayLinkProtocolManager

RPC_URL = "https://eth-sepolia.g.alchemy.com/v2/lAY70T35Lt5A4ViwfULpWvgeKfA4k5Q5"
APP_ID = 1732888855

manager = PayLinkProtocolManager(RPC_URL, APP_ID)
manager.subscribe()
