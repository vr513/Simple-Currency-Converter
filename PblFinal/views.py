from django.shortcuts import render
from subprocess import run, PIPE
import sys

def button(request):
    return render(request, 'home.html')


def external(request):
    inp1 = request.POST.get('option1',)
    inp2 = request.POST.get('option2')
    amount = str(request.POST.get('amount'))
    out = run([sys.executable, 'C:\\Users\\Varad\\Desktop\\PblFinal\\main.py', inp1, inp2 ,amount], shell=True, stdout= PIPE)
    main_output = (out.stdout).decode("ascii")
    print(main_output)
    return render(request, 'home.html', {'output': main_output})