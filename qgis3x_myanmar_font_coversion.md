# QGIS 3.X တွင်မြန်မာဖောင့် ပြောင်းခြင်း - Myanmar font conversions in QGIS 3.X #

Credit: Python-Module: Ko Thura Hlaing

 

Attribute table ထဲက Win font ကို Unicode ပြောင်းခြင်း၊ Zawgyi ကို Unicode ပြောင်းခြင်း Unicode/Zawgyi ကို Win font ပြောင်းခြင်းတို့ကို python-myanmar module သုံးပြီး QGIS 3 မှာပြုလုပ်နိုင်ကြောင်း မိတ်ဆက်ပေးခဲ့ပြီးဖြစ်ပါတယ်(link to read)။ ယခုတော့ python-module install နည်း  နဲ့ လိုအပ်တဲ့ ကျနော်ရေးထားတဲ့ conversion expression file ကို အသုံးပြုပုံကို ရေးသားဖော်ပြလိုက်ပါတယ်။
Python-Myanmar module ကို install လုပ်ခြင်း

 

1. Python path ရှာခြင်း

 

Python-Myanmar module ကို QGIS 3.x နဲ့ပါလာတဲ့ python3.7 ထဲကို install လုပ်ရပါမယ်။ အဲဒီအတွက် အရင်ဆုံး python.exe ဘယ်မှာရှိတယ်ဆိုတာ ရှာကြည့်ရပါမယ်။

 

File explorer ကနေရှာရပါမယ်။ ပုံမှန်ကတော့ QGIS install directory အောက်မှာ ရှိပါတယ်။ ကျနော့်စက်မှာဆိုရင် C:\Program Files\QGIS 3.4\apps\Python37 မှာရှိပါတယ်။]

 

 

 

 

 

ဒီ path လမ်းကြောင်းကို ကော်ပီကူးပါ။ အပေါ်ဖက်က Address bar ထဲမှာ select လုပ်ပြီး copy ကူးနိုင်ပါတယ်။

 

2. Command Prompt windows ဖြင့် module ထည့်ခြင်း

 

Windows search box တွင် cmd.exe ရိုက်ပါ။ ပေါ်လာသော cmd.exe icon ပေါ်တွင် right click နှိပ်ပြီး 

 

“Run as administrator” ကိုနှိပ်ပါ။ 

 

run cmd.exe as administrator

 

Command Prompt windows ပွင့်လာမည်..

 

Command prompt window

 

cd ဟုရိုက်ပါ။ space bar ရိုက်ပါ။ မောက်စ်တင်ပြီး right click paste လုပ်ပြီး python path ကိုထည့်ပါ။ Enter နှိပ်ပါ 

 

QGIS 3.4 ၏ Pthon37 folder သို့ပြောင်းခြင်း

 

python –m pip install python-myanmar ဟုရိုက်ပြီး Enter ခေါက်ပါ။ python-myanmar moduleကို အင်တာနက်မှ ရယူပြီး install လုပ်ပါမည်။ အားလုံးပြီးပါက နောက်ဆုံးတွင် Successfully installed python-myanmar…ဆိုပြီးစာပေါ်လာမည်။ 

 

python-myanmar module install လုပ်ခြင်း

 

Command prompt windows ကို ပိတ်ပါ။
QGIS Expression script file ကိုနေရာချထားခြင်း ..

 

https://github.com/knwin/qgis/raw/master/qgis3_myanmarfontconversion_functions.zip

 

ပေးထားသောလင့်မှ .zip ကို ဒေါင်းလုပ်ချပါ

 

Zip ကိုဖြည်ပြီး အထဲမှ qgis3_myanmarfontconversion_functions.py ဖိုင်ကို ၏ QGIS3 ၏ expression folder ထဲထည့်ပါ။ expression folder သည် အောက်ပါနေရာတွင်ရှိနိုင်သည်။]

 

C:\Users\[user name]\AppData\Roaming\QGIS\QGIS3\profiles\default\python\expressions

 

LeftCenterRightRemove

 

QGIS တွင် font conversion functions များကို အသုံးပြုခြင်း

 

