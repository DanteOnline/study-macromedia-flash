from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from ttest.form import ProfiForm
from ttest.models import ProfiQuestion, QuestionAnswer, JuniorQuestion, JuniorAnswer, SeniorQuestion, SeniorAnswer
from generic.mixin import TheoryMixin
from theory.models import Theory
from django.core.urlresolvers import reverse

# Create your views here.
def start_junior_test(request, pk):
    request.session['theory_pk'] = pk
    questions = JuniorQuestion.objects.filter(theme__pk=pk)
    questions_pks = [q.pk for q in questions]
    request.session['questions_pks'] = questions_pks
    request.session['answers_pks'] = []
    current_index = 0
    request.session['current_index'] = current_index
    return redirect('junior_form', pk=questions_pks[current_index])

def start_senior_test(request, pk):
    request.session['theory_pk'] = pk
    questions = SeniorQuestion.objects.filter(theme__pk=pk)
    questions_pks = [q.pk for q in questions]
    request.session['questions_pks'] = questions_pks
    request.session['answers_pks'] = []
    current_index = 0
    request.session['current_index'] = current_index
    return redirect('senior_form', pk=questions_pks[current_index])

def start_profi_test(request, pk):
    request.session['theory_pk'] = pk
    questions = ProfiQuestion.objects.filter(theme__pk = pk)
    questions_pks = [q.pk for q in questions]
    request.session['questions_pks'] = questions_pks
    request.session['answers'] = []
    current_index = 0
    request.session['current_index'] = current_index
    return redirect('profi_form',pk=questions_pks[current_index])

class EndJuniorTestView(TemplateView, TheoryMixin):
    template_name = 'end_junior.html'

    def get_context_data(self, **kwargs):
        context = super(EndJuniorTestView, self).get_context_data(**kwargs)
        current_theory_pk = self.request.session['theory_pk']
        context['theory'] = Theory.objects.get(pk=current_theory_pk)
        questions_pks = self.request.session['questions_pks']
        answers_pks = self.request.session['answers_pks']
        answers = []
        for pk in answers_pks:
            answer = JuniorAnswer.objects.get(pk=pk)
            answers.append(answer)
        questions = [JuniorQuestion.objects.get(pk=qpk) for qpk in questions_pks]
        context['answers'] = answers
        context['questions'] = questions
        tru_answers = []
        for q in questions:
            tru_answer = JuniorAnswer.objects.get(question = q, is_true = True)
            tru_answers.append(tru_answer)

        context['tru_answers'] = tru_answers
        tru_count = len(answers)
        count = 0
        qas = []
        for i in range(tru_count):
            q = questions[i]
            a = answers[i]
            qa = QuestionAnswer(q,a)
            if answers[i] == tru_answers[i]:
                count+=1
                qa.is_true = True
            qas.append(qa)
        context['tru_count'] = tru_count
        context['count'] = count
        context['qas'] = qas
        if float(count)/float(tru_count) < 0.8:
            context['ok'] = False
        else:
            context['ok'] = True
        return context

class EndSeniorTestView(TemplateView, TheoryMixin):
    template_name = 'end_senior.html'

    def get_context_data(self, **kwargs):
        context = super(EndSeniorTestView, self).get_context_data(**kwargs)
        current_theory_pk = self.request.session['theory_pk']
        context['theory'] = Theory.objects.get(pk=current_theory_pk)
        questions_pks = self.request.session['questions_pks']
        answers_pks = self.request.session['answers_pks']
        answers = []
        for pk_list in answers_pks:
            answer_list = []
            for pk in pk_list:
                answer = SeniorAnswer.objects.get(pk=pk)
                answer_list.append(answer)
            answers.append(answer_list)
        questions = [SeniorQuestion.objects.get(pk=qpk) for qpk in questions_pks]
        context['answers'] = answers
        context['questions'] = questions
        tru_answers = []
        for q in questions:
            tru_answer = SeniorAnswer.objects.filter(question = q, is_true = True)
            tru_answers.append(tru_answer)

        context['tru_answers'] = tru_answers
        tru_count = len(answers)
        count = 0
        qas = []
        for i in range(tru_count):
            q = questions[i]
            a = answers[i]
            qa = QuestionAnswer(q,a)
            ta=tru_answers[i]
            if len(a) == len(ta):
                is_eq = True
                for j in range(len(a)):
                    if a[j] not in ta:
                        is_eq = False
                        break
                if is_eq:
                    count+=1
                    qa.is_true = True
            qas.append(qa)
        context['tru_count'] = tru_count
        context['count'] = count
        context['qas'] = qas
        if float(count)/float(tru_count) < 0.8:
            context['ok'] = False
        else:
            context['ok'] = True
        return context

