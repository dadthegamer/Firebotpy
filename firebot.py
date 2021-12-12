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
        response = requests.get(self.url+"api/v1/status")
        if response.json() == {'connections': {'chat': True}}:
            status = "Firebot chat is connected"
        else:
            status = "Firebot chat is not connected"
        return status

    def bot_chat(self, chatmessage):
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

    def streamer_chat(self, chatmessage):
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

    def customvariable(self, varname, vardata):
        data = {
            "effects": {
                "list": [
                    {
                        "type": "firebot:customvariable",
                        "name": varname,
                        "variableData": vardata,
                    }
                ]
            }
        }
        message = "Successfully executed custom variable effect"
        self.sendit(data, message)

    def add_currency(self, currency, amount, username):
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
        response = requests.post(f"{self.url}api/v1/effects/",
                                 headers={"content-type": "application/json"}, data=json.dumps(data))
        if response.json() == {"status": "success"}:
            print(printmessage)
        else:
            print("Failed")

    def preset_effect(self, name, arg="null", argdata="null", arg2="null", arg2data="null", arg3="null", arg3data="null"):
        id = self.get_presetid(name)
        print(id)
        presetarg = {
            "args": {
                arg: argdata,
                arg2: arg2data,
                arg3: arg3data}
        }
        r = requests.post(f"{self.url}api/v1/effects/preset/" + str(id),
                          headers={"content-type": "application/json"}, data=json.dumps(presetarg))
        status = json.loads(r.text)
        if status['status'] == "success":
            print(f"Successfully executed {name} preset effect")
        else:
            print(
                f"Failed to execute {name} preset effect. Check spelling and capitalization")

    def get_currency(self, username, currency):
        currencyid = self.get_currencyid(currency)
        r = requests.get(f"{self.url}api/v1/viewers/{username}/currency/{currencyid}?username=true",
                         headers={"content-type": "application/json"})
        rjson = r.json()
        return rjson

    def get_variable(self, var):
        r = requests.get(f"{self.url}api/v1/custom-variables/{var}",
                         headers={"content-type": "application/json"})
        rjson = r.json()
        return rjson


api = Firebot(f"C:/Users/baile/AppData/Roaming/",
              "http://localhost:7472/")


api.disable_allconnections()
