# roblox-notifier
Simple Python app that sends an SMS notification when a Roblox user comes online.

This could be useful if you are waiting for a friend to come online or trying to catch a streamer online.

# Run
python3 `app/notifier.py`

# Note
In order for this code to work you need a `.env` file in the `app` dir of this project with the following information:
```
twilio_sid="" # twilio account
twilio_token="" # twilio API token
twilio_fnum="" # twilio phone number
twilio_tnum="" # person to send the SMS notification to
```
