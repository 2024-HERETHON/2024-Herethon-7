from datetime import datetime, timedelta
import random

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from Countapp.models import Record
from Accountapp.models import Member, Follow
from .forms import FollowForm


@login_required
def home(request):
    user = request.user
    end_date = datetime.now()

    # 현재 날짜를 기준으로 해당 달의 첫째 날을 계산합니다.
    start_date = datetime(end_date.year, end_date.month, 1)

    # 1일부터 오늘까지의 기록을 가져와서 합산합니다.
    records = Record.objects.filter(user=user, create_at__range=(start_date, end_date))
    total_distance = records.aggregate(total_distance=Sum('distance'))['total_distance'] or 0

    year = request.GET.get('year', end_date.year)
    month = request.GET.get('month', end_date.month)

    start1_date = datetime(year=int(year), month=int(month), day=1)
    if int(month) == 12:
        end1_date = datetime(year=int(year) + 1, month=1, day=1)
    else:
        end1_date = datetime(year=int(year), month=int(month) + 1, day=1)

    # 선택한 월의 기록을 필터링
    records1 = Record.objects.filter(user=user, create_at__range=(start1_date, end1_date))
    records_by_date = {}
    random_user=None
    for record in records1:
        date = record.create_at.date().day
        if date not in records_by_date:
            records_by_date[date] = 0
        records_by_date[date] += round(record.distance, 1)
    other_users = Member.objects.exclude(id=request.user.id)
        # 랜덤으로 한 명의 사용자 선택
    random_user = random.choice(other_users) if other_users.exists() else None
    if request.method == 'POST':
        form = FollowForm(request.POST)
        if form.is_valid():
            user_to_follow = get_object_or_404(Member, id=form.cleaned_data['user_id'])
            Follow.objects.get_or_create(follower=user, following=user_to_follow)
            return redirect('homeapp:home')
    else:
        initial_data = {'user_id': random_user.id if random_user else ''}
        form = FollowForm(initial=initial_data)

    context = {
        'user': user,
        'records': records,
        'records_by_date': records_by_date,
        'total_distance': round(total_distance, 1),
        'year': year,
        'month': month,
        'random_user': random_user,
        'form': form,
    }
    return render(request, 'homeapp/home.html', context)

from django.shortcuts import render, get_object_or_404
from .models import ExerciseInfo

def exercise_info_list(request):
    infos = ExerciseInfo.objects.all()
    context = {
        'infos': infos,
    }
    return render(request, 'homeapp/exercise_info_list.html', context)

def exercise_info_detail(request, pk):
    info = get_object_or_404(ExerciseInfo, pk=pk)
    context = {
        'info': info,
    }
    return render(request, 'homeapp/exercise_info_detail.html', context)
from django.shortcuts import render, get_object_or_404
from .models import WalkingCourse

def walking_course_list(request):
    courses = WalkingCourse.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'homeapp/walking_course_list.html', context)

def walking_course_detail(request, pk):
    course = get_object_or_404(WalkingCourse, pk=pk)
    context = {
        'course': course,
    }
    return render(request, 'homeapp/walking_course_detail.html', context)
def splash1(request):
    # If the user is not authenticated, redirect to the splash page.
    if not request.user.is_authenticated:
        return render(request, 'homeapp/splash1.html')
    # If authenticated, redirect to home page.
    return redirect('homeapp:home')
def splash2(request):
    # If the user is not authenticated, redirect to the splash page.
    if not request.user.is_authenticated:
        return render(request, 'homeapp/splash2.html')
    # If authenticated, redirect to home page.
    return redirect('homeapp:home')
def splash3(request):
    # If the user is not authenticated, redirect to the splash page.
    if not request.user.is_authenticated:
        return render(request, 'homeapp/splash3.html')
    # If authenticated, redirect to home page.
    return redirect('homeapp:home')
def splash4(request):
    # If the user is not authenticated, redirect to the splash page.
    if not request.user.is_authenticated:
        return render(request, 'homeapp/splash4.html')
    # If authenticated, redirect to home page.
    return redirect('homeapp:home')
def splash5(request):
    # If the user is not authenticated, redirect to the splash page.
    if not request.user.is_authenticated:
        return render(request, 'homeapp/splash5.html')
    # If authenticated, redirect to home page.
    return redirect('homeapp:home')
