#I have created this file
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):

    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', '')
    # Check which checkboxes are checked
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    # Initialize params dictionary
    params = {'purpose': '', 'analyzed_text': djtext}

    # Remove Punctuations
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed
        params['purpose'] += 'Remove Punctuations, '

    # Convert to Uppercase
    if fullcaps == 'on':
        analyzed = djtext.upper()
        djtext = analyzed
        params['purpose'] += 'Convert to Uppercase, '

    # Remove Newlines
    if newlineremover == 'on':
        analyzed = re.sub(r'[\n\r]+', ' ', djtext)
        djtext = analyzed
        params['purpose'] += 'Remove Newlines, '

    # Remove Extra Spaces
    if extraspaceremover == 'on':
        analyzed = re.sub(' +', ' ', djtext)
        djtext = analyzed
        params['purpose'] += 'Remove Extra Spaces, '

    # If no operation is performed
    if removepunc == 'off' and fullcaps == 'off' and newlineremover == 'off' and extraspaceremover == 'off' and charactercounter == 'off':
        return HttpResponse('Error: No operation selected')

    # Remove trailing comma and space from purpose string
    params['purpose'] = params['purpose'].rstrip(', ')

    # Add analyzed text to params dictionary
    params['analyzed_text'] = djtext

    return render(request, 'analyze.html', params)
