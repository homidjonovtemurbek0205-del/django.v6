from django.shortcuts import render
from .forms import StudentForm
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})


def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return render(request, 'success.html')
    data = {'form': form}
    return render(request, 'student.html', data)