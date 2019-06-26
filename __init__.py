from modules import app, cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase
import logging
import time
import requests

# ifttt_key = None
# ifttt_event = None
# ifttt = None


@cbpi.actor
class IFTTTWebhookActor(ActorBase):
    ifttt_url = "https://maker.ifttt.com/trigger/{}/with/key/{}"

    key = Property.Text("Maker Webhook Key", configurable=True,
                        default_value="", description="The key to be able to use this webhook")
    on_hook = Property.Text("On Hook Name", configurable=True,
                            default_value="", description="The webhook name for the on command")
    off_hook = Property.Text("Off Hook Name", configurable=True,
                             default_value="", description="The webhook name for the off command")

    power = 100

    def send(self, command):
        print(self.key)
        if self.key is None:
            cbpi.notify("IFTTT Key Error", "The IFTTT maker key must be set",
                        type="warning", timeout=None)

        url = self.ifttt_url.format(command, self.key)

        try:
            response = requests.get(url)
            print(response)
        except requests.exceptions.RequestException as err:
            print(err)
            cbpi.notify(
                "IFTTT Send Error", "There was an error sending the request to IFTTT", type="error", timeout=5)

    def on(self, power=None):
        self.send(self.on_hook)
        if power is not None:
            self.set_power(power)

    def off(self):
        self.send(self.off_hook)

    def set_power(self, power):
        power = 100
