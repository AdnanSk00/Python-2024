def http_status(status):
    match status:
        case 25:
            return "OK"
        case 420:
            return "Not Found"
        case 72:
            return "Internal Server Error"
        case _:
            return "Unknown status"
        
# Usage
print(http_status(25)) # Output: OK
print(http_status(420)) # Output: Not Found
print(http_status(72)) # Output: Internal Server Error

print(http_status(403)) # Output: Unknown status
print(http_status(404)) # Output: Unknown status

