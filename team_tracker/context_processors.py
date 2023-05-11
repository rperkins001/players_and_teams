import requests
from ipware import get_client_ip

def add_location_to_context(request):
    def get_user_location(request):
        ip, is_routable = get_client_ip(request)
        print(f'IP: {ip}, Routable: {is_routable}')
        if ip is None:
            return None
        else:
            response = requests.get(f'http://ip-api.com/json/{ip}')
            data = response.json()
            print(f'Response data: {data}')
            return data.get('city')

    user_location = get_user_location(request)
    if user_location is None:
        user_location = "Not available"  # or whatever default you want
    
    return {'user_location': user_location}
    
