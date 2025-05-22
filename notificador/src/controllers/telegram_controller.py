from flask import request, jsonify
import json
import requests
from configparser import ConfigParser
import os
import logging

class TelegramController:

    @staticmethod
    def send_message():
        data = json.loads(request.data)
        message = data.get("message")
        if not data:
            return jsonify({"msg": "invalid request"}), 400
        
        else: 
            config = ConfigParser()
            config_path = os.path.abspath("settings.ini")
            config.read(config_path)
            
            
            
            token = config.get("TELEGRAM", "TOKEN")
            chat_id = config.get("TELEGRAM", "CHAT_ID")




            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {
                    "chat_id": chat_id,
                    "text": message
                }
            response = requests.post(url, json=payload)
            return jsonify({"msg": "Se envio correctamente"}), 200