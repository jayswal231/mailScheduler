from django.shortcuts import render, redirect
from .forms import ReminderForm
from django.contrib.auth.decorators import login_required
from .models import Reminder
from .tasks import send_reminder_email
# Create your views here.

@login_required
def home(request):
    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'reminders/home.html', {'reminders': reminders})


@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()

            send_reminder_email.delay(
                subject=reminder.subject,
                message=reminder.message,
                recipient_email=reminder.email
            )

            return redirect('home')
    else:
        form = ReminderForm()
    return render(request, 'reminders/add_reminder.html', {'form': form})
