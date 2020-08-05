from modules import app, cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase
import logging
import time
import requests


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
        print((self.key))
        if self.key is None or self.key == '':
            cbpi.notify("IFTTT Key Error", "The IFTTT maker key must be set",
                        type="warning", timeout=None)

        url = self.ifttt_url.format(command, self.key)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            cbpi.notify(
                "IFTTT Send Error", "There was an error sending the request to IFTTT. Please check your key", type="danger", timeout=20000)
            self.api.app.logger.error(
                "FAILED to switch IFTTT actor: {}".format(command))

    def on(self, power=None):
        self.send(self.on_hook)
        if power is not None:
            self.set_power(power)

    def off(self):
        self.send(self.off_hook)

    def set_power(self, power):
        power = 100
