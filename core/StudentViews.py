from django.shortcuts import render

from core.models import Students, Subjects


def student_home(request):
    return render(request, "student_template/student_home_template.html")


def student_view_attendance(request):
    student = Students.objects.get(admin=request.user.id)
    course = student.course_id
    subjects = Subjects.objects.filter(course_id=course)
    return render(request, "student_template/student_view_attendance.html", {"subjects": subjects})
