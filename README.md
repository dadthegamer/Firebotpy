This is a pyhton libary to connect to Firebots API. This is a standalone project that is not associated with the offical firebot. <br>

```
pip install firebotpy
```

https://firebot.app/
From Firebots Website: <br>
"Firebot is a fully featured open-source bot that can help level up your streams." <br>

# Change Log
## 4.0 (09/12/2022)
-Enable and disable timers <br>
-Firebot Text To Speech <br>
-Role Management <br>
-Get, set, increase counters <br>
-Get system and custom commands <br>

## 3.01 (08/26/2022)
-Rewrote the entire library. No longer need to reference the text file in the local firebot directory. Assumes bot is on localhost <br>
-Added Announce messages <br>
-Added ability to retrive quotes <br>
-Added ability to make new quotes <br>
-Can remove metadata <br>
-Can retrieve user metadata stored in firebots database <br>

## 2.50 (03/31/2022)
-Added ability to get metadata for a users <br>
-Added get_allviewers method to return a list of all viewers in the database <br>
-Changed get_status method to get a boolean type. Returns True if connected and False if not connected <br>

## 2.41 (03/21/2022)
-Bug Fixes <br>

## 2.40 (03/21/2022)
-Added error handling when sending data <br>
-Added a brief description to each method <br>

## 2.31 (16/12/2021)

-Add or remove currency from all online viewers <br>
-Add or remove currency from a specific role <br>

## 2.29 (13/12/2021)

-Added whisper chat from the bot or streamer account <br>
-Added duration for custom variables (default is 0) <br>
-Added getting the value of a counter <br>

## 2.281 (12/12/2021)

-Added set roles for users <br>
-Added remove all users from roles <br>
-Added enable and disable timer <br>
-Added add and remove users to VIP roles <br>
-Added ban and unban users <br>
-Added change scene <br>
-Fixed get_status function <br>

## 2.26 (09/12/2021)

-First Release <br>
