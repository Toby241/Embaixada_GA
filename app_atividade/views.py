from django.shortcuts import render, get_object_or_404

# Create your views here.
def servicos(request):
  return render(request, 'servicos.html')

# views.py

def dashboard_view(request):
    return render(request, 'https://app.smartsupp.com/app/dashboard/conversations/coZW8OTEUPVmg')
