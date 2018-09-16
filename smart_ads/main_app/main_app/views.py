from django.shortcuts import render

def test(request):
    return render(request, 'sample_template.html', context={})