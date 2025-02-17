from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Plant
from .ai.garden_ai import GardenAI

@api_view(['POST'])
def analyze_garden(request):
    if request.FILES.get('image'):
        # Analiza obrazu AI
        ai = GardenAI()
        plants = ai.analyze_image(request.FILES['image'].temporary_file_path())
        
        # Zapisz rośliny do bazy
        for plant_name in plants:
            Plant.objects.get_or_create(name=plant_name)
            
        return Response({"plants": plants})
    return Response({"error": "Brak obrazu"}, status=400)

@api_view(['GET'])
def get_plants(request):
    plants = Plant.objects.all().values('name', 'watering_interval')
    return Response(list(plants))
