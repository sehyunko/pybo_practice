from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question, Answer


def index(request):
    page = request.GET.get('page', '1') #default page
    question_list = Question.objects.order_by('-create_date')

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer_list = Answer.objects.filter(question_id=question_id)
    context = {'question':question, 'answer_list':answer_list, 'num_answers':answer_list.count()}
    return render(request, 'pybo/question_detail.html', context)
