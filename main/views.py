from django.shortcuts import render, redirect

from main.models import Service, ServiceType


def home(request):
    servicetypes = ServiceType.objects.all()

    context = {
        'servicetypes': servicetypes
    }
    return render(request, 'main/index.html', context)


def services(request):
    slug = request.GET.get('type')

    selected_service = ServiceType.objects.get(slug=slug)
    services = Service.objects.filter(service_type=selected_service.id)

    if not services:
        return redirect('home')

    context = {
        'services': services,
        'slug': slug,
        'servicetypes': ServiceType.objects.all()
    }
    return render(request, 'main/services.html', context)


def detail_page(request, slug):
    service =Service.objects.get(slug=slug)
    context = {
        'servicetypes': ServiceType.objects.all(),
        'service': service
    }
    return render(request, 'main/detail-page.html', context)