class EndProfiTestView(TemplateView, TheoryMixin):
    template_name = 'end_profi.html'

    def get_context_data(self, **kwargs):
        context = super(EndProfiTestView, self).get_context_data(**kwargs)
        current_theory_pk = self.request.session['theory_pk']
        context['theory'] = Theory.objects.get(pk=current_theory_pk)
        questions_pks = self.request.session['questions_pks']
        answers = self.request.session['answers']
        questions = [ProfiQuestion.objects.get(pk=qpk) for qpk in questions_pks]
        context['answers'] = answers
        context['questions'] = questions
        tru_answers = [q.answer for q in questions]
        context['tru_answers'] = tru_answers
        tru_count = len(answers)
        count = 0
        qas = []
        for i in range(tru_count):
            q = questions[i]
            a = answers[i]
            qa = QuestionAnswer(q,a)
            if answers[i].replace(' ','') == tru_answers[i].replace(' ',''):
                count+=1
                qa.is_true = True
            qas.append(qa)
        context['tru_count'] = tru_count
        context['count'] = count
        context['qas'] = qas
        if count//tru_count < 5:
            context['ok'] = False
        else:
            context['ok'] = True
        return context

class ProfiFormView(FormView, TheoryMixin):
    form_class = ProfiForm
    template_name = 'profi_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProfiFormView, self).get_context_data(**kwargs)
        current_index = self.request.session['current_index']
        context['number'] = current_index+1
        current_question_pk = self.request.session['questions_pks'][current_index]
        question = ProfiQuestion.objects.get(pk=current_question_pk)
        context['question'] = question
        context['answers'] = self.request.session['answers']
        return context

    def form_valid(self, form):
        answer = form.cleaned_data['answer']
        self.request.session['answers'].append(answer)
        current_index = int(self.request.session['current_index'])
        questions_pks = self.request.session['questions_pks']
        count = int(len(questions_pks))
        if current_index < count-1:
            current_index += 1
            self.request.session['current_index'] = current_index
            return redirect('profi_form',pk=questions_pks[current_index])
        else:
            self.request.session.modified = True
            return redirect('end_profi_test')

class JuniorTemplateView(TemplateView, TheoryMixin):
    template_name = 'junior_form.html'

    def get_context_data(self, **kwargs):
        context = super(JuniorTemplateView, self).get_context_data(**kwargs)
        current_index = self.request.session['current_index']
        context['number'] = current_index+1
        current_question_pk = self.request.session['questions_pks'][current_index]
        question = JuniorQuestion.objects.get(pk=current_question_pk)
        context['question'] = question
        context['answers'] = self.request.session['answers']
        junior_answers = JuniorAnswer.objects.filter(question=question)
        context['junior_answers'] = junior_answers
        return context

    def post(self, request, *args, **kwargs):
        answer_pk = self.request.POST['j']
        self.request.session['answers_pks'].append(answer_pk)
        current_index = int(self.request.session['current_index'])
        questions_pks = self.request.session['questions_pks']
        count = int(len(questions_pks))
        if current_index < count - 1:
            current_index += 1
            self.request.session['current_index'] = current_index
            return redirect('junior_form', pk=questions_pks[current_index])
        else:
            request.session.modified = True
            return redirect('end_junior_test')

class SeniorTemplateView(TemplateView, TheoryMixin):
    template_name = 'senior_form.html'

    def get_context_data(self, **kwargs):
        context = super(SeniorTemplateView, self).get_context_data(**kwargs)
        current_index = self.request.session['current_index']
        context['number'] = current_index+1
        current_question_pk = self.request.session['questions_pks'][current_index]
        question = SeniorQuestion.objects.get(pk=current_question_pk)
        context['question'] = question
        context['answers'] = self.request.session['answers_pks']
        senior_answers = SeniorAnswer.objects.filter(question=question)
        context['senior_answers'] = senior_answers
        return context

    def post(self, request, *args, **kwargs):
        answer_pks = self.request.POST.getlist('j')
        self.request.session['answers_pks'].append(answer_pks)
        current_index = int(self.request.session['current_index'])
        questions_pks = self.request.session['questions_pks']
        count = int(len(questions_pks))
        if current_index < count - 1:
            current_index += 1
            self.request.session['current_index'] = current_index
            return redirect('senior_form', pk=questions_pks[current_index])
        else:
            request.session.modified = True
            return redirect('end_senior_test')

class TestMainView(TemplateView, TheoryMixin):
    template_name = 'test_index.html'

