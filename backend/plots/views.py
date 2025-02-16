from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Plot
from .utils.pdf_builder import generate_water_sewage_pdf

@api_view(['POST'])
def check_mpzp(request):
    # ... (kod integracji z Geoportal)
    return Response({"status": "OK"})

@api_view(['POST'])
def generate_pdf(request):
    # ... (logika generowania PDF)
    return Response({"file": "wniosek.pdf"})
