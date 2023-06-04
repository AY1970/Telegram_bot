from django.http import HttpResponse

def commands_view(request):
    commands_list = ['/add_contact', '/view_contacts', '/delete_contact', '/weather']
    response = "Available commands:\n" + "\n".join(commands_list)
    return HttpResponse(response)

def add_contact_view(request):
    # Логика добавления контакта
    return HttpResponse("Contact added.")

def view_contacts_view(request):
    # Логика просмотра контактов
    return HttpResponse("List of contacts.")

def delete_contact_view(request):
    # Логика удаления контакта
    return HttpResponse("Contact removed.")

def weather_view(request):
    # Логика получения информации о погоде
    return HttpResponse("Weather.")

