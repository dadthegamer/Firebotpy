This is a firebot library to connect to Firebots API.

https://firebot.app/
From Firebots Website:
"Firebot is a fully featured open-source bot that can help level up your streams."


You must first pass through the local directory as well as the base url and and port for the api. Below is an example. 
api = Firebot(f"C:/Users/user/AppData/Roaming/",
              "http://localhost:7472/")
Once you do that you can trigger a method:
EXAMPLE: api.get(status)

After you have established your connected you can then trigger effects. Below are the currently supported effects.

Everything is caps sensitive
get_status = returns the connection status of the bot
bot_chat = Sends a chat message from your connected bot
streamer_chat = Sends a chat message from your streamer account
delay = Passes a delay
aws_polly = Text-To-Speech for Amazon Polly. As of now it is just english, US. You can define the voice and volume. See the list of voices in the AWS effect in Firebot.
customvariable = Create/set a value for a variable
add_currency = Adds currency to a defined user
subtract_currency = Subtracts currency to a defined user
set = Sets currency to a defined user
celebration = Trigger one of the celebrations
chat_feed_alert = Send a chat feed alert message
set_counter = Set the value of a counter
increment_counter = Increase the value of a counter
enable_timer = Enables a timer
disable_timer = Disables a timer
reset_timer = Resets a timer
preset_effect = Trigger a preset effect list. As of now there are up to 3 pre defined arguments you can pass through the effect list. 
get_currency = Gets the defined currency value from a username
get_variable = Gets the given variable value
