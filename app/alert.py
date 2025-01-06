def send_alert(new_pools):
    for pool in new_pools:
        print(f"New pool detected: {pool['address']} for token {pool['mint_x']}")
        # You can replace this with an email, SMS, or webhook call.
