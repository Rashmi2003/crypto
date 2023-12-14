def log_error(error_message):
   
    print(f"Error: {error_message}")

def handle_request_error(response):
    
    if response.status_code != 200:
        log_error(f"HTTP Request failed with status code {response.status_code}")
        log_error(f"Response content: {response.text}")

def handle_exception(exception, custom_message="An exception occurred"):
   
    log_error(f"{custom_message}: {str(exception)}")
