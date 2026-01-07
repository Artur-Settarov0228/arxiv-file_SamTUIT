from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.utils import timezone

from apps.login.models import Registration
from .models import Talabalar

from django.core.paginator import Paginator



class TalabalarView(View):
    def get(self, request:HttpRequest) -> HttpResponse:
        user_id = request.session.get("user_id")

        if not user_id:
            return HttpResponse("Login topilmadi", status=401)

        if not Registration.objects.filter(id=user_id).exists():
            return HttpResponse("Foydalanuvchi topilmadi", status=403)

        talabalar = Talabalar.objects.all().order_by("-id")

        full_name = request.GET.get("full_name")
        if full_name:
            talabalar = talabalar.filter(full_name__icontains=full_name)

        faculty = request.GET.get("faculty")
        if faculty:
            talabalar = talabalar.filter(faculty=faculty)

        admission_year = request.GET.get("admission_year")
        if admission_year and admission_year.isdigit():
            talabalar = talabalar.filter(admission_year=admission_year)

        group = request.GET.get("group")
        if group:
            talabalar = talabalar.filter(group=group)

        paginator = Paginator(talabalar, 100)  # 🔥 100 tadan
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, "ftot/index.html", {
            "talabalar": page_obj,
            "page_obj": page_obj,
            "filters": request.GET
        })

    



class AddTalaba(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        user_id = request.session.get("user_id")

        if not user_id:
            return HttpResponse("Login topilmadi", status=401)

        if not Registration.objects.filter(id=user_id).exists():
            return HttpResponse("Foydalanuvchi topilmadi", status=403)

        return render(request, "ftot/talaba_qoshish.html")


    def post(self, request: HttpRequest) -> HttpResponse:
        user_id = request.session.get("user_id")

        if not user_id:
            return HttpResponse("Login topilmadi", status=401)

        if not Registration.objects.filter(id=user_id).exists():
            return HttpResponse("Foydalanuvchi topilmadi", status=403)

        full_name = request.POST.get("full_name")
        pasport = request.POST.get("passport")
        qabul_yili = request.POST.get("admission_year")
        faculty = request.POST.get("faculty")
        group = request.POST.get("group")
        status = request.POST.get("status")

        
        if not full_name:
            return HttpResponse("F.I.Sh kiritilishi shart", status=400)

        if len(full_name) > 300:
            return HttpResponse("F.I.Sh 300 belgidan oshmasligi kerak", status=400)

        
        if not pasport:
            return HttpResponse("Passport kiritilishi shart", status=400)
        if Talabalar.objects.filter(pasport=pasport).exists():
            return HttpResponse("Bu odam avval kiritilgan", status= 400)

        if len(pasport) > 9:
            return HttpResponse("Passport 9 belgidan oshmasligi kerak", status=400)

        
        if not qabul_yili:
            return HttpResponse("Qabul yili kiritilishi shart", status=400)

        if not qabul_yili.isdigit():
            return HttpResponse("Qabul yili raqam bo‘lishi kerak", status=400)

        qabul_yili = int(qabul_yili)

        if qabul_yili < 2005:
            return HttpResponse("Qabul yili 2005 dan kichik bo‘lishi mumkin emas", status=400)

        if qabul_yili > timezone.now().year:
            return HttpResponse("Kelajakdagi yilni kiritish mumkin emas", status=400)

        
        if not faculty:
            return HttpResponse("Fakultet tanlanmadi", status=400)

        if faculty not in dict(Talabalar.CHOISE_FACULTY):
            return HttpResponse("Noto‘g‘ri fakultet tanlandi", status=400)

       
        if not group:
            return HttpResponse("Guruh kiritilishi shart", status=400)

        if len(group) > 128:
            return HttpResponse("Guruh nomi 128 belgidan oshmasligi kerak", status=400)

      
        if not status:
            return HttpResponse("Status tanlanmadi", status=400)

        if status not in dict(Talabalar.CHOISE_STATUS):
            return HttpResponse("Noto‘g‘ri status tanlandi", status=400)

       
        Talabalar.objects.create(
            full_name=full_name,
            pasport=pasport,
            qabul_yili=qabul_yili,
            faculty=faculty,
            group=group,
            status=status
        )

        return redirect("talabalar:talabalar")
    
class DeleteTalaba(View):
    def post(self, request: HttpRequest, talaba_id: int)-> HttpResponse:
        user_id = request.session.get("user_id")

        user_id = request.session.get("user_id")

        if not user_id:
            return HttpResponse("Login topilmadi", status=401)

        if not Registration.objects.filter(id=user_id).exists():
            return HttpResponse("Foydalanuvchi topilmadi", status=403)

        talaba = Talabalar.objects.filter(id = talaba_id).first()
        if not talaba:
            return HttpResponse("Talaba topilmadi", status=404)
        
        talaba.delete()
        return redirect("talabalar:talabalar")
    

class TalabaUpdateView(View):

    def get(self, request: HttpRequest, talaba_id: int) -> HttpResponse:
        user_id = request.session.get("user_id")

        if not user_id:
            return HttpResponse("Login topilmadi", status=401)

        if not Registration.objects.filter(id=user_id).exists():
            return HttpResponse("Foydalanuvchi topilmadi", status=403)

        talaba = Talabalar.objects.filter(id=talaba_id).first()
        if not talaba:
            return HttpResponse("Talaba topilmadi", status=404)

        return render(request, "ftot/talaba_tahrirlash.html", {
            "talaba": talaba,
            "faculties": Talabalar.CHOISE_FACULTY,
            "statuses": Talabalar.CHOISE_STATUS,
        })

    def post(self, request: HttpRequest, talaba_id: int) -> HttpResponse:
        user_id = request.session.get("user_id")

        if not user_id:
            return HttpResponse("Login topilmadi", status=401)

        if not Registration.objects.filter(id=user_id).exists():
            return HttpResponse("Foydalanuvchi topilmadi", status=403)

        talaba = Talabalar.objects.filter(id=talaba_id).first()
        if not talaba:
            return HttpResponse("Talaba topilmadi", status=404)

        full_name = request.POST.get("full_name", "").strip()
        pasport = request.POST.get("pasport", "").strip()
        qabul_yili = request.POST.get("qabul_yili", "").strip()
        faculty = request.POST.get("faculty")
        group_name = request.POST.get("group", "").strip()
        status = request.POST.get("status")

        if not full_name:
            return HttpResponse("F.I.Sh kiritilishi shart", status=400)

        if len(full_name) > 300:
            return HttpResponse("F.I.Sh 300 belgidan oshmasligi kerak", status=400)

        if len(pasport) > 9:
            return HttpResponse("Passport 9 belgidan oshmasligi kerak", status=400)

        if not qabul_yili.isdigit():
            return HttpResponse("Qabul yili raqam bo‘lishi kerak", status=400)

        qabul_yili = int(qabul_yili)

        if qabul_yili < 2005 or qabul_yili > timezone.now().year:
            return HttpResponse("Qabul yili noto‘g‘ri", status=400)

        if faculty not in dict(Talabalar.CHOISE_FACULTY):
            return HttpResponse("Noto‘g‘ri fakultet", status=400)

        if status not in dict(Talabalar.CHOISE_STATUS):
            return HttpResponse("Noto‘g‘ri status", status=400)

        talaba.full_name = full_name
        talaba.pasport = pasport
        talaba.qabul_yili = qabul_yili
        talaba.faculty = faculty
        talaba.group = group_name
        talaba.status = status
        talaba.save()

        return redirect("talabalar:talabalar")


        
    