QGIS 3.x ၏ Expression dialogbox ရှိ Function Editor တွင် qgis3_myanmarconversion_function selectလုပ်ပြီး ညာဖက်ရှိ “Save and Load Functions” button  ကိုနှိပ်ပြီး function များကို load လုပ်ရန်လိုပါမည်။

 

loading the function (if  not appeared automatically)

 

Expression dialogbox များ နှင့် Field Calculator တို့တွင် font conversion functions များကို FontConversion အမည် အောက်တွင် တွေ့ရမည်။ 

 

ready made functions seen under "FontConversion" in expression diaglogbox

 

Font conversion functions များ ရှင်းလင်းချက် - 

uni2win( )  - ယူနီကုဒ် မှ ဝင်းဖောင့် ပြောင်းခြင်း

uni2zg( ) - ယူနီကုဒ် မှ ဇော်ဂျီ ပြောင်းခြင်း

zg2uni( )  - ဇော်ဂျီ မှ ယူနီကုဒ် ပြောင်းခြင်း

zg2win( )  - ဇော်ဂျီ မှ ဝင်းဖောင့် ပြောင်းခြင်း

win2uni( ) - ဝင်းဖောင့် မှ ယူနီကုဒ် ပြောင်းခြင်း

win2zg( )  - ဝင်းဖောင့် မှ ဇော်ဂျီ ပြောင်းခြင်း

 

မြန်မာစာပါသော field သို့မဟုတ် string/text ကို ကွင်းစကွင်းပိတ်ထဲတွင်ထည့်ပေးရမည်။ အထက်ပါ function များကို label ထိုးရာတွင်လည်းကောင်း field calculator တွက်ချက်ရာတွင်လည်းကောင်း အသုံးပြုနိုင်သည်။

 

uni2win(T_NAME_M3)

 

Win font lable ဖြင့် မြင်ရပုံ

 

အထက်ပါနည်းသည် Attribute table တွင် font ပြောင်းပြီးသိမ်းခြင်းမဟုတ်ပဲ attribute column မှဖတ်ပြီး တိုက်ရိုက်ပြောင်းကာ label စာထိုးခြင်းဖြစ်သည်။

 

မှတ်ချက်။ python-myanmar version 1.5.1 တွင် Unicode/Zawgyi မှ Win font သို့ ပြောင်းရာတွင် ယူနီကုဒ် “ကျောက်တော်” “မော်လိုက်” စသည်တို့ကို ဝင်း စာလုံး ပြောင်းရာတွင် “ကျောက်တေ” “မေလိုက်” အဖြစ် ပြောင်းသည်ကိုတွေ့ရပါသည်။ ထိုအခက်အခဲကို Python-myanmar module ရေးသားသူ ကိုသူရလှိုင် ကို အကြောင်းကြားထားပါတယ်။ နောက် version တွင် အထက်ပါ conversion လွဲချော်မှု ပြင်ဆင်ပြီးဖြစ်ပါလိမ့်မည်။ 

 

လောလောဆယ် တွင် ကျနော် ပြင်ထားသော wininnwa.json file (https://bit.ly/2TZAtfq ) ကို ..\QGIS 3.4\apps\Python37\Lib\site-packages\myanmar\data အောက်ရှိ ဖိုင်နှင့်အစားထိုး သုံးပါက အထက်ပါ ပြသနာကို ဖြေရှင်း နိုင်ပါသည်။

 

သို့သော် ယူနီကုဒ် “အဓိဋ္ဌာန်” ကို ပြောင်းရာတွင် “အဓိဋ္ဌ-န်”ဟုဖြစ်နေသည် ကိစ္စ ကိုတော့ ကျနော့် ဖိုင် က မရှင်းနိုင်သေးပါ။

 

--------------------------------

 

2019 - 03 - 23, တပေါင်းလပြည့်ကျော် ၃ ရက်

 

[2020 - 05 - 18 တွင်ယူနီကုတ်ဖြင့်ပြောင်းရေးခဲ့ပါသည်။]

 

Kyaw Naing Win

 
copied from own post at https://www.facebook.com/notes/344775629947378/
