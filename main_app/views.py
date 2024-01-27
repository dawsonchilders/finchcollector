from django.shortcuts import render

finches = [
  {'name': 'Wally', 'description': 'prim and proper gentleman', 'age': 2},
  {'name': 'Taeva', 'description': 'fierce and powerful', 'age': 3},
  {'name': 'Billy', 'description': 'a delightful little scamp', 'age': 1},
  {'name': 'Greta', 'description': 'precocious troublemaker', 'age': 4},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })
