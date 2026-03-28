def check_message_length(message):
    if len(message) < 160:
        return message
    else:
        return message[:160]

print(check_message_length("дай бог выпадет эта задача"))
