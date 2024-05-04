from utils import mqtt_client as mc

def test_received():
    print("test received")
    mc.publish("markdown/confirmation",{"status":"received"})
    return

mc.add_action("markdown/render",test_received)
mc.start()
