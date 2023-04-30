from django.shortcuts import render, redirect

# Create your views here.
from .forms import PlayerProfileForm, PlayerPitcherForm, PlayerFielderForm
from .models import Player
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
# トップ画面
def top(request):
    return render(request, "first_version/top.html")


# 選手作成画面
def create_player(request):
    if request.method == "POST":
        print("views.py:if request.method == 'POST':")
        print("----------------------------------------------------------")
        form_profile = PlayerProfileForm(request.POST)
        form_pitcher = PlayerPitcherForm(request.POST)
        form_fielder = PlayerFielderForm(request.POST)
        print("formプロフィール:",form_profile)
        # print("経歴:",form_profile["career"])
        # print("経歴:",form_profile.cleaned_data["career"])
        
        #POSTされたデータの内容をログに出力
        print(request.POST)
        
        
        # 3つのフォームの入力内容がすべて有効である場合、モデルへの保存処理を実行する。
        if form_profile.is_valid() and form_pitcher.is_valid() and form_fielder.is_valid():
            print("views.py:form_profile.is_valid() and form_pitcher.is_valid() and form_fielder.is_valid()")
            print("----------------------------------------------------------")
            player_model = form_profile.save(commit=False)
            # 投手能力
            player_model.pitching_form = form_pitcher.cleaned_data['pitching_form']
            # 野手能力
            player_model.contact = form_fielder.cleaned_data['contact']
            player_model.save()
            return redirect('top/')
        else:
            print("views.py:POST/else(ERROR)")
            print("----------------------------------------------------------")
            # print(form_profile.errors, form_pitcher.errors, form_fielder.errors)
            
    else:
        print("views.py:NOT POST ")
        form_profile = PlayerProfileForm()
        form_pitcher = PlayerPitcherForm()
        form_fielder = PlayerFielderForm()
    
    return render(request, "first_version/create_player.html", \
                    {"form_profile":form_profile ,"form_pitcher":form_pitcher,"form_fielder":form_fielder})


# class create_player(CreateView):
#     model = Player
#     form_class = PlayerProfileForm  # form_classはform_valid()メソッドで設定
#     template_name = 'first_version/create_player.html'
#     success_url = reverse_lazy('create_player')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.profile_form = PlayerProfileForm()
#         self.pitcher_form = PlayerPitcherForm()
#         self.fielder_form = PlayerFielderForm()
        
#     def get(self, request, *args, **kwargs):
#         self.object = None
#         context = self.get_context_data(**kwargs)
#         context['profile_form'] = self.profile_form
#         context['pitcher_form'] = self.pitcher_form
#         context['fielder_form'] = self.fielder_form
        
#         # return self.render_to_response(context)
#         # return render(request, "first_version/create_player.html",context=context)
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwrgs):
#         self.profile_form = PlayerProfileForm(request.POST)
#         self.pitcher_form = PlayerPitcherForm(request.POST)
#         self.fielder_form = PlayerFielderForm(request.POST)
#         # self.form_class = [self.profile_form, self.pitcher_form, self.fielder_form]
#         self.from_class = [self.profile_form, self.pitcher_form, self.fielder_form]
        
#         if all([form.is_valid() for form in self.from_class]):
#             return self.form_valid(self.from_class)
#         else:
#             return self.form_invalid(self.form_class)
    
#     #フォームの入力値が有効な場合の処理
#     def form_valid(self, form_class):
#         instance = form_class[0].save(commit=False)
#         instance.field1 = form_class[0].cleaned_data['field1']
#         instance.field2 = form_class[1].cleaned_data['field2']
#         instance.field3 = form_class[2].cleaned_data['field3']
#         instance.save() #ここでモデルへ保存。※レコードのINSERT処理。
#         return super().form_valid(form_class)


#     #フォームの入力値が無効な場合の処理
#     def form_invalid(self, form_class):
#         return self.render_to_response(self.get_context_data(form1=form_class[0], form2=form_class[1], form3=form_class[2]))

# class create_player(TemplateView):

#     #初期変数定義
#     def __init__(self):
#         print("in.views.py(__init__)")
#         self.params = {"Message":"情報を入力してください。",
#                         "form":forms.PlayerForm(),
#                         }

#     #GET時の処理を記載
#     def get(self,request):
#         print("in.views.py(GET)")
#         print("request.method:",request.method)
#         return render(request, "first_version/create_player.html",context=self.params)


#     #POST時の処理を記載
#     def post(self,request):
#         print("in.views.py(POST)")
#         if request.method == "POST":
#             print("in:request.method == POST")
    
#             self.params["form"] = forms.Player_Form(request.POST)
            
#             #フォーム入力が有効な場合
#             if self.params["form"].is_valid():
#                 print("in:フォームが有効")
#                 #入力項目をデータベースに保存
#                 self.params["form"].save(commit=True)
#                 self.params["Message"] = "入力情報が送信されました。"
#                 return render(request, "first_version/top.html")
#             else:
#                 print("in:(else)フォームが無効です。")
#         else:
#             render(request, "first_version/create_player.html", context=self.params)
            
#         return render(request, "first_version/create_player.html", context=self.params)



