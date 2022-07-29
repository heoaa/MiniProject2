
from django.http import HttpResponse
from django.shortcuts import render
from .model_survey import survey

# -------------------------------------------------------------------------------------------
# 테스트 페이지
def test(request):
    return render(request,
           'surveyapp/test.html',
           {})
# -------------------------------------------------------------------------------------------
# 메인 페이지
def main(request):
    return render(request,
           'surveyapp/main.html',
           {})
# -------------------------------------------------------------------------------------------
# Part1_01 연도별 최저임금 현황
def part1_01(request):
    return render(request,
           'surveyapp/part1_01.html',
           {})
# -------------------------------------------------------------------------------------------
# Part1_02 연도별 물가 현황    
def part1_02(request):
    return render(request,
           'surveyapp/part1_02.html',
           {})
# -------------------------------------------------------------------------------------------
# Part1_01 연도별 GDP 현황
def part1_03(request):
    return render(request,
           'surveyapp/part1_03.html',
           {})
# -------------------------------------------------------------------------------------------
# 설문조사 폼
def survey_form(request):
    return render(request,
           'surveyapp/survey_form.html',
           {})
# -------------------------------------------------------------------------------------------
# 설문조사 고용주
def survey_employer(request):
    return render(request,
           'surveyapp/survey_employer.html',
           {})
# -------------------------------------------------------------------------------------------
# 설문조사 근로자
def survey_worker(request):
    return render(request,
           'surveyapp/survey_worker.html',
           {})
# -------------------------------------------------------------------------------------------
# 설문 DB TABLE 생성
def createTable(request):
    survey.createTableSurvey()
    
    return HttpResponse("Create OK")
# -------------------------------------------------------------------------------------------
# 입력한 고용주 설문 DB 저장
def set_Survey_Employer_Insert(request) :
    peco = request.POST.get("eco")
    page = request.POST.get("age")
    pgender = request.POST.get("gender")
    pQ1 = request.POST.get("Q1")
    pQ1_1 = request.POST.get("Q1_1")
    pQ1_2 = request.POST.get("Q1_2")
    pQ2 = request.POST.get("Q2")
    pQ3 = request.POST.get("Q3")
    pQ4 = request.POST.get("Q4")
    pQ5 = request.POST.get("Q5")
    pQ6 = request.POST.get("Q6")
    
    rs = survey.setSurveyEmployerInsert(peco, page, pgender, pQ1,pQ1_1,pQ1_2,pQ2,pQ3,pQ4,pQ5,pQ6)
    
    msg = ""
    if rs == "OK" :
        msg = """<script>
                    alert('설문에 참여해 주셔서 감사합니다')
                    location.href = '/survey/survey_employer_list'
                    </script>"""
    else: 
        msg = """<script>
                    alert('실패')
                    history.go(-1)
                    </script>"""
    return HttpResponse(msg)
# -------------------------------------------------------------------------------------------
# 고용주 설문 전체 조회
def view_Survey_Employer_List(request) :
    
    df = survey.getSurveyEmployerList()
    
    # return HttpResponse(df.to_html())
    context = {"df" : df.to_html}
    
    return render(
        request,
        "surveyapp/survey_employer_list.html",
        context
    )
# -------------------------------------------------------------------------------------------
# 입력한 근로자 설문 DB 저장
def set_Survey_Worker_Insert(request) :
    peco = request.POST.get("eco")
    page = request.POST.get("age")
    pgender = request.POST.get("gender")
    pQ1 = request.POST.get("Q1")
    pQ1_1 = request.POST.get("Q1_1")
    pQ1_2 = request.POST.get("Q1_2")
    pQ2 = request.POST.get("Q2")
    pQ3 = request.POST.get("Q3")
    pQ4 = request.POST.get("Q4")
    pQ5 = request.POST.get("Q5")
    pQ6 = request.POST.get("Q6")
    pQ7 = request.POST.get("Q7")
    
    rs = survey.setSurveyWorkerInsert(peco, page, pgender, pQ1,pQ1_1,pQ1_2,pQ2,pQ3,pQ4,pQ5,pQ6,pQ7)
    
    msg = ""
    if rs == "OK" :
        msg = """<script>
                    alert('설문에 참여해 주셔서 감사합니다')
                    location.href = '/survey/survey_worker_list'
                    </script>"""
    else: 
        msg = """<script>
                    alert('실패')
                    history.go(-1)
                    </script>"""
    return HttpResponse(msg)
# -------------------------------------------------------------------------------------------
# 근로자 설문 전체 조회
def view_Survey_Worker_List(request) :
    
    df = survey.getSurveyWorkerList()
    
    # return HttpResponse(df.to_html())
    context = {"df" : df.to_html}
    
    return render(
        request,
        "surveyapp/survey_worker_list.html",
        context
    )
# -------------------------------------------------------------------------------------------
