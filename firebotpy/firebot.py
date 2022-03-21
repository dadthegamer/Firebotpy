import requests
import json


class Firebot:

    def __init__(self, directory, url):
        self.directory = directory
        self.url = url

    def get_presetid(self, name):
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/effects/preset-effect-lists.json', 'r') as f:
            data = json.load(f)
        effects = data.keys()
        for effect in effects:
            if name == data[effect]['name']:
                id = data[effect]['id']
        f.close()
        return id

    def get_roleid(self, name):
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/roles/customroles.json', 'r') as f:
            data = json.load(f)
        roles = data.keys()
        for role in roles:
            if name == data[role]['name']:
                id = data[role]['id']
        f.close()
        return id

    def get_timerid(self, name):
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/timers.json', 'r') as f:
            data = json.load(f)
        timers = data.keys()
        for timer in timers:
            if name == data[timer]['name']:
                id = data[timer]['id']
        f.close()
        return id

    def get_currencyid(self, name):
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/currency/currency.json', 'r') as f:
            data = json.load(f)
        currencies = data.keys()
        for currency in currencies:
            if name == data[currency]['name']:
                id = data[currency]['id']
        f.close()
        return id

    def get_counterid(self, name):
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/counters/counters.json', 'r') as f:
            data = json.load(f)
        counters = data.keys()
        for counter in counters:
            if name == data[counter]['name']:
                id = data[counter]['id']
        f.close()
        return id

    def get_all_presets(self):
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/effects/preset-effect-lists.json', 'r') as f:
            data = json.load(f)
        effects = data.keys()
        presetdict = {}
        for effect in effects:
            name = data[effect]['name']
            id = data[effect]['id']
            presetdict[name] = id
        f.close()
        return presetdict

    def get_status(self):
        attempts = 0
        while attempts <= 5:
            try:
                response = requests.get(self.url+"api/v1/status")
                if response.json() == {'connections': {'chat': True}}:
                    status = "Firebot chat is connected"
                else:
                    status = "Firebot chat is not connected"
                return status
            except:
                attempts += 1

    def bot_chat(self, chatmessage):
        """
        Send a message as the bot.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:chat",
                        "message": chatmessage,
                        "chatter": "Bot",
                    }
                ]
            }
        }
        message = "Successfully sent chat message as bot"
        self.sendit(data, message)

    def whisper_chatbot(self, username, chatmessage):
        """
        Send a whisper message as the bot.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:chat",
                        "chatter": "Bot",
                        "whisper": username,
                        "message": chatmessage,
                    }
                ]
            }
        }
        message = "Successfully sent whisper chat message as bot"
        self.sendit(data, message)

    def whisper_chatstreamer(self, username, chatmessage):
        """
        Send a whisper message as the streamer.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:chat",
                        "chatter": "Streamer",
                        "whisper": username,
                        "message": chatmessage,
                    }
                ]
            }
        }
        message = "Successfully sent whisper chat message as streamer"
        self.sendit(data, message)

    def streamer_chat(self, chatmessage):
        """
        Send a message in chat as the streamer.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:chat",
                        "message": chatmessage,
                        "chatter": "Streamer",
                    }
                ]
            }
        }
        message = "Successfully sent chat message as streamer"
        self.sendit(data, message)

    def enable_twitchconnection(self):
        """
        Turn on Twitch connection.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:toggleconnection",
                        "allAction": "toggle",
                        "services": [
                            {
                                "id": "chat",
                                "action": True
                            }
                        ],
                        "mode": "custom",
                    }
                ]
            }
        }
        message = "Successfully enabled chat connection"
        self.sendit(data, message)

    def disable_twitchconnection(self):
        """
        Turn off Twitch connection.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:toggleconnection",
                        "allAction": "toggle",
                        "services": [
                            {
                                "id": "chat",
                                "action": False
                            }
                        ],
                        "mode": "custom",
                    }
                ]
            }
        }
        message = "Successfully disabled chat connection"
        self.sendit(data, message)

    def enable_allconnections(self):
        """
        Turn on all connections.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:toggleconnection",
                        "allAction": "true",
                        "services": [
                            {
                                "id": "chat",
                                "action": True
                            }
                        ],
                        "mode": "all",
                    }
                ]
            }
        }
        message = "Successfully enabled all connections"
        self.sendit(data, message)

    def disable_allconnections(self):
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:toggleconnection",
                        "allAction": "false",
                        "services": [
                            {
                                "id": "chat",
                                "action": True
                            }
                        ],
                        "mode": "all",
                    }
                ]
            }
        }
        message = "Successfully disabled all connections"
        self.sendit(data, message)

    def delay(self, delaytime):
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:delay",
                        "delay": delaytime
                    }
                ]
            }
        }
        message = f"Delay of {delaytime} executed"
        self.sendit(data, message)

    def aws_polly(self, message, voiceid, volume):
        """
        Sends a message to Amazon Polly. Must have Amazon Polly set up in firebot
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "aws:polly",
                        "text": message,
                        "voiceId": voiceid,
                        "volume": volume,
                    }
                ]
            }
        }
        message = "Successfully executed AWS Polly effect"
        self.sendit(data, message)

    def customvariable(self, varname, vardata, duration=0):
        """
        Sets the value of a custom variable.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:customvariable",
                        "ttl": duration,
                        "name": varname,
                        "variableData": vardata,
                    }
                ]
            }
        }
        message = "Successfully executed custom variable effect"
        self.sendit(data, message)

    def add_currency(self, currency, amount, username):
        """
        Add currency to a user.
        """
        currencyid = self.get_currencyid(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Add",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "individual",
                        "userTarget": username
                    }
                ]
            }
        }
        message = f"Successfully added {currency} to {username}"
        self.sendit(data, message)

    def subtract_currency(self, currency, amount, username):
        """
        Subtracts currency from a user.
        """
        currencyid = self.get_currencyid(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Remove",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "individual",
                        "userTarget": username
                    }
                ]
            }
        }
        message = f"Successfully removed {currency} from {username}"
        self.sendit(data, message)

    def set_currency(self, currency, amount, username):
        """
        Sets the currency value for a user.
        """
        currencyid = self.get_currencyid(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Set",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "individual",
                        "userTarget": username
                    }
                ]
            }
        }
        message = f"Successfully set {currency} for {username}"
        self.sendit(data, message)

    def celebration(self, celebrationtype, celebrationtime):
        """
        Trigger a firebot celebration. Either Fireworks or Confetti.
        """
        if celebrationtype == "Fireworks" or celebrationtype == "Confetti":
            data = {
                "effects": {
                    "list": [
                        {
                            "type": "firebot:celebration",
                            "celebration": celebrationtype,
                            "length": celebrationtime
                        }
                    ]
                }
            }
            message = f"Successfully sent {celebrationtype} celebration"
            self.sendit(data, message)
        else:
            return "Celebration type must be Fireworks or Confetti. Check capitalization"

    def chat_feed_alert(self, message):
        """
        Send a chat feed alert.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:chat-feed-alert",
                        "message": message,
                    }
                ]
            }
        }
        message = "Successfully sent chat feed alert"
        self.sendit(data, message)

    def set_counter(self, countername, value):
        """
        Set a counter to a specific value.
        """
        counterid = self.get_counterid(countername)
        data = {
            "effects": {
                "list": [
                    {
                        "counterId": counterid,
                        "mode": "set",
                        "type": "firebot:update-counter",
                        "value": value,
                    }
                ]
            }
        }
        message = f"Successfully set {countername} counter to {value}"
        self.sendit(data, message)

    def increment_counter(self, countername, value):
        """
        Increment a counter by a specified amount.
        """
        counterid = self.get_counterid(countername)
        data = {
            "effects": {
                "list": [
                    {
                        "counterId": counterid,
                        "mode": "increment",
                        "type": "firebot:update-counter",
                        "value": value,
                    }
                ]
            }
        }
        message = f"Successfully incremented {countername} counter by {value}"
        self.sendit(data, message)

    def add_role(self, role, username):
        """
        Add a user to a specific role.
        """
        roleid = self.get_roleid(role)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:update-roles",
                        "viewerType": "custom",
                        "addRoleId": roleid,
                        "customViewer": username,
                    }
                ]
            }
        }
        message = f"Successfully added {username} to {role} role"
        self.sendit(data, message)

    def add_vip(self, username):
        """
        Add a user to VIP.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:update-vip-role",
                        "action": "Add VIP",
                        "username": username
                    }
                ]
            }
        }
        message = f"Successfully added {username} to VIP role"
        self.sendit(data, message)

    def remove_vip(self, username):
        """
        Remove a user from VIP.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:update-vip-role",
                        "action": "Remove VIP",
                        "username": username
                    }
                ]
            }
        }
        message = f"Successfully removed {username} to VIP role"
        self.sendit(data, message)

    def ban_user(self, username):
        """
        Ban a user.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:modban",
                        "action": "Ban",
                        "username": username
                    }
                ]
            }
        }
        message = f"Successfully banned {username}"
        self.sendit(data, message)

    def unban_user(self, username):
        """
        Unban a user.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:modban",
                        "action": "Unban",
                        "username": username
                    }
                ]
            }
        }
        message = f"Successfully banned {username}"
        self.sendit(data, message)

    def change_obs_scene(self, scene):
        data = {
            "effects": {
                "list": [
                    {
                        "type": "ebiggz:obs-change-scene",
                        "custom": True,
                        "sceneName": scene,
                    }
                ]
            }
        }
        message = f"Successfully changed scene to {scene}"
        self.sendit(data, message)

    def remove_allrole(self, role):
        """
        Removes all users from a specific role.
        """
        roleid = self.get_roleid(role)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:update-roles",
                        "viewerType": "current",
                        "removeAllRoleId": roleid,
                    }
                ]
            }
        }
        message = f"Successfully removed all users from {role}"
        self.sendit(data, message)

    def remove_user_role(self, role, username):
        """
        Removes a user from a specific role.
        """
        roleid = self.get_roleid(role)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:update-roles",
                        "viewerType": "custom",
                        "removeAllRoleId": roleid,
                        "customViewer": username,
                    }
                ]
            }
        }
        message = f"Successfully removed {username} from {role}"
        self.sendit(data, message)

    def set_metadata(self, key, data, username):
        """
        Set the metadata for a user.
        """
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:set-user-metadata",
                        "username": username,
                        "key": key,
                        "data": data,
                    }
                ]
            }
        }
        message = f"Successfully set {key} metadata for {username} to {username}"
        self.sendit(data, message)

    def enable_timer(self, timername):
        """
        Enable a given timer.
        """
        timerid = self.get_timerid(timername)
        data = {
            "effects": {
                "list": [
                    {
                        "selectedTimerId": timerid,
                        "toggleType": "enable",
                        "type": "firebot:toggle-timer",
                    }
                ]
            }
        }
        message = f"Successfully enabled {timername} timer"
        self.sendit(data, message)

    def disable_timer(self, timername):
        """
        Disable a given timer.
        """
        timerid = self.get_timerid(timername)
        data = {
            "effects": {
                "list": [
                    {
                        "selectedTimerId": timerid,
                        "toggleType": "disable",
                        "type": "firebot:toggle-timer",
                    }
                ]
            }
        }
        message = f"Successfully disabled {timername} timer"
        self.sendit(data, message)

    def reset_timer(self, timername):
        """
        Resets a given timer to its default value.
        """
        timerid = self.get_timerid(timername)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:reset-timer",
                        "selectedTimerId": timerid,
                    }
                ]
            }
        }
        message = f"Successfully reset {timername} timer"
        self.sendit(data, message)

    def sendit(self, data, printmessage):
        attempts = 0
        while attempts <= 5:
            try:
                response = requests.post(f"{self.url}api/v1/effects/",
                                        headers={"content-type": "application/json"}, data=json.dumps(data))
                if response.json() == {"status": "success"}:
                    break
                else:
                    print("Failed")
            except:
                attempts += 1

    def preset_effect(self, name, arg="null", argdata="null", arg2="null", arg2data="null", arg3="null", arg3data="null", arg4="null", arg4data="null"):
        """
        Triggers a given preset effect list. Able to pass in preset args as well.
        """
        id = self.get_presetid(name)
        print(id)
        presetarg = {
            "args": {
                arg: argdata,
                arg2: arg2data,
                arg3: arg3data,
                arg4: arg4data}
        }
        attempts = 0
        while attempts <= 5:
            try:
                r = requests.post(f"{self.url}api/v1/effects/preset/" + str(id),
                                headers={"content-type": "application/json"}, data=json.dumps(presetarg))
                status = json.loads(r.text)
                if status['status'] == "success":
                    print(f"Successfully executed {name} preset effect")
                else:
                    print(
                        f"Failed to execute {name} preset effect. Check spelling and capitalization")
            except:
                attempts += 1

    def get_currency(self, username, currency):
        """
        Retrives how much currency a specific user has
        """
        currencyid = self.get_currencyid(currency)
        attempts = 0
        while attempts <= 5:
            try:
                r = requests.get(f"{self.url}api/v1/viewers/{username}/currency/{currencyid}?username=true",
                                headers={"content-type": "application/json"})
                rjson = r.json()
                return rjson
            except:
                attempts += 1

    def get_variable(self, var):
        """
        Retrives the value of a given variable
        """
        attempts = 0
        while attempts <= 5:
            try:
                r = requests.get(f"{self.url}api/v1/custom-variables/{var}",
                                headers={"content-type": "application/json"})
                rjson = r.json()
                return rjson
            except:
                attempts += 1

    def get_allvariable(self):
        r = requests.get(f"{self.url}api/v1/custom-variables",
                         headers={"content-type": "application/json"})
        rjson = r.json()
        return rjson

    def get_topcurrency(self, name, count = 10):
        """
        Retrives the top users in a specific currency. Defaults to top 10
        """
        attempts = 0
        while attempts <= 5:
            try:
                r = requests.get(f"{self.url}api/v1/currency/{name}/top?count={count}",
                                headers={"content-type": "application/json"})
                rjson = r.json()
                currency_list = []
                id = self.get_currencyid(name)
                for users in rjson:
                    userdict = {}
                    username = users['username']
                    amount = users['currency'][id]
                    userdict = {'username': username, 'amount': amount}
                    currency_list.append(userdict)
                return currency_list
            except:
                attempts += 1

    def get_countervalue(self, name):
        """
        Retrives the value of a specific counter
        """
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/counters/counters.json', 'r') as f:
            data = json.load(f)
        counters = data.keys()
        for counter in counters:
            if name == data[counter]['name']:
                value = int(data[counter]['value'])
        f.close()
        return value

    def view_rolemembers(self, rolename, username):
        """
        View all members in a specific role
        """
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/roles/customroles.json', 'r') as f:
            data = json.load(f)
        roles = data.keys()
        for role in roles:
            if rolename == data[role]['name']:
                role = data[role]['viewers']
                if username in role:
                    in_role = True
                else:
                    in_role = False
            else:
                print(f"Did not find {rolename}. Check your spelling")
        f.close()
        return in_role

    def get_command(self, name):
        with open(f'{self.directory}Firebot/v5/profiles/Main Profile/chat/commands.json', 'r') as f:
            data = json.load(f)
            x = data['customCommands']
        commands = data.keys()
        for command in x:
            print(x[command][name])

    def add_currency_online(self, currency, amount):
        """
        Adds currency to all online viewers
        """
        currencyid = self.get_currencyid(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Add",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "allOnline",
                    }
                ]
            }
        }
        message = f"Successfully added {amount} {currency} to all online viewers"
        self.sendit(data, message)

    def remove_currency_online(self, currency, amount):
        """
        Removes currency from all online viewers
        """
        currencyid = self.get_currencyid(currency)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "action": "Remove",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "allOnline",
                    }
                ]
            }
        }
        message = f"Successfully added {amount} {currency} to all online viewers"
        self.sendit(data, message)

    def add_currency_role(self, currency, amount, role):
        """
        Adds currency to a specific role
        """
        currencyid = self.get_currencyid(currency)
        roleid = self.get_roleid(role)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "roleIds": [
                            roleid
                        ],
                        "action": "Add",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "group",
                    }
                ]
            }
        }
        message = f"Successfully added {amount} {currency} to all users in {role} role"
        self.sendit(data, message)

    def remove_currency_role(self, currency, amount, role):
        """
        Removes currency from a specific role
        """
        currencyid = self.get_currencyid(currency)
        roleid = self.get_roleid(role)
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:currency",
                        "roleIds": [
                            roleid
                        ],
                        "action": "Remove",
                        "currency": currencyid,
                        "amount": amount,
                        "target": "group",
                    }
                ]
            }
        }
        message = f"Successfully removed {amount} {currency} to all users in {role} role"
        self.sendit(data, message)

