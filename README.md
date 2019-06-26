# cbpi-iftttwebhookactor

This actor can be used to switch any of the smart switches that the IFTTT platform allows. Simply pick which one you use from the `+ that` section

## Setup
1. Create an IFTTT account at https://ifttt.com/
2. Click `My Applets` at the top of the screen
3. Click on `New Applet`
4. In `+ this` add a new `Webhooks` service
5. Choose `Receive a web request` and give it a name (bear in mind that the on and off of the actor will require a different webhook)
6. In `+ that` pick the required actor to switch

## Adding to Cbpi
1. Add a new actor and choose `IFTTTWebhookActor` as the type
2. Enter your maker api key which can be found in setting section of this page https://ifttt.com/maker_webhooks
3. Add the name of your on and off webhooks

I tested this by simply downloading the IFTTT app onto my smartphone and then in the `+ that` section selecting notification. This will send you a notification to your smartphone
