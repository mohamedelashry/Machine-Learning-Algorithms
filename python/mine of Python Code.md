Python Code
 مبادئ هامة 
* زرار F5 ينفذ الأمر  او الضغط  علي     
* لو تم وضع # وتم ضغط Ctrl +1 لجعل الكلام كومنت , بلون رمادي
* المسافة أول السطر غير مسموح بها , إلا في الدوال المتداخلة
* المسافة وسط السطر لا بأس بها
* الحروف الـ capital تفرق في المعنى عن الـ small والأصل أن الجميع small
* وجود المثلث البرتقالي , يدل على وجود ملاحظة أو خطأ معين في الكود في كتابته ,   
احيانا تكون ملاحظة عابرة  ,او خطأ كبير
* او ظهر هذا السطر وحده  ,فالبرنامج لازال يعمل , لو ظهر ثم الناتج فقد انتهي البرنامج
  

   * أمر print يظهر الناتج 
   * يشترط وضع أقواس قبل و بعد الناتج     
   * يمكن وضع قيم حقيقية أو متغيرات
   * اذا تم وضع متغير , فيتم استخدام أقواس فقط
   * اذا تم وضع قيمة وكانت رقم او بوليان , فيتم استخدام أقواس فقط
   * اذا تم وضع قيمة نص string فيجب وضع أقواس و سنجل كوتيشن او دبل كوتيشن
   * يمكن وضع اكثر من قيمة في الأقواس , وتفصلهم كوما , 




المتغيرات
   * هي رموز تحتوي علي قيم , بأنواع مختلفة
   * تستخدم لتعيين القيم , او القيام بعمليات عليها   , او عرضها , او دمجها معا , وهكذا
   * لتعريف اي متغير , مش بتكتب نوعه , بس تقول a=5 فيحدد نوعه و يحفظ القيمة 
   * أمر type   بعدها المتغير يجيب نوعه
   * ممكن تعمل كذا تعريف في نفس الوقت 
a,s,f,g,u = 4,5.6,8j,4,5
yourname , yourcountry = ‘ahmed’ , ‘Algeria’
thiscase  = True
name , country , age , case = 'ahmed' , 'Algeria' , 22 , True
   * انواعها
int , str , float , bool , list , tuple , set , dict , complex
   * يمكن التحويل من انواع لانواع (خاصة بين الـ  str  , int , float )
a = “5”
b = int(a)
c = float(a)
d = 7
e = str(d)
f = complex(b,d)
   * بالنسبة للرقم المركب , ممكن نستدعي الرقم الحقيقي والتخيلي فيه
c.real
c.imag
   * المتغير الثنائي (بيناري) 
bin(50)


   *  ممكن لدالة الـ bool ان تقرا رقم أو نص , واذا كان فارغ أو صفر يكون false
c=bool(5.3)
d=bool('ahmed')
e=bool(0)
e=bool('')
  العمليات الرياضية


   * الجمع
x + y
   * الطرح
x - y
   * الضرب
x * y
   * القسمة
x / y
   * القسمة مع ارقام صحيحة
x // y
   * باقي القسمة
x % y
   * الأس
x ** y
   * ھل تساویھا ؟
x == y
   * اكبر من
x > y
   * اكبر من او يساوي
x >= y
   * اصغر من
x < y
   * اصغر من او یساوي
x <= y
   * هل قيمة a اكبر من 15 و أصغر من 30
15 < a < 30
   * القيمة المطلقة
abs(x)
   * تحویل لرقم صحیح (مش تقریب)
int(x)
   * تحویلھ لرقم مركب
complex(5,4)
   * رقمین حاصل القسمة , وباقي القسمة
divmod(x,y)
   * الأس
pow(x,y)


=========================================


________________


 مكتبة Math


   * المكتبة :
   * مجموعة من الدوال و الأوامر و الخواص , مدموجة معا في ملف , بحیث یمكنك استخدامھا بسھولة بمجرد
استدعائھا او استیرادھا
   * بشكل دائم یتم تكون مكتبات جدیدة , او تعدیل مكتبات قدیمة , وعلي المتخصص في تعلیم الآلة مواكبة ھذا
أولا بأول


      * يتم استيراد أي مكتبة بأكثر من شكل
      * یتم ذكر اسم المكتبة في كل دالة
import libraryname
      * یتم ذكر الاختصار في كل دالة
import libraryname as ab
      * تصلح فقط لدالة واحدة
from libraryname import function
      * یتم ذكر الدالة فقط دون مقدمة
from libraryname import *
      * مكتبة Math :
      * یتم استیرادھا بالأمر
import math as m
      * مضروب
m.factorial(x)
      * اكسبونینشیال
m.exp(x)
      * دالة لن ln
m.log()
      * لوج لأساس معین
m.log(x,y)
      * ولوج للأساس 10
m.log10(x)
      * الجذر التربیعي
m.sqrt(x)
      * التحویل من degrees لـ radians
m.degrees(x)
      * التحويل من radians لـ   degrees 
m.radians(x)
      * الدوال المثلثية
m.sin(x)     m.cos(x)      m.tan(x)
      * الدوال المثلثیة العكسیة
m.asin(x)      m.acos(x)      m.atan(x)
      * الدوال المثلثية للقطع الزائد
m.sinh(x)      m.cosh(x)      m.tanh(x)
      * الدوال المثلثیة العكسیة للقطع الزائد
m.asinh(x)      m.acosh(x)      m.atanh(x)
      * الثوابت الھامة
m.pi       m.e        m.tau       m.inf
      * نسخ الإشارة
m.copysign(a,b)
      * التقریب للأعلي
m.ceil(x)
      * التقریب للأقل
m.floor(x)
      * دالة قیمة الخطأ
m.erf(x)
      * دالة الجاما
m.gamma(x)


=========================================


________________


 النصوص String  1


      * یتم تعريفها بالطریقة العادیة مع السنجل او الدبل كوتیشن
a = "sweet home alabama"
a = 'sweet home alabama'


      * استدعاء حرف معین (اضف رقما للرقم الموجود)
a[0] , a[3] , a[7]
      * حرف من النھایة
a[-1] , a[-3] , a[-7]
      * تكرار 3 مرات
a*3
      * من الحرف الخامس للثاني عشر
a[4:12]
      * من البدایة للثاني عشر
a[:12]
      * من الخامس للنھایة
a[4:]
      * الجملة كلھا
a[:]
=========================================


________________


 النصوص String  2


      * من الخامس لثاني عشر بخطوة 2
a[4:12:2]
      * من البدایة للسابع , خطوة 3
a[:7:3]
      * من التاسع للنھایة بخطوة 4
a[8::4]
      * الجملة كلھا بخطوة 2
a[::2]
      * خد الحروف من الاخر لغاية رابع حرف من ورا , و بالعكس
a[-1:4:-1]
      * كل الحروف بعكس الترتيب
a[::-1]
      * ھیجبلك   list فیھا كل الحروف لوحدھا , بما فیھا المسافة
list(a)
      * نفس الامر السابق , ولكن مع ترتیب
sorted(list(a))
      * ھیفصصھا  بس مش ھیكرر , یعني  a لو متكررة 5  مرات ھیجیبھا مرة واحدة
set(x)
      * ھیفصصھا بناء على كلمات مش حروف
a.split()
      * و ممكن السبلیت یكون بناء علي رقم او رمز معین , بحیث تكون ھي الفواصل
x = "12354785669854412503665"
x.split("5")


      * لو التیكست مكتوب علي كذا سطر , كل سطر فیھم جملة
a.splitlines()


=========================================


________________


 النصوص String  3




      * ھیمسك أول كلمة and  یشوفھا , ويعمل اللي قبلھا جملة ,وھي جملة , واللي بعدھا جملة
a.partition(‘and’)
      * نفس الفكرة , بس ھیجیب اول كلمة and  من الیمین
a.rpartition(‘and’)
      * یبحث عن الكلمة المطلوبة , و یجیب بدایتھا أي حرف , ولو موجودة اكتر من مرة یجیب الاولي بس
a=”he is a good man but he is liar”
a.find(‘he’)
      * نفس الدالة ,بس بيبدأ البحث من الیمین, لكن الرقم بيكون ترتيب الحروف من الشمال
a.rfind(‘he’)
      * ولو عايز تعرف الحرف أو الكلمة المعينة مكانھا فین في الجملة , استخدم اندیكس وھیجیبلك جت  امتي , ولو ھي اتكررت اكتر من مره ھیجبلك اول واحدة
a.index('e')
      * والفارق بینھم ان لو الكلمة او الحرف مش موجود , ف find ھتجیب سالب واحد بینما index ھتجیب error
      * لو عایز ابدال حروف معینة لحرف تاني , استخدام ریپلیس
a.replace ('f','i')
      * و ممكن في كلمة كاملة , لاحظ أن السترنج لا یتغیر , هو یظهر النتیجة و انت احفظھا
a.replace ('sweet','ugly')
      * حرف m اتكرر كام مرة في الجملة
a.count(‘m’)
      * یجعل اول حرف في الجملة كابيتال والباقي سمول
a.capitalize()
      * یجعل اول حرف في كل كلمة كابیتال
a.title()
      * یجعل كل الحروف کاپیتال
a.upper()
      * عكس , أى حرف کاپیتال یجعلها سمول و العكس
a.swapcase()
      * یعمل مسافات یمین و شمال الكلام , بحیث یکون مجموع السطر بالمسافات بالكلام 30 خطوة
a.center(30)


=========================================


________________


 النصوص String  4




      * بعد الكلام اعمل مسافات علي یمینھ , بحیث یكون المجموع 30
a.ljust(30)
      * قبل الكلام اعمل مسافات علي شمالها  بحیث یكون المجموع 30
a.rjust(30)
      * لما اعمل حرف معین , یعنی بدل ما یملاه مسافات يملاه الحرف ده
a.rjust(30 ,'*')
      * ده بيملي اصفار شمال السترنج , زي rjust  بس اصفار بس
'435'.zfill(10)
      * ھل كل الحروف المستخدمة الفابیتیك , لو فیھا رموز زي  (+@%)  یقول  false  غیر كدة  true
a.isalpha()
      * معناھا حذف اي مسافات قبل أو بعد الكلام
a.strip()
      * حذف اي مسافة من الیمین بس
a.rstrip()
      * حذف اي مسافة من الشمال بس
a.lstrip()
      * ولو هحط حرف معین داخل  strip  ھیتعامل معاه علي انها المسافة فی حذفها , يعني ده هيكون  abc
x = "**abc**"
print(x.strip('*'))


 النصوص String  5




      * بعض الحروف يكون لیھا تأثیر مثل باك سلاش /
      * یعني لو كتبتها و وراها  n  ساعتها بیقطع الکلام و یعمله سطر تاني
a = "sweet \n home alabama"
      * ولو انا عایز عن عمد  n\  تظهر من غیر ما یحصل تأثيرها , أعمل r  قبل النص
a= r'C:\some\name'
      * لو كتبت بعدھا  t  ھیعمل مسافة , یعنی تاب 
a = "sweet \t home alabama"
      * لو عایز اكتب اكتر من سطر , اعمل تلاتة دبل كوتيشن """ في أول الكلام وتلاتة في الاخر 
a = """ sweet home
           alabama """
      * معناھا اطبع القیمة في نفس السطر دون النزول لسطر جدید
a , b = 'aaaa' , 'bbbbb'
print(a,end='')
print(b)


      * من الحروف الغریبة برضه  %
      * تستخدم عشان احشر متغیر جوة الكلام , فلو عایز اكتب سوییت هوم , بعدها متغیر معین ھیتم تحدیده  , وممكن یكون المستخدم ھیدخله , اكتب % بعدھا  s و بعد ما تخلص ال " اكتب % بعدھا المتغیر
      * وطبعا لازم اكون اعرف ايه ھي ال aaa قبل كدة
aaa = “alabama”
a = "sweet home %s" %aaa        


      * ولو عایز احط رقم ھو المتغیر , أعمل d دسیمال مكان s سترنج
bbb = 136
a = "sweet home %d" %bbb
      * و ممكن یتم دمجھم معا
a = "sweet %s %d" % ( aaa , bbb)
      * معناھا اكتب كلمة numbers  بعدھا اكتب الدیسیمال رقم 7 , بس على مسافة 5 فراغات
a = “numbers %5d“ %7
      * معناھا برضھ اكتب 7 بعد 5 فراغات , بس يكون المسافات دیھ اصفار , يعني كدة 000007
a = “numbers %05d“ %7
      * وممكن الاضافات دیھ تكون في اول او وسط الكلام
a="%s has %03d qoute types." %("Python", 2)
      * حيل لجعل الكوتيشن ' تكون في النص
      * لجعل الكوتیشین جزء من الكلام ممكن نعمل اي من ھذه الحیل
'doesn\'t'
"doesn't"
' "Yes," he said.'
"\"Yes,\" he said."
'"Isn\'t," she said.'


=========================================


________________


 النصوص String  6


      * هل كل السترنج ارقام (ترو او فولس)
      * هل كل السترنج ارقام (ترو او فولس)
a.isdigit()
      * هل كل السترنج حروف كابيتال
a.isupper() 
      * هل كله سمول
a.islower() 
      * هل اول حرف بس كابيتال
a.istitle()
      * هل آخر كلمة في a هي كلمة كذا (true or false)
a.endswith(‘alabama’)
      * هل أول كلمة هي كلمة كذا  (true or false)
a.startswith(‘sweet’)
      * يقوم أمر (جوين) باضافة ما قبله لما بعده
a = ', '.join( ('one', 'two', 'three') )
      * عمل مسافات بين كل حرف و التاني
'  '.join('hello')
      * هنا يقوم بإضافة 100 رقم عشوائي , كل واحد يتراوح من 0 ل 9
' '.join([str(i) for i in np.random.randint(10, size=100)])


=========================================


  النصوص String  7


      * هنا مجرد  هيستبدل بالأقواس قيمة باي
"The value of pi is {}".format(np.pi)
      * نستبدل قيمتين (سواء نص او رقم)
'{0} and {1}'.format('red', 'blue')
      * ولو عملت أرقام مختلفة , هيمشي علي الارقام , يعني هيبدا بالكلمة الثانية
'{1} and {0}'.format('red', 'blue')
      * ممكن تكون بـ keywords
"First: {first}. Last: {last}.".format(last='Z', first='A')
      * معناها ان اعمل فورمات للباي , بحيث تكون float وهات 3 أرقام بعد العلامة العشرية
"pi = {0:.3f}".format(np.pi)
      * ممكن اكتر من حاجة  , هيعمل Im 20 years old
'{:s} {:d} years old'.format('Im',20)
      * ده بوسطن الكلام المعطي بين الرمزين
'|' + '{:^51}'.format('Hello') + '|'
      * يعمل اسهم بين الكلام الاول والثاني
'{0:10} ==> {1:10d}'.format('name', 56322)








      * من الادوات الخاصة بالبحث في الكلمات اداة compile في مكتبة re
      * انا قلتله ان هات اي كلمة فيها @ ,وهات الكلمة اللي قبلها , وامشي لغاية الدوت . , وبعدها هات 3 حروف من a-z
import re
email = re.compile('\w+@\w+\.[a-z]{1}')
text = "To email Guido, try guido@python.org or guido@google.com "
print(email.findall(text))
      * وكدة هيجيب كل جزء في الايميل لوحده 
import re
text = "To email Guido, try guido@python.org or guido@google.com "
email3=re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
print(email3.findall(text))
      * كدة هيعمل dictionary
mport re
text = "To email Guido, try guido@python.org or guido@google.com "
email4=re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+).(?P<suffix>[a-z]{3})')
match=email4.match('guido@python.org')
print(match.groupdict())


=========================================


________________


 التعامل مع الملفات 
Handling with Files


      * أمر open يقوم بفتح الملف و حفظه في مكان معين
f= open('D:\\1\\1.txt','w')
      * كتابة سطر معين
f.write('write this line in the file')
      * اغلاق الملف
f.close()
      * فتح ملف للإضافة و ليس لمسح القديم 
f= open('D:\\1\\1.txt','a')
      * لفتح ملف وقراءته
f= open('D:\\1\\1.txt','r')
      * لقراءة السطور و إظهارها
for a in f:
    print(a)
      * للتعامل مع ملف csv
outfile = open('D:\\1\\5.csv', 'w')
outfile.write('a')
outfile.close()


      * للتعامل مع ملف اكسيل
outfile = open('D:\\1\\5.xls', 'w')
outfile.write('a')
outfile.close()
      * للقراءة من الاكسيل
outfile = open('D:\\1\\5.xls', 'r')
for g in outfile:
    print(g)
      * مكتبة os  وهنا هيجيبلك المكان الديفولت اللي بيتعامل معاه
import os
a=os.getcwd()
print(a)
      * ينشئ فولدر في مكان معين , و كلمة ترو عشان يعمل overwrite لو موجود
os.makedirs('D:\\1\\00' , exist_ok = True)
      * يفحص الفولدر او الملف موجود ولا لا
a = os.path.exists('D:\\00')
a = os.path.exists('D:\\1\\0.txt')
      * مكتبة شاتل , لنسخ ونقل الملفات
import shutil as sh
      * نسخ ملف من مكان لمكان , ويجب أن يكون الفولدر موجود
sh.copyfile( 'D:\\1\\1.txt', 'D:\\1\\00\\0.txt')
      * نقل فولدر لما فيه
sh.copytree('D:\\1\\00' , 'D:\\1\\33')
      * نقل ملف او فولدر
sh.move('D:\\1\\1.txt' , 'D:\\1\\33\\55.txt') 






  القوائم  Lists


      * ما هي : 
مجموعة من البيانات التي يتم تخزينها بترتيب محدد
قد يكون بها أنواع مختلفة من البيانات مثل : 
      * نصوص String
      * أرقام Integer , Float , Complex
      * بوليان Boolean
      * لا يستلزم تحديد نوعها بشكل مسبق
      * يمكن دمج اكثر من نوع معا في القائمة
      * يمكن للقائمة أن يتم تعديلها لاحقا , ويتم إضافة بيانات 
      * الأنواع المختلفة : 
      * القائمة List 
      * يتم التعامل معها بالأقواس  [ ]
      * تشمل أنواع مختلفة من البيانات , ويمكن تعديلها لاحقا
      * الصفوف tuple 
      * يتم التعامل معها بالأقواس  ( )
      * تشمل  بيانات غير قابلة للتغيير
      * المجموعة Set   
      * يتم التعامل معها بالأقواس   {  }  
      * لا تقبل التكرار
      * القاموس  Dictionary
      * يكون شكلها {'a':1, 'b':2, 'c':3} 
      * تشمل على  دليل و مفاتيح و قيم


      * يتم تعريفها عن طريق اني اكتب اسمها و اعمل أقواس مربعة فاضية
L = [ ]
      * و اضيف عليها ارقام بالطريقة ديه
s = [1,2,3,6,9,8,7]
      * ممكن القائمة تحتوي على عناصر من أنواع مختلفة
s = [ “sam” , 5 , 3.2 , 5+2j ] 
      * ممكن يكون فيه ليست جوة الليست
s = [ 2 , 3, [ 4 , 5 ] ]
      * لما بدخل تيكست و احولها ليست , بتكون عناصرها كل حرف من حروفها حتى المسافة
x = list("love apple")
      * كده هاعمل كل عنصر من العناصر ديه a,b,c تساوي كل حرف من حروف الكلمة يعني كل عنصر من عناصر ليست , بشرط يكونو نفس العدد بالظبط
a,b,c,d,e,f,g = x
      * و ممكن اكتب عنصر محدد هيكتبلك قيمته , ولاحظ ان اول رقم دايما بيكون ترتيبه صفر , فده معناه العنصر الخامس
s[4]
      * ولو انا عايز اعمل ليست عبارة عن عدد من عناصر ليست ديه , فاعملها كده  , وده معناه ان ليست واي هي ليست عبارة عن العناصر من العنصر 5 للعنصر التاسع في مصفوفة تي , لاحظ انه بيبدا بالرقم الاول , وينتهي بالرقم قبل الاخير
y = t[5:10]
      * و ممكن اقوله هات كل العناصر لغاية العنصر السادس , اسيب الخانة الاولى فاضية
y = t[:7]
      * معناها هات العناصر من الاول , لكن تجاهل اخر 3 عناصر من الاخر
y = t[:-3]


      * او هات من العنصر السابع لغاية آخر عنصر 
y = t[7:]
      * ولو عايزها كلها تكتب كده 
y = t[:]
      * يتم عمل تعديل في الليست
t[7]=5 
      * بمسح من العنصر الثالث للخامس
t[2:5]=[]


      * بامسحها كلها
t[:]=[]
      * ليست جوة الليست
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x= [['a', 'b', 'c'], [1, 2, 3]]


      * معناها العنصر الأول فيها , يعني الستة الأول ['a', 'b', 'c'] 
x[0]
      * تستخدم لما يكون عندي ليست جوة ليست , فكدة يروح للعنصر السادس , هيلاقيه ليست , يجيب منه العنصر الثاني
x[5][1]
      * ولو عايز امسح قيمة فيهم اعمل ديل واكتب اسم الليست و الاندكيس  
del t[4]
      * ولو عايز امسح كل الليست اكتب كدة
del y
      * يعني امسح اي عنصر اسمه b
y.remove(“b”)
      * ويمكن تضم عناصر ليستين على بعض
ss= y + t
      * ولو عملت ضرب الستة في رقم , ساعتها هتتكرر العناصر خمس مرات
y*5
      * لو عايز مثلا اعمل لستة فيها الف رقم انتجر
x = [0] * 1000
      * لو عايز اعمل لستة فيها الف رقم فلوت
x = [0.0] * 1000
      * لو عايز مثلا اعمل لستة فيها الف سترينج
x = [’s’] * 1000
      * كده هاعمل عشر لستات , كل واحدة 8 عناصر , وكأنها مصفوفة 8 في 10
x = [[0]*8] *10
      * ولو عايز اعرف هما كام عنصر
len (y)
      * مجموع قيمتها لو ارقام , ولو العناصر فيها حاجة مش ارقام مش هتنفع
sum(y)
      *  اقل او اكبر قيمة فيها ولو استخدمناها في السترنج , هيتعامل ان حروف a, b , c هي الاصغر  و ان x , y , z اكبر
max(y)
min(y)
      * برتبهم من الصغير للكبير , سواء ارقام او حروف
sorted(y)
      * لو عملت أمر sort وقتها هيتم ترتيب القائمة نفسها
y.sort()
      * بيرتب من الكبير للصغير
sorted(y,reverse = True)
      * لو عايز ارتب بناء على العنصر التانى مش الاول , يعني ديه
 [('At', 85), ('Br', 35), ('Cl', 17), ('F', 9), ('I', 53)]
      * هتكون كدة 
[('F', 9), ('Cl', 17), ('Br', 35), ('I', 53), ('At', 85)]
sorted(y, key=lambda e: e[1])
      * بناء على العنصر الرابع , ترتيب عكسي (الكبير للصغير)
sorted(y,reverse = True, key=lambda e: e[3])
      * هيفصصها بناء على كلمات مش حروف
s.split()
      * لو عايز اعرف هل فيه عنصر معين موجود في الليست ولا لا , اكتب العنصر بعدها أن بعدها ليست , وترجعلي ب true أو false
7 in y
      * هنزود على القائمة y كل عناصر x
y.extend(x)
      *  تضيف قيمة ليستة
y.append (555)
      * لو عايز اضيف عنصر في مكان معين في الليست ( مش في الاخر ) يبقي انسرت , اكتب الاول رقم الانديكس المطلوب , وبعدها اكتب القيمة 
y.insert(5,999999)        
      * لو عايز اشوف العنصر الفلاني اتكرر كام مرة استخدم اكاونت
y.count (555)
      * لو عايز اعرف العنصر الفلاني رقمه كام  : انديكس
y.index (5)
      * ممكن اعمل عكس لترتيب العناصر , الاخر اول والاول آخر 
x.reverse()
      * يحذف آخر عنصر في اللستة
y.pop()
      * حذف  العنصر الخامس في اللستة
y.pop(4)
      * دالة اسمها الرينج , ودية بتستخدم لعمل أرقام من صفر قبل الرقم المعطى واحد
N = range(20)
      * عشان احولها للستة , استخدم ده
M = list(range(20))
      * ولو عايز رينج من رقم لرقم  (ناقص واحد)تعمله كدة , هتلاقي ان الارقام اتعرضت من 2 لـ 19
N = range(2,20)
      * ولو عايز يكون فيه خطوة اعمل كدة (يعني 2 , 5 , 8 . . . )
N = range(2,20,3)         
      * و ممكن يكون تكوين ليست , بالشكل ده , اني اقوله عايز تكعيب كل الارقام من صفر لـ 11
y = [ x**3 for x in range(12)]
y = list(map(lambda x : x**3 , range(12)))
      * احد الطرق التي يمكن بها انشاء ليست
ss = [-5 + i*0.5 for i in range(20)]
      * و ممكن اكونها بالشكل ده , بحيث هتساوي [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
f = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


      * لو عايز اعمل لستة من بعدين , عدد الصفوف 7 و عدد العواميد 5
L = [[0 for i in range(5)] for j in range(7)]
      * لما باعمل iter قبل أي ليست , كل ما انده لها بكلمة next , هيجيب القيمة اللي بعدها
I = iter([2, 4, 6, 8, 10])
print(next(I))
print(next(I))
      * نفس الكلام لو iter مع range
I = iter(range(20))
      * لو تم مساواة ليست وليست , فكل قيمها هتكون نفسها
x = [1,2]
y = x
      * لو تم تعديل قيم معينة في الليست (حتى لو كلها) فالستة الجديدة y هيتم التعديل فيها , حتى لو مقلتش تاني ان y=x
x = [1,2]
y = x
x[0] = 5
x[1] = 15
      * لكن لو تم تعديل ليست الأولى كلها برقم تانية , بالليست اللي كانت بتساويها y مش هتتعدل , وهتفضل بنفس قيمها القديمة 
x = [1,2]
y = x
x = [6,9]
      * و من الأدوات القوية مع اليست او التابل , اداة enumerate  , واللي بتخليك تقطع اي سترنج  ,او تمسك أي لست أو تبل
, عشان تاخد العناصر فيها و ترقمها
      * الenumerate بتاخد قيمتين , الأولى العداد , والتانية العنصر نفسه
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
         * ولو انا اديته رقم معين , هيبدا بيه , بحيث اول عنصر هيكون رقمه 4
enumerate(items, 4)
         * اداة تانية في نفس السياق هي الـ zip و اللي بتجمع عناصر اتنين ليست , بحيث تربط بين واحدة من هنا ومن هناك
         * يعني هنا هيتم الجمع بين العنصر الأول هنا , والاول هنا , بعدها التاني هنا , والتاني هنا و هكذا 
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print (a, b)
         * من الأدوات المستخدمة في الترتيب itemgetter والتي يتم استدعائها من operator
from operator import itemgetter
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10),]
         * كدة هيرتب القيم , تبعا للعنصر الثالث , وهو السن
print(sorted(student_tuples, key=itemgetter(2)))
         * كدة هيرتبهم تبعا للعنصر الثاني (الحروف) ولو تساوت قيمتين , هيرتبهم تبعا للعنصر الثالث (السن)
print(sorted(student_tuples, key=itemgetter(1,2)))
         * من نفس المكتبة ممكن نستخدم اداة methodcaller
         * معناها رتب الكلمات ديه تبعا لعدد حرف a فيها 
messages = ['critical!!!', 'hurry!', 'bla bla', 'alabama']
print sorted(messages, key=methodcaller( 'count', 'a'))






________________


الصفوف , المجموعات , القاموس




         * تكتب الـ Tuple بالقوس الدائري , هي لا تسمح بالتغيير
L =(2,5,6,3,2)
         * إعادة الترتيب
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
a = sorted(student_tuples, key=lambda student: student[2])


         * المجموعات Set  بالقوس المعووج , لا تقبل التكرار
D = {1,1,2,2,6,8,4,6,3}
         * و ممكن تتكتب بنفس الشروط الواردة في القوائم 
a ={n**2 for n in range(12)}
         * یجیب العناصر الاقل فقط
a or b
         * یجیب العناصر الاكثر فقط
a and b
         * جميع العناصر ھنا و ھنا
a | b
a.union(b)
b.union(a)






         * العناصر المشتركة فقط
a & b
a.intersection(b)


         * جميع العناصر عدا المشتركة
a ^ b
a.symmetric_difference(b)
b.symmetric_difference(a)


         * E بعد حذف عناصر D عناصر 
a - b
a.difference(b)


         * القاموس وھو اشبھ بعمل دلیل للربط بین مفتاح بحیث استدعى الكود بسھولة
         * متنساش ان لازم اعمل الاقواس دیھ { } و بعدھا یكون فیھ المفتاح , بعدھا القيمة كلھم في كوتشين  
         * بحیث لما انادي بالمفتاح یجیبلي القیمة فورا
allkeys = {'egypt':'0020' , 'america':'001' , 'ksa':'00966'}
         * طريقة لكتابة قاموس
{n:n**2 for n in range(6)}
         * و ممكن اعدل فیھا
allkeys['egypt'] = '0030'
         * ولو عملت سؤال ھل كلمة  egypt  في المفاتیح ھیقول  true
print ('egypt' in allkeys)
         * ولو سالته هل 0020 من المفاتیح یقول لا
print ('0020' in allkeys)
         * لكن لو قاتلها ھي 0020 من القیم یقول ایوه
print ('0020' in allkeys.values())
         * ھنا ھیجبلي قیمة ال  value للمفتاح egypt
print (allkeys.get('egypt'))
         * ھنا نفس الموضوع , بس بقولھ لو ملقیتش مفتاح egypt ھات قیمة 0300 , فھیجیب 0020
print (allkeys.get('egypt','0300'))
         * ھنا عشان ملقاش فرنسا , ھیجیب 044 
print (allkeys.get('France','044'))
         * ممكن تضيف عنصر في القاموس كدة , وھیكون في الاول 
allkeys['Germany'] = ‘0046’
         * و ممكن امسح قیمة فیھم
del(allkeys['egypt'] )
         * و ممكن افضي كل القیم فیھا
allkeys.clear()
         * او لو عايز امسحها هي نفسها
del(allkeys)
         * ولو عايز تعرف ھما كام عنصر
len(allkeys)
         * و ممكن انسخ قاموس جوة قاموس بأمر كوبي 
dic = allkeys.copy()
         * و ممكن احوال كل عناصر لیست , تكون مفاتیح قاموس جدید بالامر ده 
         * الاول عرفت لسته , بعدھا قلت ان القاموس الفلاني , اصنع مفاتيحه من اللسته دیه
list1 = {"a","b","c","d"}
dic2 = dict.fromkeys(list1)


         * وطبعا لو عایز املي البیانات التانیة استخدم الامر ده 
dic2['a'] = 'aaa'
         * ولو عايز اعمل لستة بالمفاتيح بس 
a=list(dic2.keys())
         * ولو عايز اعمل لستة بالمعلومات بس 
b = list(dic2.values())
         * ولو عايز اعمل لستة بكله
c = list(dic2.items())
         * وممكن یكون القاموس متداخل كدة , بحیث لكل مفتاح اكتر من قیمة 
allkeys={'names':('a','b','c'),'address':('x','y','z')}
         * لو علمت كدة یظهر القيم و المفاتیح الثمانیة 
print ( allkeys )
         * كدة ھیظھر القیم التلاتة للمفتاح الاول 
print ( allkeys['names'] )
         * كدة ھیظھر القیمة التالتة للمفتاح الاول بس 
print(allkeys['names'][2])
         * ھنا لو مساحت مفتاح معین , ھیتمسح مع قیمه كلها 
del ( allkeys['names'])
         * ودیه طریقة عشان اعرض المفاتیح , بناء علي ترتیب القیم 
students = ['dave', 'john', 'jane']
grades = {'john': 'F', 'jane':'A', 'dave': 'C'}
print sorted(students , key=grades.__getitem__)


=========================================




________________


قاعدة  If


         * یتم كتابة إف , بعدھا نقطتين , ثم في السطر التالي تترك مسافة , و بايثون بتعرف ان الاف خلصت , لما تلاقي أن السطر مكتوب مش بمسافة
if x != 5 :
print ('hello')


         * لو استخدم ايلس , تكون السطر اللي بعده , واعمل نقطتين , وتيجي شمال 
if x != 5 :
print ('hello')
else :
print ('no')


         * و لو عایز استخدم آیلتس اف , اكتبھا الیف 
if x != 5 :
print ('hello')
elif x > 8 :
print ('yes')
else :
print ('no')


         * وممكن معملش سطور جدیدة , تكون في نفس السطر 
if x != 5 : print ('hello')
elif x > 8 : print ('yes')
else :print ('no')




         * و طبعا ممكن تستخدم معاھا  and , or  
and , or
         * كلا من or و and  تساوي الرمزین دول بالتوالي
and = &
or = |


         * و ممكن ادخل  if في قلب سطر زي كدة و معناھا , قیمة ماكس ھي a لو a اكبر , والا تكون b
a,b = 11,10
max = a if (a>b) else b
print (max)




=========================================


________________


قاعدة  For




         * لاستخدام الفور , لازم نستخدم معاھا ال Range و ده معناه ان یا for اشتغلي بقيمة ال n التى تتراوح من 2 ل 19 بخطوة 3
for n in range(2,20,3) :
print (n)


         * و ممكن اعملھا سطر واحد بالشكل ده , بحیث ھتساوي 
         * [(4 ,3) ,(1 ,3) ,(4 ,2) ,(1 ,2) ,(3 ,2) ,(4 ,1) ,(3 ,1)]
f = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
         * و ممكن استخدمھا اني افصص كلمة لحروف , فال for ھتجري من صفر لاخر رقم في طول الجملة , ونعرضھا حرف حرف
Y = 'supercalifragilisticexpialidocious'
for n in range(len(Y)) :
print (Y[n])


         * و بفرض اني عايز أكتب كلم من ورا لقدام اعمل الكود ده 
         * فكدة ال S اخدت الحروف من ورا لقدام و ضمتھا علي بعض
S = ' '
Y = 'supercalifragilisticexpialidocious'
for n in range(len(Y)) :
S = S + Y[(len(Y) - n-1)]








         * ولو عايز اللوب في حالة معينة متتكسرش , بس تتجاھل تنفیذ الأمر في حالة معینة استخدم  continue
t = 'supercalifragilisticexpialidocious'
for v in t :
if v == 'x' :
Continue
print v


         * مثال
t = "divide"
for v in t : 
        If v == "i" : 
Continue
print(v) 
         * مثال
for v in range(20) : 
        if v % 5 ==0 : 
                Continue
        print(v)
         * مثال
for v in range(20) : 
        if v % 5 ==0  or v % 3 == 0  : 
                Continue
        print(v)
         * استخدام  continue   مع  for  
for x in range(20) :
        If x% ==0 : 
                print("divided over  is " + str(x))
                continue
        print("not divided over  is " + str(x))


         * قراءة for في سترينج
YY = "how are you doing"
for g in YY : 
        print (g)
         * قراءة فور في ليست
students  = ["ahmed","ramy","heba"]


for a in students : 
        print(a)
         * قراءة فور في قاموس
grades  = {"ahmed":35 ,"mona":40 ,"mena":37 }


for a in grades : 
        print(a)
         * مثال اخر
grades  = {"ahmed":35 ,"mona":40 ,"mena":37 }


for a in grades.items() : 
        print(a)
         * مثال اخر
grades  = {"ahmed":35 ,"mona":40 ,"mena":37 }


for a,b in grades.items() : 
        print(a)
print(b)
         * مثال
grades  = {"ahmed":35 ,"mona":40 ,"mena":37 }


for a in grades.keys() : 
        print(a)
         * مثال
grades  = {"ahmed":35 ,"mona":40 ,"mena":37 }


for a in grades.values() : 
        print(a)
         * أمر enumerate
students =  ["ahmed","ramy","ramy","mena"]


for i,a in enumerate(students) : 
        print(i)
print(a)
         * مثال
students =  ["ahmed","ramy","ramy","mena"]
grades = [25,33,66,95]
for i,a in zip(students,grades) : 
        print("student" + i + " got " + str(a) + "degree"  )
         * مثال
a  = [i for i in range(20) ]
print(a)  
         * مثال
a  = [i for i in range(20) if i%3 ==0 ]
print(a) 
         * مثال
a  = [i for i in range(20) if i%3 ==0  and i %2 ==0 ]
print(a) 
         * مثال
a  = [ i**2  for i in range(20) ]
print(a) 
         * مثال
a  = [i**2 for i in range(20) if i%3 ==0 and i %2 ==0 ]
print(a) 
         * مثال
a  = [(i,j) for i in range(3) for j in range(4)]
print(a) 
         * مثال
a  = [(i*2,j+3) for i in range(3) for j in range(4)]
print(a) 
         * استخدام else
for x in range(10) :
        print(x)
else :
        print("Done")
         * مثال
print(sum([k for k in range(20)]))
         * مثال
print(sum([1/k for k in range(1,11)]))


         * مثال
print(sum([3*(k**2) for k in range(150)]))


         * مثال
a = [3*x for x in [y**2 for y in range(10)]]


=========================================


________________


قاعدة while


         * تتم عبر كتابة الـ while ثم الشرط , ولو كان true يتم تنفيذ الخطوات اللي معمولة بمسافة يمين شوية , ثم الرجوع مرة اخرى لشرط الوايل لتقييمه , لو كان false  فيتم تجاوز كل الخطوات اللي معمولة مسافة , ثم الذهاب لأول خطوة مش معمول لها مسافة
         * هناخد رقم من المستخدم , بعدها الشرط ان يكون اقل من او يساوي 100 , و الشرطين اللى هيتنفذ , أن يتم طباعة الرقم , وزيادة عليه 1 , وفي الاخر بعد نهاية الوايل , يعرض كلمه done و هي مش معمول لها مسافة فكدة كدة هيتنفذ 


n = int(input("input number : "))


while n <= 10 :
        print(n)
        n = n +1
print("Done")
         * لو عايز اعمل دالة مستمرة على طول , اعمل while true بس متنساش اني اعمل كسر في النص بالـ break عند تحقق شرط معين
while True : 
        a = int(input("Number ?"))
        if a > 15 : 
                print("yes")
                break
        else :
                print("No")


print("end")
         *  ممكن نخلي فيه شرط في الوايل يخلي الفنكشن ترجع للشرط تقيمه تاني زي ده 
n = int(input("input number ?"))
while n<=100:
        print(n)
n = int(input("input number ?"))
print("Done")
        
         * و ممكن نحط قدام while رقم مش شرط , و هيفضل اللوب شغالة لغاية لما الرقم يوصل لصفر  , ساعتها هيتم التعامل كأنها false 
a = 8
while a : 
        print(a)
        a = a-1
         * ممكن اضافة ايلس مع وايل ,وساعتها وايل هتقعد تلف عدد غير محدود من المرات طالما الشرط محقق لغاية لما الشرط يبقى غير محقق , ساعتها يروح مع ايلس مرة واحدة و يخرج 
a = 0
while a<10 :
a+=1 
        print("more")
else:
        print("less")


=========================================


________________


مكتبة الاحصاء Statistics




         * هي مكتبة مهمة , للتعامل مع القيم الإحصائية في بايثون
         * يتم استدعائها بالأمر : 


import statistics as st
         * المتوسط الحسابي 
import statistics as st
b = [1,2,3,4,5,6]
a = st.mean(b)
print(a)
         * المتوسط المتجانس
import statistics as st
a = st.harmonic_mean( [7,2,3,6,9,33,2.5])
print(a)
         * الوسيط
import statistics as st
a = st.median( [3,6,9,4,5,3.2,9,7])
print(a)
         * مثال
import statistics as st
a = st.median( [3,6,9,4,5,3.2,9,7,9])
print(a)
         * الوسيط الأقل  : لو عدد القيم فردي بيكون نفس القيمة اللي في النص (نفس الميديان) , بس لو زوجي بدل ما أجمع الاتنين اللي في النص و نقسمها على 2 , هاخد القيمة الاقل فيهم 
import statistics as st
a = st.median_low( [3,6,9,4,5,3.2,9,7,9])
print(a)
         * الوسيط الأعلي : نفس فكرة الاقل لكن نأخذ الأعلي في حالة كان عدد الأرقام زوجي


import statistics as st
a = st.median_high( [3,6,9,4,5,3.2,9,7,9])
print(a)


         * المنوال : أكتر رقم تم تكراره
import statistics as st
a = mode( [2,3,5,4,2,3,6,9,8,5,2,2,3,4,6])
print(a)
         * الانحراف المعياري
import statistics as st
a = st.stdev([3.2,6.9,8.1,-9.3,66])
print(a)




         * التباين
import statistics as st
a = st.variance([3.2,6.9,8.1,-9.3,66])
print(a)


=========================================


________________


 مكتبة Random


         * رقم عشوائي بين الصفر و الواحد 
import random as rn
a = rn.random()
print(a)
         * هات رقم صحيح من 1 ل 20 


import random as rn
a = rn.randint(1,20)
print(a)
         * رقم كسري بين 1 و 20 
import random as rn
a = rn.uniform(1,20)
print(a)
         * يعطي رقم صحيح من الصفر للرقم الموضوع هنا 15 
import random as rn
a = rn.randrange(150)
print(a)
         * يعني هات رقم من 0 ل 20 بس يكون من الخطوات  2 , (زوجي) 
import random as rn
a =rn.randrange(0,20,2)
print(a)


         * يقوم باختيار احد العناصر من الداخل
import random as rn
a =rn.choice(['a','b','c'])
print(a)
         * يقوم باختيار أحد الحروف بشكل عشوائي 


import random as rn
a =rn.choice('sweet home alabama')
print(a)


         *          * يقوم باختيار عشر عناصر  , من صفر الى 200 
import random as rn
a =rn.sample(range(200) ,10)
print(a)
         * يقوم بعمل ترتيب عشوائي للقائمة  
import random as rn
items = [1,2,3,4,5,6]
rn.shuffle(items)
print (items)


=========================================


________________


الدوال  Functions


         * يتم اولا كتابة def قبلها , ثم اسم الدالة , ثم أقواس () واللي هتتساب فاضية لو مفيش باراميترز  و لما تنادي  عليها في اي مكان اكتب اسمها و بعدها اقواس , بس لازم الدالة تتقري الاول 
def star() : 
    for h in range(10) : 
        print ('**')


star()
         * لابد أن يتم تعريف الدالة قبل استخدامها  
star()


def star() : 
    for h in range(10) : 
        print ('**')




         * لابد أن يتم تعريف الدالة قبل استخدامها  
def star() : 
    for h in range(10) : 
        print ('**')


s=star
s()










         * يمكن استخدام الدالة , عبر إدخال قيم محددة فيها , ويكون اسمها *args   , والتي اولا يمكن تحديد ما هي هذه القيم بالضبط
def find_avg(a,b):
        average = (a+b)/2
        print ("average is ",average)
find_avg(2,3)
         * و ممكن عمل  args     غير محددة , عبر كتابة * قبل المتغير , وتكون  وقتها list 
def find_avg(*numbers):
  sum = 0
  for i in numbers :
    sum += i
  print ("average is ",sum/(len(numbers)))
  print (numbers)
find_avg(2,3)
find_avg(2,3,4)
find_avg(1,2,3,4,5,6,7,8,9,10)
         * و من الممكن استخدام النجمة * إرسال متغيرات أثناء مناداة الدالة و ليس في تعريفها
def avg_of_two(a,b):
  print ((a+b)/2)
def avg_of_three(a,b,c):
  print ((a+b+c)/3)
var1 = (1,2)
avg_of_two(*var1)
var2 = (1,2,3)
avg_of_three(*var2)
         * مثال آخر
def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print ("another arg through *argv :", arg)


test_var_args('ahmed','mohamed','mona','sameh')
         * وهناك ما يسمى **kwargs    وهي بإرسال قاموس بدلا من ليست كمتغيرات , وتبدأ بـ **
def print_values(**values):
  print (values)
print_values(one = 1, two = 2)


         * مثال أخر في نفس السياق 
def print_values(**values):
  for key, value in values.items():
    print("{} = {}".format(key,value))
print_values(one = 1,two = 2,three = 3,four = 4,five = 5)




         * مثال أخر في نفس السياق 
def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print ("%s == %s" %(key,value))
 
greet_me(name="Python")
         * و ممكن ارسال الـ kwargs   حينما يتم استدعاء الدالة  
def avg_of_two(a,b):
  print ((a+b)/2)
def avg_of_three(a,b,c):
  print ((a+b+c)/3)
var1 = {'a':1,'b':2}
avg_of_two(**var1)
var2 = {'a':1,'b':2,'c':3}
avg_of_three(**var2)






         * مثال مجمع  
def show_details(a,b,*args,**kwargs):
  print("a is ",a)
  print("b is ",b)
  print("args is ",args)
  print("kwargs is ",kwargs)
show_details(1,2,3,4,5,6,7,8,9)
print("-----------")
show_details(1,2,3,4,5,6,c= 7,d = 8,e = 9)
print("-----------") 
         * مثال آخر  
def test_args_kwargs(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)
# first with *args
args = ("two", 3,5)
test_args_kwargs(*args)
 
# now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)
         * استخدام الـ args
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') :
    print ( "-- This parrot wouldn't", action)
    print ("if you put", voltage, "volts through it.")
    print ("-- Lovely plumage, the", type)
    print ("-- It's", state, "!")




parrot(1000) # 1 positional argument
parrot(voltage=1000) # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM') # 2 keyword arguments




         * مثال آخر
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') :
    print ( "-- This parrot wouldn't", action)
    print ("if you put", voltage, "volts through it.")
    print ("-- Lovely plumage, the", type)
    print ("-- It's", state, "!")






parrot(action='VOOOOOM', voltage=1000000) # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump') # 3 positional arguments
parrot('a thousand', state='pushing up the daisies') # 1 positional, 1 keyword




         * مثال آخر
def parrot(voltage, state='a stiff', action='voom'):
    print ("-- This parrot wouldn't", action),
    print ("if you put", voltage, "volts through it."),
    print ("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}


parrot(**d)
         * نماذج من الأخطاء
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue') :
    print ( "-- This parrot wouldn't", action)
    print ("if you put", voltage, "volts through it.")
    print ("-- Lovely plumage, the", type)
    print ("-- It's", state, "!")




parrot() # required argument missing
parrot(voltage=5.0, 'dead') # non-keyword argument after a keyword argument
parrot(110, voltage=220) # duplicate value for the same argument
parrot(actor='John Cleese') # unknown keyword argument




         * ومن الممكن إعطاء قيم افتراضية للدالة , بحيث يتم استخدامها اذا لم يتم تحديدها  
def powers(m, n = 4 ) : 
    print (m**(n))
powers(3,2)




         * وإذا لم يتم تحديدها تستخدم القيمة الافتراضية  
def powers(m, n = 4 ) : 
    print (m**(n))
powers(3)
         * وممكن أثناء استدعاء الدالة أن يتم عمل تحديد الأرقام المعطاة  
def powers(m,n) : 
    print (m**(n))


powers(m=3 ,n= 4)




         * وممكن اثناء الاستدعاء أن يتم كتابة الرموز دون ترتيب 
def powers(m,n) : 
    print (m**(n))


powers(n=3 ,m= 4)






         * ويمكن استخدام أمر return  لإعطاء قيمة للدالة  
def power(y,c) : 
    x = y**c
    return x


print(power(2,3))




         * ويمكن عمل دوال متداخلة  
def power(y,c) : 
    x = y**c
    return x
     
def times4(xx) : 
    z = 4*xx
    return z


def add7(zz) : 
    w = zz+7
    return w
    
d = int(input('first : '))
dd = int(input('second : '))


print (add7(times4(power(d,dd))))




         *  فيه حاجة اسمها variable scope يعني مجال تعريف المتغير , يعني  لو فيه متغير اتعرف برة , هيسمع برة بس , ولو اتغير في مكان برة هتتغير قيمته , لكن لو فيه متغير بنفس الاسم اتعرف داخل فنكشن , فيكون حاجة تانية بقيمة مختلفة , ولا يتعارض مع اللي برة حتى لو بنفس الاسم 


         * يعني هنا الـ xx اللي جوة بـ 14 بينما اللي برة بـ 5 
xx = 5


def gg() : 
    xx = 14
   
gg()
print (xx)




         * ولو عايز اللي برة يسمع في اللي جوه , استخدم جوه كلمة global في تعريف المتغير , وبعدها قول اللي انت عايزه عشان يعرف انك قصدك على اللى برة 
xx = 5


def gg() : 
    global xx
    xx = 14
    
gg()
print (xx)




         * اللمدا , هي استخدام مختصر و ذكي للدوال , يعني هاعمل دالة بشكل سريع من غير ما اعمل الشكل الكبير الخاص بالدالة
         * ببساطة اكتب اسم الدوالة powers يساوي المدى بعدها العناصر المستخدمة x,y بعدها نقطتين : بعدها المخرج هيساوي ايه


powers = lambda x,y : x**y


print (powers(5,3))




         * وممكن اعمل كذا لمدا جوة ليست , بحيث انادي عليها , اني اقول اسمها بعدها رقم العنصر  في قوس مربع  بعدها الرقم المطلوب في قوس دائري 
powers = [lambda x: 1,lambda x: x,lambda x: x**2,lambda x: x**3]


print(powers[0](5))  
print(powers[1](5))  
print(powers[2](5))  
print(powers[3](5))  




         * الفلتر , هو طريقة اختيار أرقام معينة , بناء على شرط محدد , وغالبا يكون الشرط بالمدا
         *  يعني هنا قلنا ان اللسته ارقام كذا بعدها اقوله ان الارقام الزوجية , هي لسته , مع فلتر (ا , ب)
         * أ : يتم وضع لمدا لو تحققت يتم تفعيل الفلتر , لم تتحقق لا تفعل
         * ب : اللسته الاصلي اللي هياخد منها
mylist = [0,1,2,3,4,5,6,7,8,9]
evennumber = list(filter(lambda x: x % 2 == 0 , mylist   ))
oddnumber = list(filter(lambda x: x % 2 == 1 , mylist   ))
print (evennumber)
print (oddnumber)
         * أما الماب فهو تطبيق دالة معينة (المدى ) على كل العناصر 
mylist = (0,1,2,3,4,5,6,7,8,9)


print ("square list" , list(map(lambda x: x**2 , mylist)))


         * وممكن بدل ما اكتب التفاصيل قدام اللمدا , استخدم دالة محددة سابقة التعريف 
list1 = (1,2,3,4,5,6)
 
def cpower (x):
    return x**3


print (list(map(lambda x :cpower(x)  , list1)))


         * دالة الـ yield الخضوع , وهي تسمح بتكرار ارقام معينة , وكل شوية ارجع واكمل من اخر رقم وقفت فيه   الاول اعرفها كدالة , وفي الفور , اكتب   yield بدل   return
         * بعدها خارج الدالة , انده لها في فور , واقول ان الـ g في دالة الخضوع , ساعتها كل شوية يجيب الرقم اللي بعده 


def yie():
    for i in range(10):
        yield i
        
for g in yie():
       print(g)


         * او اني اعمل نفس التعريف في الاول , بعدها اقول ان المتغير f يساوي الدالة نفسها , فلما اقول next بعدها المتغير بيجيب اللي بعده
def yie():
    for i in range(10):
        yield i
           
f = yie()
print (next(f))
print (next(f))
print (next(f))
         * مثلا ديه طريقة عادية لعمل متسلسلة فيبوناتشي 
def fibon(n):
    a = b = 1
    result =[]
    for i in range(n):
        result.append (a)
        a , b = b , a+b
    return result


print (fibon(20))




         * و ممكن اعملها بالـ yield كدة 
def fibon(n):
    a = b = 1
     
    for i in range(n):
        yield  a
        a , b = b , a+b
     
for x in fibon(20):
    print (x)




         * الـ recursive functions الدوال المتكررة , اللي بتستدعي نفسها
         * يعني لو عايز اعمل دالة للفاكتوريال , اعملها كدة , هي بتنده نفسها اكتر من مرة 
def fac(n):
    if n ==1 : 
        return 1
    else : 
        return n * fac(n-1)


print(fac(10))




=========================================


________________


الكلاس   Classes




         * ممكن عمل كلاس جديدة عن طريق اكتب class بعدها اسمها بعدها نقطتين , ثم المتغيرات او الدوال 
class car : 
    length = 15
    width = 8
    height = 6
    color = 'white'
    volume = length * width * height
    
print(car.color)




         * ممكن استخدام اي بيانات في الكلاس  
class car : 
    length = 15
    width = 8
    height = 6
    color = 'white'
    volume = length * width * height
    
print(car.color)




         * لما اقول ان فيه  object   يساوي الكلاس , يكون ليه نفس بياناته   
class car : 
    length = 15
    width = 8
    height = 6
    color = 'white'
    volume = length * width * height


volvo = car


print(volvo.height)




         * ولو تم حفظ الكلاس في ملف بامتداد py  ممكن اعمله استدعاء واستخدام كافة الدوال و المتغيرات فيها
from myclasses import  car 




         * او ممكن استدعاء كل الكلاسات المحفوظة فيه
from myclasses import  * 
         * الـ Class Variable  
class car() : 
    color = 'blue'
    
volvo = car
nissan = car


volvo.color = 'white'
nissan.color = 'green'


print(volvo.color)
print(nissan.color)
         * الـ instance variable  
class car() :
    def __init__(self, color):
        self.color = color
    
volvo = car('white')
nissan = car('green')


print(volvo.color)
print(nissan.color)




         * استخدام لأداة الـ self   
class calc : 
    def __init__(self,p2,p3) :
        self.power2 = p2**2
        self.power3 = p3**3
    
a = calc(40,50)
print(a.power2)
print(a.power3)
         * و ممكن اعمل قيم مفترضة للمعاملات  
class d : 
    def __init__(self,p2 = 10 ,p3 = 20) : 
        self.power2 = p2**2
        self.power3 = p3**3
a = d()
print(a.power2)
print(a.power3)




         * وممكن اقوم انا بتعيينها و الغاء القيم المفترضة  
class d : 
    def __init__(self,p2 = 10 ,p3 = 100) : 
        self.power2 = p2**2
        self.power3 = p3**3
a = d(5,3)
print(a.power2)
print(a.power3)




         * او كدة  
class d : 
    def __init__(self,p2 = 10 ,p3 = 100) : 
        self.power2 = p2**2
        self.power3 = p3**3
a = d(p2=5,p3=3)
print(a.power2)
print(a.power3)




         * --
class d :  
    def __init__(self,nn,p2 = 10 ,p3 = 100) : 
        
        self.power2 = p2**2
        self.power3 = p3**3
        self.roots = nn
        
    def root(self ) : 
        print (self.roots**0.5)
    
a = d(2500)
a.root()




         * وممكن التعامل مع الدوال بشكل مباشر من غير المرور بـ init  
class d :  
    def square(n) : 
        print (n**2)
    
    def summ(a,b,c,d,e,f) : 
        return ((a+b-c+e)*(d+f))


  
a = d    
a.square(3)
print (a.summ(1,2,3,4,5,7))




         * مثال
class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def show(self):
        s = '%s, %s, balance: %s' % (self.name, self.no, self.balance)
        print (s)


a1 = Account('John Olsson', '19371554951', 20000)
a2 = Account('Liz Olsson', '19371564761', 50000)
print("a1 balance :  " , a1.balance )
print("a2 no      :  " ,   a2.no)


a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print ("a1's balance:", a1.balance)
print ("a2's balance:", a2.balance)


a1.show()
a2.show()




         * مثال 
class Person:
    def __init__(self, name,mobile_phone=None, office_phone=None,private_phone=None, email=None):
        self.name = name
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email
    def add_mobile_phone(self, number):
        self.mobile = number
    def add_office_phone(self, number):
        self.office = number
    def add_private_phone(self, number):
        self.private = number
    def add_email(self, address):
        self.email = address
    def dump(self):
        s = self.name + '\n'
        if self.mobile is not None:
            s += 'mobile phone: %s\n' % self.mobile
        if self.office is not None:
            s += 'office phone: %s\n' % self.office
        if self.private is not None:
            s += 'private phone: %s\n' % self.private
        if self.email is not None:
            s += 'email address: %s\n' % self.email
        print (s)


p1 = Person('Hans Hanson',office_phone='767828283', email='h@hanshanson.com')
p2 = Person('Ole Olsen', office_phone='767828292')
p2.add_email('olsen@somemail.net')
phone_book = [p1, p2]


for person in phone_book:
    person.dump()






=========================================


________________


Numpy
         * هي من أهم المكتبات المستخدمة في بايثون , والتي تستخدم بقوة في العمليات الرياضية و التعامل مع المصفوفات 
         * يتم استدعائها بالأمر


import numpy as np  
العمليات الرياضية 




         * الدوال المثلثية مشكلتها انها تتعامل بالـ radians  و ليس الـ degree
from  numpy import *


a = sin(30)
b = cos(30)
c = tan(30)


print(a , b , c)




         * ولعلاج الأمر , اما يم يتم ضرب الرقم في (باي  / 180)  
from  numpy import *


a = sin(30*np.pi/180)
b = cos(30*np.pi/180)
c = tan(30*np.pi/180)


print(a)
print(b)
print(c)




         * ام يتم استخدام الدالة  deg2rad  
from  numpy import *


a = sin(deg2rad(30))
b = cos(deg2rad(30))
c = tan(deg2rad(30))


print(a)
print(b)
print(c)




         * التقريب أمر round  
from  numpy import *


a = round(3.68528)
b = round(3.68528,1)
c = round(3.68528,2)
d = round(3.68528,3)
e = round(3.68528,4)


print(a)
print(b)
print(c)
print(d)
print(e)




         * أمر ceil , floor  للتقريب الاعلى والاقل  
from  numpy import *


a = floor(3.68528)
b = ceil(3.68528)


print(a)
print(b)




         * أمري mod , power  
from  numpy import *


a = mod(20,7)
b = power(2,5)


print(a)
print(b)
________________


كتابة المصفوفات


         * يتم استخدام أمر array  لتحويل ليست إلى مصفوفة   
from  numpy import *




a = [2,3,6,5,4,7,8]
b = array(num)


print(a)
print(b)


         * ويمكن عمل مصفوفة ثنائية الأبعاد  
from  numpy import *




a = [[1,2,3],[5,3,6],[9,6,5]]
b = array(a)
print(a)
print(b)


         * وممكن استخدام أمر range  لعمل مصفوفة  
from  numpy import *


a = array([range(i, i + 3) for i in [2, 4, 6]])


print(a)




         * يمكن عمل تعريف للمتغيرات عقب كتابتها  
from  numpy import *


a = array([('x',3,4.2),('y',4,5.3),('z',5,6.3)],
           dtype =[('name','U5'),('number','i2'),
                   ('value','f4')])
print(a)
         * استخدام أمر   empty  يمكن عمل مصفوفة فارغة  
from  numpy import *


a = empty((3,2))


print(a)
         * امر uniform  يأتي بقيمة عشوائية
from numpy import *
a = random.uniform(1,10)
b = random.uniform(1,10,20)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
         * بأمر random.random   يمكن عمل مصفوفة بأرقام عشوائية تتراوح بين 0 و 1   
from  numpy import *


a =random.random((2,3))


print(a)






         * أمر random.normal  يأتي بالتوزيع الطبيعي لأرقام بين الصفر و 1 , عدد 10 أرقام   
from  numpy import *


a =random.normal(0,1,10)


print(a)
         * بأمر  random.randint  يمكن تحديد رقم عشوائي صحيح بين 0 و 150 
from  numpy import *


a =  random.randint(150)


print(a)
         * و   يمكن تحديد 7 ارقام صحيحة عشوائية من 0 الى 5 
from  numpy import *


a =random.randint(5, size=7)


print(a)
         * ولو تم كتابة رقمين فتكون الأرقام تتراوح بين الرقمين  
from  numpy import *


a =random.randint(5,20, size=7)


print(a)
         * ويمكن عمل مصفوفة أرقام صحيحة بين 0 و 10  
from  numpy import *


a = random.randint(0, 10, (3, 3))


print(a)




         * او تلات ابعاد  
from  numpy import *


a = random.randint(5,10, size=(3, 4, 5))


print(a)
         * او يتعمل صف ارقام و يتم تشكيلها  
from  numpy import *


a = random.randint(1,60,25)
b = reshape(a,(5,5))


print(a)
print(b)
         * هنا يعمل ارقام عشوائية من 0 لـ 1 بالعدد المطلوب  
from  numpy import *


a = random.rand(15)


print(a)




         * او مصفوفة بعدين  
from  numpy import *


a = random.rand(5,3)


print(a)




         * او تلات ابعاد  
from  numpy import *


a = random.rand(5,3,2)


print(a)
         * أمر choice   يختار قيمة عشوائية  
from  numpy import *


y=[1,2,3,6,9,8,5,4,7,8,9,6,5,9,6]
a = random.choice(y)


print(a)
         * ويمكن اختيار اكثر من قيمة  
from  numpy import *


y=[1,2,3,6,9,8,5,4,7,8,9,6,5,9,6]
a = random.choice(y. size = 5)


print(a)


         * أمر shuffle  يعمل تغيير عشوائي في الترتيب  
from  numpy import *


y=[1,2,3,6,9,8,5,4,7,8,9,6,5,9,6]
print(y)


random.shuffle(y)


print(y)




         * عمل مصفوفة اصفار او  وحايد  
from  numpy import *
a = zeros(8)
b = ones(10)


print(a)
print(b)
         * لو مطلوب بعدين (فيه قوسين في الاول و في الاخر )  
from  numpy import *
a = zeros((3,5))
b = ones((6,8))


print(a)
print(b)
         * تلات أبعاد  
from  numpy import *
a = zeros((2,3,2))
b = ones((2,3,2))


print(a)
print(b)
         * مصفوفة الوحدة  
from  numpy import *
a = eye(5) 
print(a)
         * أمر full   بيعمل مصفوفة بنفس الرقم المعطى  
from  numpy import *
a = full((3, 5), 35)


print(a)




         * ويمكن كتابة مصفوفة بأبعاد محددة كدة
from  numpy import *


a =arange(18).reshape(3,6)
b =arange(27).reshape(3,3,3)


print(a)
print(b)
         * لكتابة ارقام متوزعة بالتساوي بين رقمين
from  numpy import *


b =linspace(0,30)
c =linspace(0,100,5)


print(b)
print(c)
         * لتحويلها لمصفوفة
from  numpy import *
b =linspace(0,30,12).reshape(3,4)
c =linspace(0,100,27).reshape(3,3,3)


print(b)
print(c)
         * المصفوفة القطرية
from numpy import *
a =diag(array([5,12,4,-1,3]))
b =diag(array([5,12,4,-1,3]),k=3)
print(a)
print('-------------------------')
print(b)
print('-------------------------')
________________
التعامل مع المصفوفات




         * ممكن حساب الأرقام التي ليست صفر  
from  numpy import *
a = random.randint(0, 10, (3, 3))
b = count_nonzero(a)
print(a)
print(b)
         * او تحديد عدد الأرقام اكبر او اصغر من كذا   
from  numpy import *
a = random.randint(0, 10, (3, 3))
b = count_nonzero(a>5)
c = count_nonzero(a<8)


print(a)
print(b)
print(c)




         * وممكن حساب الأرقام يكون بالصف كله  
from  numpy import *
a = random.randint(0, 10, (3, 3))
b = count_nonzero(a>5,axis=1)
c = count_nonzero(a<8,axis=1)


print(a)
print(b)
print(c)




         * لمعرفة هل فيه رقم اكبر او اصغر من كذا ولا لا   
from  numpy import *
a = random.randint(0, 10, (3, 3))
b = any(a>5)
print(a)
print(b)
         * ويمكن عملها في كل صف  
from  numpy import *
a = random.randint(0, 10, (3, 3))
b = any(a>5,axis=1)


print(a)
print(b)
         * ويمكن معرفة هل كل العناصر شرط معين
from  numpy import *
a = random.randint(0, 10, (3, 3))
b = all(a>5)


print(a)
print(b)
         * ويمكن معرفة هل العناصر اكبر من او اصغر من رقم معين
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b = a>10
c = a<15


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)




         * مقارنة المصفوفات  
from  numpy import *


a =arange(9).reshape(3,3)
b =arange(9).reshape(3,3)
c = 2*b
d = isclose(a,b,rtol = 0.1)
e = isclose(a,c,rtol = 0.1)




print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)




         * يمكن ضرب قيم المصفوفة في بعضها (ضرب الدوت)  
from  numpy import *
 
a =arange(5)
b =empty(5)


multiply(a, 10, out=b)


print(a)
print(b)


         * لرفع كل العناصر للأس الرابع  
from  numpy import *
 
a =arange(5)
b =empty(5)


power(a, 4, out=b)


print(a)
print(b)


         * مجموع قيم المصفوفة  
from  numpy import *
 
a =arange(15)




b = add.reduce(a)


print(a)
print(b)


         * حاصل ضرب قيم المصفوفة 
from  numpy import *
 
a =arange(2,8)




b = multiply.reduce(a)


print(a)
print(b)




         * عملية ضرب متبادلة  
from  numpy import *
 
a =arange(2,8)




b = multiply.outer(a,a)


print(a)
print(b)
         * جمع كل الارقام السابقة  
from  numpy import *
 
a =arange(10)




b = add.accumulate(a)


print(a)
print(b)
         * ضرب الارقام السابقة  
from  numpy import *
 
a =arange(2,8)




b = multiply.accumulate(a)


print(a)
print(b)




         * لمعرفة عدد عناصر المصفوفة , او عدد صفوفها لو اكتر من بعد
from  numpy import *
 
a =arange(12)
b = len(a)


c = a.reshape(3,4)
d = len(c)


print(a)
print(b)
print(c)
print(d)
         * لمعرفة كل عدد عناصرها   
from  numpy import *
 
a =arange(12)
b = a.size


c = a.reshape(3,4)
d = c.size


print(a)
print(b)
print(c)
print(d)
         * و هنا الابعاد بالتفصيل  
from  numpy import *
 
a =arange(12)
b = a.shape


c = a.reshape(3,4)
d = c.shape


print(a)
print(b)
print(c)
print(d)
         * عدد ابعادها  
from  numpy import *
 
a =arange(12)
b = a.ndim


c = a.reshape(3,4)
d = c.ndim


print(a)
print(b)
print(c)
print(d)
         * انوع البيانات في المصفوفة  
from  numpy import *
 
a =array(['a','d','g','h','j'])
b = a.dtype


c = arange(12)
d = c.reshape(3,4)
e = d.dtype


print(a)
print(b)
print(c)
print(d)
print(e)




         * وممكن نعمل تشكيل للمصفوفة من هنا  
from  numpy import *




a = matrix('{} {} ; {} {}'.format(1,2,3,4))
b = matrix('{} {} {};{} {} {}'.format(1,2,3,4,5,6))


print(a)
print(b)
         * نجمع قيم المحور  
from  numpy import *


a =arange(9)
b = a.reshape(3,3)
c = trace(b)




print(a)
print(b)
print(c)
         * قيمة المصفوفة , وقيمة ايجان فاليو  
from  numpy import *


a =arange(9)
b = a.reshape(3,3)
c = linalg.det(b)
d = linalg.eig(b)
print(a)
print(b)
print(c)
print(d)
         * الاقتطاع من المصفوفة  
from  numpy import *


a =arange(10) 


c = a[3]
d = a[3:9]
e = a[3:9:2]
f = a[-1]
g = a[-3]


print(a)
print(c)
print(d)
print(e)
print(f)
print(g)




         * مثال
from  numpy import *


a =arange(36).reshape(6,6)


c = a[3]
d = a[3:9]
e = a[3:9:2]
f = a[-1]
g = a[-3]


print(a)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
print('-------------------------')
print(f)
print('-------------------------')
print(g)




         * مثال
from  numpy import *


a =arange(36).reshape(6,6)


c = a[3,1]
d = a[3,:]
e = a[:,2]
f = a[:,1:3]
g = a[1:2,:]


print(a)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
print('-------------------------')
print(f)
print('-------------------------')
print(g)




         * مثال
from  numpy import *


a =arange(36).reshape(6,6)


c = a[3:4,1:5]
d = a[2:,3:]
e = a[:2,:3]
f = a[:,-1]
g = a[-1,:]


print(a)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
print('-------------------------')
print(f)
print('-------------------------')
print(g)




         * مثال
from  numpy import *


a =arange(36).reshape(6,6)


c = a[::2,::3]
d = a[::-1,::-1]
e = a[:2:-1,:3:-1]
f = a[2::2,3::3]
g = a[-1::,-1::]


print(a)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
print('-------------------------')
print(f)
print('-------------------------')
print(g)




         * تعديل القيم  
from  numpy import *


a =arange(16).reshape(4,4)
print(a)


a[2,3] = 0
print(a)
a[:,3] = 0 
print(a)
a[2,:] = 0 
print(a)
a[:,:] = 0 
print(a)




         * النسخة المربوطة   
from  numpy import *


a =arange(16).reshape(4,4)
print(a)
b = a[:,1:3]
print(b)
a[:,:] = 5
print(a)
print(b)




         * النسخة المستقلة  
from  numpy import *


a =arange(16).reshape(4,4)
print(a)
b = a[:,1:3].copy()
print(b)
a[:,:] = 5
print(a)
print(b)




         * ثلاثة أبعاد  
from  numpy import *


a =arange(18).reshape(3,3,2)


c = a[1]
d = a[1,2]
e = a[2,2,1]




print(a)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)




         * التجزيئ
from  numpy import *
x = [11,22,33,44,55,66,77,88]
x1, x2, x3 = split(x, (3,6))
print(x1, x2, x3)
x1, x2, x3 = split(x, (1,5))
print(x1, x2, x3)
x1, x2, x3 = split(x, (6, 3))
print(x1, x2, x3)
x1, x2, x3 = split(x, (0, 3))
print(x1, x2, x3)
x1, x2, x3 = split(x, (4, 0))
print(x1, x2, x3)




         * تحديد عنصر   
from  numpy import *


a =arange(16).reshape(4,4)


b = a[2][1]


print(a)
print(b)




         * ضم  مصفوفات  
from  numpy import *


a =arange(4).reshape(2,2)
b =2*arange(4).reshape(2,2)


c = vstack((a,b))
print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)




         * بشكل افقي
from  numpy import *


a =arange(4).reshape(2,2)
b =2*arange(4).reshape(2,2)


c = hstack((a,b))
print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)




         * زيادة رأسية  , أمر مختلف
from numpy import *


a =random.randint(5,20, size=9).reshape(3,3)
b =random.randint(5,20, size=9).reshape(3,3)
c = concatenate([a,b] , axis = 0)




print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')




         * زيادة افقية   
from numpy import *


a =random.randint(5,20, size=9).reshape(3,3)
b =random.randint(5,20, size=9).reshape(3,3)
c = concatenate([a,b] , axis = 1)




print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')




         * اكبر و اصغر قيم  
import numpy as np


a =np.random.randint(5,20, size=9).reshape(3,3)


b = np.max(a)
c = np.min(a)
d = np.argmax(a)
e = np.argmin(a)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)




         * ايجاد الـ Variance و الـ Covariance  
from numpy import *


a =random.randint(5,20, size=9).reshape(3,3)


b = var(a)
c = cov(a)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)


________________
________________




العمليات الرياضية للمصفوفات


         * الجمع والطرح  
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b =random.randint(5,20, size=9).reshape(3,3)
c = a+b
d = a-b


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)




         * الضرب والقسمة  
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b =random.randint(5,20, size=9).reshape(3,3)
c = a*b
d = a/b


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)




         * الضرب و القسمة  على رقم
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b =random.randint(5,20, size=9).reshape(3,3)
c = a*3
d = b/5


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)




         * دوال للمصفوفة
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b =random.randint(5,20, size=9).reshape(3,3)
c = sin(a)
d = b**2
e = log(a)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)




         * ضرب المصفوفات
from numpy import *
a =random.randint(1,4, size=9).reshape(3,3)
b =random.randint(1,4, size=9).reshape(3,3)




c = dot(a,b)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)




         * مجموع القيم  
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b = sum(a)
c = a.sum()
d = a.sum(axis = 1)
e = a.sum(axis = 0)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)




         * قيم احصائية  
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b = a.mean()
c = a.std()
d = a.var()


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)




         * معامل الارتباط
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b = corrcoef(a)


print(a)
print('-------------------------')
print(b)
print('-------------------------')




         * الترتيب الافقي و الرأسي  
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b = sort(a,axis=0)
c = sort(a,axis=1)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')




         * معكوس المصفوفة  
from numpy import *
a =random.randint(1,4, size=9).reshape(3,3)
b =linalg.inv(a)


c = dot(a,b)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
________________
قراءة الملفات


         * فتح الملفات  
from numpy import *
fname = 'D:\\1.txt'
dtype1 = dtype([('gender', '|S1'), ('height', 'f8')])
a = loadtxt(fname, dtype=dtype1, skiprows=9, usecols=(1,3))
 
print(a)
------------------------------------------------------------------------------
# Student data collected on 17 July 2014
# Researcher: Dr Wicks, University College Newbury


# The following data relate to N = 20 students. It
# has been totally made up and so therefore is 100%
# anonymous.


Subject Sex    DOB      Height  Weight       BP     VO2max
(ID)    M/F  dd/mm/yy     m       kg        mmHg  mL.kg-1.min-1
JW-1     M    19/12/95    1.82     92.4    119/76   39.3
JW-2     M    11/1/96     1.77     80.9    114/73   35.5
JW-3     F    2/10/95     1.68     69.7    124/79   29.1
JW-6     M    6/7/95      1.72     75.5    110/60   45.5
# JW-7    F    28/3/96     1.66     72.4    101/68   -
JW-9     F    11/12/95    1.78     82.1    115/75   32.3
JW-10    F    7/4/96      1.60     -       -/-      30.1
JW-11    M    22/8/95     1.72     77.2    97/63    48.8
JW-12    M    23/5/96     1.83     88.9    105/70   37.7
JW-14    F    12/1/96     1.56     56.3    108/72   26.0
JW-15    F    1/6/96      1.64     65.0    99/67    35.7
JW-16    M    10/9/95     1.63     73.0    131/84   29.9
JW-17    M    17/2/96     1.67     89.8    101/76   40.2
JW-18    M    31/7/96     1.66     75.1    -/-      -
JW-19    F    30/10/95    1.59     67.3    103/69   33.5
JW-22    F    9/3/96      1.70     -       119/80   30.9
JW-23    M    15/5/95     1.97     89.2    124/82   -
JW-24    F    1/12/95     1.66     63.8    100/78   -
JW-25    F    25/10/95    1.63     64.4    -/-      28.0
JW-26    M    17/4/96     1.69     -       121/82   39.


         * مثال
from numpy import *
a,b,c = loadtxt('D:\\0.txt', unpack=True,skiprows=3)
print(a)
print(b)
print(c)


----------------------------------------------------
Median age at First Marriage, 1890-2010
Source: U.S. Bureau of the Census, www.census.gov
Year     Men      Women
1890     26.1     22.0
1900     25.9     21.9
1910     25.1     21.6
1920     24.6     21.2
1930     24.3     21.3


         * أمرمختلف
from numpy import *


data = genfromtxt('D:\\0.txt', skip_header=1,
                  dtype=[('student','u8'),
                         ('gender','S1'),('black','f8'),
                         ('colour','f8')],delimiter=',',
                         missing_values='X')


print(data)


-----------------------------------------------------------
Subject Number, Gender, Time (words in black), Time (words in colour)
1,F,18.72,31.11
2,F,21.14,52.47
3,F,19.38,33.9




   
________________
التعامل مع Polynomials


         * الدرجة الأولي  
import numpy as np


Polynomial = np.polynomial.Polynomial


X= np.array([0,20,40,60,80,100,120,140,160,180])
Y= np.array([10,9,8,7,6,5,4,3,2,1])


points,stats = Polynomial.fit(X,Y,1,full=True)


print(points)




         * كتابة الـ Poly   
from numpy import *


a = poly1d((-7))
b = poly1d((-7,2))
c = poly1d((-7,2,1))
d = poly1d((-7,2,1,3))
e = poly1d((-7,2,1,3,6))




print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
         * التعويض
from numpy import *


a = poly1d((-7,2,1,3,6))


b=a(5)
c=a(0)
d=a(-15)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
         * أمر مختلف
from numpy import *


a = polyval((1,2),2)
b = polyval((1,2,3),7)
c = polyval((1,2,3,5),-3)
d = polyval((1,2,3,5,-6),12.6)




print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
         * اشتقاق المعادلة  
from numpy import *


a =polyder(poly1d((1,2,3)))
b =polyder(poly1d((1,2,3)),2)
c =polyder(poly1d((1,2,3)),3)


d =polyder(poly1d((1,2,3,5,12)))
e =polyder(poly1d((1,2,3,5,12)),3)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
         * التعويض في الاشتقاق
from numpy import *


a =polyder(poly1d((1,2,3)))
b =polyder(poly1d((1,2,3)),2)
c =polyder(poly1d((1,2,3)),3)


d =polyder(poly1d((1,2,3,5,12)))
e =polyder(poly1d((1,2,3,5,12)),3)


print(a(2))
print('-------------------------')
print(b(0))
print('-------------------------')
print(c(3))
print('-------------------------')
print(d(-1))
print('-------------------------')
print(e(5))
         * التكامل  
from numpy import *


a =polyint(poly1d((1,2,3)))
b =polyint(poly1d((1,2,3)),2)
c =polyint(poly1d((1,2,3)),3)


d =polyint(poly1d((1,2,3,5,12)))
e =polyint(poly1d((1,2,3,5,12)),3)


print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
         * التعويض في التكامل
from numpy import *


a =polyint(poly1d((1,2,3)))
b =polyint(poly1d((1,2,3)),2)
c =polyint(poly1d((1,2,3)),3)


d =polyint(poly1d((1,2,3,5,12)))
e =polyint(poly1d((1,2,3,5,12)),3)


print(a(2))
print('-------------------------')
print(b(0))
print('-------------------------')
print(c(3))
print('-------------------------')
print(d(-1))
print('-------------------------')
print(e(5))
         * جذور المعادلة (حلها)  
from numpy import *


a =roots(poly1d((1,2)))
b =roots(poly1d((1,2,3)))
c =roots(poly1d((1,2,3,5)))
d =roots(poly1d((1,2,3,5,12)))
e =roots(poly1d((1,2,3,5,12,22)))




print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
         * توافق النقاط  
from numpy import *


x = array([3,6,2,5,4])
y = array([2,3,-9,6,2.5])
z = polyfit(x, y, 2)




print(x)
print('-------------------------')
print(y)
print('-------------------------')
print(z)
print('-------------------------')




________________


التعامل مع التاريخ


         * الصياغة
from numpy import *
x = array('2015-07-04', dtype=datetime64)


print(x)
print('-------------------------')
         * مثال
from numpy import *
x = datetime64('2015-07-04')
print(x)
print('-------------------------')
         * زيادة ايام
from numpy import *
x = datetime64('2015-07-04')


y = x + arange(12)


print(x)
print('-------------------------')
print(y)
         * نقص ايام
from numpy import *
x = datetime64('2015-07-04')


y = x - arange(12)


print(x)
print('-------------------------')
print(y)
         * فارق الايام
from numpy import *
x = datetime64('2015-07-04')
y = datetime64('2018-09-21')


z = y-x


print(x)
print('-------------------------')
print(y)
print('-------------------------')
print(z)




________________


الدوال في نمباي


         * يتم استخدامها بأداة fromfunction  
from numpy import *


x = fromfunction(lambda i: i**3, (10,))


print(x)
print('-------------------------')
         * بعد واحد
from numpy import *


x = fromfunction(lambda i: 3 * (i+5)**3, (10,))


print(x)
print('-------------------------')
         * بعدين
from numpy import *


x = fromfunction(lambda i,j: i+j, (4,5))


print(x)
print('-------------------------')
         * مثال
from numpy import *


x = fromfunction(lambda i,j: 3*i*j, (4,5))


print(x)
print('-------------------------')
         * ثلاث ابعاد
from numpy import *


x = fromfunction(lambda i,j,k: i+j+k, (2,3,4))


print(x)
print('-------------------------')
         * مثال
from numpy import *


x = fromfunction(lambda i,j,k: (2*i)+(j**2)*k, (2,3,4))


print(x)
print('-------------------------')
         * شكل مختلف
from numpy import *


def powers(i):
    i = i**2
    return i
 
x = fromfunction(powers, (9,), dtype=int)


print(x)
print('-------------------------')
         * مثال
from numpy import *


def powers(i,j):
    i = i**j
    return i




x = fromfunction(powers, (4,5), dtype=int)


print(x)
print('-------------------------')
         * قيم بوليان
from numpy import *


m,n = 20, 5


def f(i):
    return (i % n == 0)
x = fromfunction(f, (m,), dtype=int)


print(x)
print('-------------------------')




=======================================
























Pandas






         * مكتبة Pandas  من أهم مكتبات بايثون , لقراءة البيانات و التعامل معها , وعمل الرسوم البيانية الخاصة بها
         * هي اختصار لكلمات : Panel Data Analysis
         * يتم استدعائها بالأمر   
import pandas as pd
العمليات الأساسية 
         * عمل مصفوفة من بعد واحد ( الـ S   كابيتال )  
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
         * القيم
data = pd.Series((0.25, 0.5, 0.75, 1.0))
print(data.values) // value
print(data.index) // index 
print(data.keys) // pair
         * معلومات عنها
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))
print(data.describe())
         * اكبر , اصغر
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))
print(data.agg(['max','min','sum','mean','std']))


         * الاجتزاء
data = pd.Series((0.25, 0.5, 0.75, 1.0))
print(data[1])
print(data[1:3])
print(data[1:3:2])
         * كتابة ليست
data1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd']) //as list 
data2 = pd.Series({'a':1,'b':2,'c':3,'d':4}) //as dictionary
print(data1)
print(data2)
         * قيمة محددة 
data1 = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
data2 = pd.Series({'a':1,'b':2,'c':3,'d':4})
print(data1['a'])
print(data2['b'])
         * عمل ليست
x = pd.Index([2,3,5,7,11])
print(x)


         * علاقات منطقية
a = pd.Index([1, 3, 5, 7, 9])
b = pd.Index([2, 3, 5, 7, 11])


print(a)
print(b)
print(a & b)
print(a | b)
print(a ^ b)
الرسومات البيانية




         * منحني عادي
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))
data.plot()
data.plot(kind='line')  


  



         * القرص
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))
data.plot(kind='pie')  
  





         * الاعمدة
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))
data.plot(kind='bar')  


  

         * أعمدة أفقية
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))
data.plot(kind='barh')
  





        
         * هيتسوجرام
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))        
data.plot(kind='hist')


  





         * الصندوق
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))


data.plot(kind='box')


  

         * المنحنى الطبيعي
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))


data.plot(kind='kde')


  





         * نفسه
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))


data.plot(kind='density')


  





         * المساحة
data = pd.Series((3,6,9,8,5,4,2,6,3,5,8))


data.plot(kind='area')


  

DataFrame


         * هي أداة مخصصة لعمل جداول صفوف و اعمدة من البيانات
         * كتابة الجدول
import pandas as pd
import numpy as np
myarray = np.array([[6,9,8,5,4,2],[0,2,5,6,3,9],
                    [8,5,4,1,2,3],[6,9,8,5,4,2],
                    [0,5,3,6,9,8],[8,7,4,5,2,3]])
rownames = ['a', 'b','c','d','e','f']
colnames = ['one', 'two', 'three','four','five','six']
df = pd.DataFrame(myarray, index=rownames, columns=colnames)
print(df)




         * باستخدام القاموس
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades)


         * اظهار عمود محدد
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades)
print(grades['Chemistry'])
         * اظهارها بالعكس (مقلوب المصفوفة)
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.T)










         * إظهار القيم والمفاتيح
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.keys())
print(grades.values)




         * معرفة هل القيمة كذا موجودة او لا
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print('Math' in grades.keys())
print('math' in grades.keys())
print(12 in grades.values)
print(55 in grades.values)


         * فك القيم
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.stack())




         * اظهار قيم محددة بالرقم
import pandas as pd


w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})


grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})


print(grades.iloc[:3, :2])




         * اظهار قيم بالاسم
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.loc['b':'c', 'Math':])
         * اظهار قيم بالشرط
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})


grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})


print(grades.loc[grades.Math >3])




         * اظهار أعمدة بشرط محدد
import pandas as pd


w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.loc[grades.Math >3,['French' ,'Math']])


         * اظهار اعمدة
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.columns)
         * اظهار صفوف
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})


grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})


print(grades.index)








         * اظهار عمود محدد
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades['Math'])


         * ترتيب صفوف
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.sort_values(['Math'],ascending= False))
print(grades.sort_values(['French'],ascending= True))
         * اظهار قيم إحصائية
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades.max())
print(grades.min())
print(grades.mean())
print(grades.std())






         * اظهار قيم إحصائية عمود محدد 
import pandas as pd


w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})


grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})


print(grades['Math'].max())
print(grades['French'].min())
print(grades['Physics'].mean())
print(grades['Chemistry'].std())
         * معامل الارتباط
import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])


print(df)
print(df.corr())




         * قيمة الانحراف
import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])


print(df)
print(df.skew())




         * كتابة جدول دالة تربيعية 
import pandas as pd
data = [{'square': i**2} for i in range(10)]
d = pd.DataFrame(data)
print(d)
         * عدد من الدوال
import pandas as pd
data = [{'square': i**2,'cube': i**3
         ,'root': i**0.5} for i in range(10)]


d = pd.DataFrame(data)
print(d)
         * مزج القواميس
import pandas as pd
d = pd.DataFrame([{'a':1,'b':2},{'a':3,'b':4},{'a':5,'b':6}])


print(d)




         * مزج القواميس مع وجود فراغات 
import pandas as pd
d = pd.DataFrame([{'a':1,'b':2},{'b':3,'c':4},{'d':5,'e':6}])
print(d)
         * كتابة جدول
import pandas as pd
import numpy as np


d =pd.DataFrame(np.random.rand(3, 2),
                columns=['food', 'drink'],index=['a', 'b', 'c'])
print(d)        
         * عمليات حسابية مع اعمدة
import pandas as pd
w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})
grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
grades['Total'] = (grades['Math'] + grades['French'] + 
      grades['Chemistry']+ grades['Physics']) /100
print(grades)
         * صيغة اخري
import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])


result = (df['A'] + df['B']) / (df['C'] - 1)
print(df)
print(result)




         * صيغة اخري
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])


result = pd.eval("(df.A + df.B) / (df.C - 1)")


print(df)
print(result)




         * اظهار صفوف بشروط محددة  
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
result = df.query('A < 0.5 and B < 0.5')
print(df)
print(result)
         * صيغة اخري
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
tmp1 = df.A < 0.5
tmp2 = df.B < 0.5
tmp3 = tmp1 & tmp2
result = df[tmp3]
print(df)
print(result)
         * صيغة اخري
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
result = df[(df.A < 0.5) & (df.B < 0.5)]
print(df)
print(result)
         * صيغة اخري
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
result = df[(df.A < 0.5) | (df.B < 0.5)]
print(df)
print(result)
         * باستخدام دالة لإنشاء الجدول 
import pandas as pd
def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind] for c in cols}
    return pd.DataFrame(data, ind)
print(make_df('ABC', range(3)))
         * مزج الجداول
import pandas as pd
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering',
                              'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
print(df1)
print(df2)
df3 = pd.merge(df1, df2)
print('--------------------------')
print(df3)
         * مزج الجداول
import pandas as pd
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering',
                              'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.merge(df1, df2)
print(df3)
print('--------------------------')
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
df5 = pd.merge(df3, df4)
print(df4)
print('--------------------------')
print(df5)


         * مثال
import pandas as pd
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 
                              'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})


df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})


print(df1)
print(df3)
print(pd.merge(df1, df3, left_on="employee", right_on="name"))




         * حذف أعمدة        
import pandas as pd
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 
                              'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})


df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})


print(df1)
print(df3)
print(pd.merge(df1, df3, left_on="employee",
               right_on="name").drop('name', axis=1))




         * تغيير المفتاح
import pandas as pd
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 
                              'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})


df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})


print(df1)


df2 = df1.set_index('employee')


print(df2)




         * تقاطع البيانات
import pandas as pd
df1 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                    columns=['name', 'food'])


df2 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['cola', '7 up']},
                    columns=['name', 'drink'])
print(df1)
print('-----------------------------')
print(df2)
print('-----------------------------')
df3 = pd.merge(df1, df2)
print(df3)




         * تقاطع البيانات
import pandas as pd
df1 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                    columns=['name', 'food'])


df2 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['cola', '7 up']},
                    columns=['name', 'drink'])
print(df1)
print('-----------------------------')
print(df2)
print('-----------------------------')
df3 = pd.merge(df1, df2, how='inner')
print(df3)




         * جميع الصفوف
import pandas as pd
df1 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                    columns=['name', 'food'])


df2 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['cola', '7 up']},
                    columns=['name', 'drink'])
print(df1)
print('-----------------------------')
print(df2)
print('-----------------------------')
df3 = pd.merge(df1, df2, how='outer')
print(df3)




         * الجدول الأيمن كامل
import pandas as pd
df1 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                    columns=['name', 'food'])


df2 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['cola', '7 up']},
                    columns=['name', 'drink'])
print(df1)
print('-----------------------------')
print(df2)
print('-----------------------------')
df3 = pd.merge(df1, df2, how='right')
print(df3)




         * الجدول الأيسر كامل
import pandas as pd
df1 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                    columns=['name', 'food'])


df2 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['cola', '7 up']},
                    columns=['name', 'drink'])
print(df1)
print('-----------------------------')
print(df2)
print('-----------------------------')
df3 = pd.merge(df1, df2, how='left')
print(df3)


         * بيانات إحصائية
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': np.random.rand(10),'B': np.random.rand(10)})
print(df)
print('------------------------------')
print(df.sum())
print('------------------------------')
print(df.prod())
print('------------------------------')
print(df.mean())
         * بيانات إحصائية عمود معين 
import pandas as pd
import numpy as np


df = pd.DataFrame({'A': np.random.rand(10),'B': np.random.rand(10)})
print(df)
print('------------------------------')
print(df['A'].sum())
print('------------------------------')
print(df['B'].prod())
print('------------------------------')
print(df['A'].mean())


         * دمج بيانات الأعمدة
import pandas as pd
import numpy as np


df = pd.DataFrame({'A': np.random.rand(10),'B': np.random.rand(10)})
print(df)
print('------------------------------')
print(df.mean(axis='columns'))


         * بيانات إحصائية للصفوف
import pandas as pd
import numpy as np
df = pd.DataFrame({'A': np.random.rand(10),'B': np.random.rand(10)})
print(df)
print('------------------------------')
print(df.mean(axis='rows'))
print('------------------------------')
print(df.count())
print('------------------------------')
print(df.min())
print('------------------------------')
print(df.max())
print('------------------------------')
print(df.std())
print('------------------------------')
         * بيانات إحصائية
import pandas as pd
df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])
print(df)
print(df.describe())
         * مجموع قيم متشابهة
import pandas as pd


df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])


print(df)
print(df.groupby('key').sum())




         * بيانات إحصائية لقيم متشابهة
import pandas as pd


df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])


print(df)
print(df.groupby('key').describe())




         * فك القيم الإحصائية
import pandas as pd


df = pd.DataFrame({'key':['A','B','C','A','B','C'],
                   'data': range(6)},columns=['key', 'data'])


print(df)
print(df.groupby('key').describe().unstack())




         * المجموعات
import pandas as pd
import numpy as np


df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])


print(df)
df2 = df.groupby('key').aggregate({'data1': 'min','data2': 'max'})
print(df2)


         * الفلتر
import pandas as pd
import numpy as np


df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])


print(df)
def filter_func(x):
    return x['data2'].std() > 4


df2 = df.groupby('key').filter(filter_func)
print(df2)




         * تطبيق لمبدأ
import pandas as pd
import numpy as np


df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': np.random.randint(0, 10, 6)},
                    columns = ['key', 'data1', 'data2'])


print(df)


df2 = df.groupby('key').transform(lambda x: x**2)


print(df2)


MultiIndex






         * هي أداة للتعامل مع الجداول , والتي غالبا ما تكون ثلاثية الابعاد 
         * كتابة جدول و اظهاره   
import pandas as pd
index = [('California', 2000),('California', 2010),
         ('New York', 2000),('New York', 2010),
         ('Texas', 2000),('Texas', 2010)]
populations = [10000,15000,
               20000,25000,
               30000,35000]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(populations, index=index)
pop = pop.reindex(index)
print(pop)
         * سنة محددة  
import pandas as pd
index = [('California', 2000),('California', 2010),
         ('New York', 2000),('New York', 2010),
         ('Texas', 2000),('Texas', 2010)]
populations = [10000,15000,
               20000,25000,
               30000,35000]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(populations, index=index)
pop = pop.reindex(index)
print(pop[:, 2010])


         * تدوير البيانات  
import pandas as pd
index = [('California', 2000),('California', 2010),
         ('New York', 2000),('New York', 2010),
         ('Texas', 2000),('Texas', 2010)]
populations = [10000,15000,
               20000,25000,
               30000,35000]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(populations, index=index)
pop = pop.reindex(index)
print(pop.unstack())
         * زيادة عمود  
import pandas as pd
index = [('California', 2000),('California', 2010),
         ('New York', 2000),('New York', 2010),
         ('Texas', 2000),('Texas', 2010)]
populations = [10000,15000,
               20000,25000,
               30000,35000]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(populations, index=index)
pop = pop.reindex(index)


pop_df = pd.DataFrame({'total': pop,
                       'under18':[9267089, 9284094,4687374,
                                  4318033,5906301, 6879014]})


print(pop)
print(pop_df)






         * نفس النتيجة باستخدام dataframe  
import pandas as pd
        
import numpy as np
df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'],
                         [1, 2, 1, 2]],columns=['income', 'profit'])
print(df)


         * نفس الأمر  
import pandas as pd


data = {('California', 2000): 10000,('California', 2010):15000,
        ('Texas', 2000): 20000,('Texas', 2010): 25000,
        ('New York', 2000): 30000,('New York', 2010): 35000}
df = pd.Series(data)
print(df)


         * بيانات متداخلة  
import pandas as pd
import numpy  as np


index = pd.MultiIndex.from_product([[2013, 2014],[1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'],
                                      ['HR', 'Temp']],
                                    names=['subject', 'type'])
data = np.round(np.random.randn(4, 6))
health_data = pd.DataFrame(data, index=index, columns=columns)


print(health_data)


         * اختيارات محددة  
import pandas as pd
import numpy  as np
index = pd.MultiIndex.from_product([[2013, 2014],[1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'],
                                      ['HR', 'Temp']],
                                    names=['subject', 'type'])
data = np.round(np.random.randn(4, 6))
health_data = pd.DataFrame(data, index=index, columns=columns)
print(health_data['Guido', 'HR'])
         * تحديد بيانات
import pandas as pd
import numpy  as np
index = pd.MultiIndex.from_product([[2013, 2014],[1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'],
                                      ['HR', 'Temp']],
                                    names=['subject', 'type'])
data = np.round(np.random.randn(4, 6))
health_data = pd.DataFrame(data, index=index, columns=columns)
print(health_data.loc[:, ('Bob', 'HR')])
         * اقتطاع شريحة  
import pandas as pd
import numpy  as np
index = pd.MultiIndex.from_product([[2013, 2014],[1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'],
                                      ['HR', 'Temp']],
                                    names=['subject', 'type'])
data = np.round(np.random.randn(4, 6))
health_data = pd.DataFrame(data, index=index, columns=columns)
  idx = pd.IndexSlice
print(health_data.loc[idx[:, 1], idx[:, 'HR']])
أدوات أخري




         * التعامل مع النصوص String  
         * ويكون هذا بالأمر : 
pd.Series(data).str
         * مثال
import pandas as pd


data = ['peter', 'Paul', 'MARY', '15' , '  ' ]
print( pd.Series(data).str.len()) # length
print( pd.Series(data).str.startswith('p'))# is it start with "p"
print( pd.Series(data).str.endswith('Y')) #does is end with "r"


         * بحث عن حرف
import pandas as pd


data = ['peter', 'Paul', 'MARY', '15' , '  ' ]
print( pd.Series(data).str.find('t')) # find this letter
print( pd.Series(data).str.rfind('A'))# find it from right
         * عمل فراغات جوار الكلمة 
import pandas as pd


data = ['peter', 'Paul', 'MARY', '15' , '  ' ]
print( pd.Series(data).str.rjust(20))# adjust from right
print( pd.Series(data).str.ljust(50))# adjust from left




         * عمل اصفار
import pandas as pd
data = ['peter', 'Paul', 'MARY', '15' , '  ' ]
print( pd.Series(data).str.center(10))# make it center 
print( pd.Series(data).str.zfill(5))# fill zeros
         * فحص حالات الكلمات
import pandas as pd


data = ['peter', 'Paul', 'MARY', '15' , '  ' ]
 print( pd.Series(data).str.isupper())# is it all calpital
print( pd.Series(data).str.islower())# is it lower ? 
print( pd.Series(data).str.istitle())# is like like "This"
print( pd.Series(data).str.isspace())# is it all spaces ? 
print( pd.Series(data).str.isdigit())# is it numbers ?
print( pd.Series(data).str.isalpha())# is it all letters ?
print( pd.Series(data).str.isalnum())# is it not got any spaces ? 
print( pd.Series(data).str.isdecimal())# is it decimals ? 
print( pd.Series(data).str.isnumeric()) # is it number
print( pd.Series(data).str.upper())# make it capital
print( pd.Series(data).str.capitalize())# make it like 'This'
print( pd.Series(data).str.lower())# make it lower
print( pd.Series(data).str.swapcase())# switch capital & small




         * التعامل مع التواريخ
import pandas as pd


x = pd.to_datetime("4th of July, 2018")
 
print(x)




         * زيادة ايام
import pandas as pd
import numpy as np
x = pd.to_datetime("4th of July, 2018")
 y = x + pd.to_timedelta(np.arange(20),'D')
print(x)
print(y)
         * نقص ايام
import pandas as pd
import numpy as np
x = pd.to_datetime("4th of July, 2018")
 y = x - pd.to_timedelta(np.arange(20),'D')
print(x)
print(y)
         * سلسلة ايام
import pandas as pd
index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04','2015-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)
print(data)
         * ايام محددة
import pandas as pd
index = pd.DatetimeIndex(['2011-03-12', '2012-08-21',
                          '2013-07-11','2014-11-08'])
data = pd.Series([0, 1, 2, 3], index=index)
print(data['2011-01-01':'2012-12-31'])
         * سنة محددة  
import pandas as pd
index = pd.DatetimeIndex(['2011-03-12', '2012-08-21',
                          '2013-07-11','2014-11-08'])
data = pd.Series([0, 1, 2, 3], index=index)
print(data['2012'])
         * شهر محدد  
import pandas as pd
index = pd.DatetimeIndex(['2011-03-12', '2012-08-21',
                          '2013-07-11','2014-11-08'])
data = pd.Series([0, 1, 2, 3], index=index)
print(data['2012-08'])
         * من كذا لكذا  
import pandas as pd
data = pd.date_range('2011-12-25', '2012-01-08')
print(data)
         * عدد من الايام  
import pandas as pd
data = pd.date_range('2011-12-25', periods=8)
print(data)
         * عدد من الساعات  
import pandas as pd
data = pd.date_range('2011-12-25', periods=8, freq='H')
print(data)
         * عشر ساعات  
import pandas as pd
data = pd.timedelta_range(0, periods=10, freq='H')
print(data)
         * خطوات بالساعة والدقيقة والثانية  
import pandas as pd
data = pd.timedelta_range(0, periods=9, freq="2H30T40S")
print(data)
         * أيام العمل Business Days  
import pandas as pd
from pandas.tseries.offsets import BDay
data = pd.date_range('2018-07-01', periods=5, freq=BDay())
print(data)
         * قراءة ملفات csv  
import pandas as pd
df = pd.read_csv('D:\\1.csv')
print(df.head()) 


==================================================


Id        SepalLengthCm        SepalWidthCm        PetalLengthCm        PetalWidthCm        Species
1        5.1        3.5        1.4        0.2        Iris-setosa
2        4.9        3        1.4        0.2        Iris-setosa
3        4.7        3.2        1.3        0.2        Iris-setosa
4        4.6        3.1        1.5        0.2        Iris-setosa
5        5        3.6        1.4        0.2        Iris-setosa
6        5.4        3.9        1.7        0.4        Iris-setosa
7        4.6        3.4        1.4        0.3        Iris-setosa
8        5        3.4        1.5        0.2        Iris-setosa
9        4.4        2.9        1.4        0.2        Iris-setosa
10        4.9        3.1        1.5        0.1        Iris-setosa
11        5.4        3.7        1.5        0.2        Iris-setosa
12        4.8        3.4        1.6        0.2        Iris-setosa
13        4.8        3        1.4        0.1        Iris-setosa
14        4.3        3        1.1        0.1        Iris-setosa
15        5.8        4        1.2        0.2        Iris-setosa
16        5.7        4.4        1.5        0.4        Iris-setosa
17        5.4        3.9        1.3        0.4        Iris-setosa
18        5.1        3.5        1.4        0.3        Iris-setosa
19        5.7        3.8        1.7        0.3        Iris-setosa
20        5.1        3.8        1.5        0.3        Iris-setosa
21        5.4        3.4        1.7        0.2        Iris-setosa


 


         * البداية بعمود محدد
import pandas as pd
data=pd.read_csv('D:\\1.csv', index_col='SepalWidthCm')
print(data)




         * الحفظ في ملف
import pandas as pd




w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})


grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})


print(grades)
grades.to_csv('D:\\2.csv')




         * حفظ في ملف اكسل  
import pandas as pd




w = pd.Series({'a':1 ,'b':2 ,'c':3 ,'d':4 ,'e':5})
x = pd.Series({'a':6 ,'b':7 ,'c':8 ,'d':9 ,'e':10})
y = pd.Series({'a':11 ,'b':12 ,'c':13 ,'d':14 ,'e':15})
z = pd.Series({'a':16 ,'b':17 ,'c':18 ,'d':19 ,'e':20})


grades = pd.DataFrame({'Math':w,'Physics':x,'French':y,'Chemistry':z})
print(grades)
grades.to_excel('D:\\1.xls',sheet_name ='Sheet 1')




         * قراءة من ملف اكسل أو csv  
import pandas as pd


grades1 = pd.read_csv('D:\\2.csv')
grades2 = pd.read_excel('D:\\1.xls')


print(grades1)
print(grades2)




         * فتح ملف و قراءته  
from pandas import read_csv
filename = 'D:\\2.csv'
names = ['a', 'b', 'c', 'd', 'e']
data = read_csv(filename, names=names)
print(data)




         * قراءة ملف و عمل بيانات إحصائية عنه  
from pandas import read_csv
from pandas import set_option
filename = "D:\\pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
set_option('display.width', 100)
set_option('precision', 3)
description = data.describe()
print(description)




         * بيانات إحصائية مع عمل group  لها  
# Class Distribution
from pandas import read_csv
filename = "D:\\pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
class_counts = data.groupby('class').size()
print(class_counts)




         * معامل الارتباط  
from pandas import read_csv
from pandas import set_option
filename = "D:\\pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
set_option('display.width', 100)
set_option('precision', 3)
correlations = data.corr(method='pearson')
print(correlations)




         * قيم الانحراف  
from pandas import read_csv
filename = "D:\\pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
skew = data.skew()
print(skew)




________________




Matplotlib


         * هي من المكتبات الحيوية  , المستخدمة لتحليل و رسم  البيانات
  

         * غالبا ما يتم استخدام مكتبة pyplot   منها بأحد الأمرين
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


         * معرفة الإصدار
import matplotlib 
print(matplotlib.__version__)
         * لها عدد من الأبواب , وهي :
- Style
- Plot
- Scatter         
- Pie
- Bar
- Histogram
- Contour
- 3D
- Subplot                
- Annotate
- Imshow
- Legend        


1 . Style


         * هي باقة لونية متعلقة بالرسم , ويتم تحديدها لتحديد شكل الرسم الناتج
         * تتم عبر الأمر 
plt.style.use('      ')
         * الباقات هي : 
plt.style.use('bmh')
  



plt.style.use('classic')
  















plt.style.use('dark_background')
  



plt.style.use('fivethirtyeight')
  



plt.style.use('ggplot')
  



plt.style.use('grayscale')
  











plt.style.use('seaborn-bright')
  

plt.style.use('seaborn-colorblind')
  



plt.style.use('seaborn-dark')
  



plt.style.use('seaborn-dark-palette')
  











plt.style.use('seaborn-darkgrid')
  

plt.style.use('seaborn-deep')
  

plt.style.use('seaborn-muted')
  

plt.style.use('seaborn-notebook')
  



plt.style.use('seaborn-paper')
  







plt.style.use('seaborn-pastel')
  

plt.style.use('seaborn-poster')
  



plt.style.use('seaborn-talk')
  



plt.style.use('seaborn-ticks')
  



plt.style.use('seaborn-white')
  



plt.style.use('seaborn-whitegrid')
   
2 . Plot




         * يستخدم للرسم البياني , للخطوط و المنحنيات , علي ان تكون من بعدين 
         * تستخدم الأمر 
plt.plot(    )
         * رسم بياني تقليدي
import matplotlib.pyplot as plt
a = ( 1,2,3,6,5,8,7,4)
plt.plot(a)


  



         * لو اخدت 2 ليست , فسيتم رسمها اكس و واي
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.plot(a,b)


  



         * تغيير الستايل عشان اشوف جريد
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
plt.plot(a,b)
  



         * دالة الـ   sin  
import matplotlib.pyplot as plt
import numpy as np
plt.style.use ('ggplot')
x = np.linspace(0, 10) 
y = np.sin(x) 
plt.plot(x, y)
  

         * دالة الـ cos  
import matplotlib.pyplot as plt
import numpy as np
plt.style.use ('ggplot')
x = np.linspace(0, 10) 
y = np.cos(x) 
plt.plot(x, y)


  

         * تحديد أسماء المحاور
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
plt.ylabel('Time')
plt.xlabel('Work')
plt.plot(a,b)


  

         * بطريقة أخرى
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()
ax.set_xlabel('Time')
ax.set_ylabel('Work')


plt.plot(a,b)


  

         * بطريقة أخرى
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()


ax.set(xlabel='Time', ylabel='Work' )


plt.plot(a,b)


  

         * تحديد المارك
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()


ax.set(xlabel='Time', ylabel='Work' )
plt.plot(a,b,marker='o')


  

         * حجم المارك
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()


ax.set(xlabel='Time', ylabel='Work' )
plt.plot(a,b,marker='o',markersize=11)


  

         * تحديد لون الخط
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()


ax.set(xlabel='Time', ylabel='Work' )
plt.plot(a,b,color='blue',marker='o',markersize=11)


  



         * طرق كتابة اللون


plt.plot(a,b,color='blue',marker='o',markersize=11) #color name
plt.plot(a,b,color='g',marker='o',markersize=11) #color litter
plt.plot(a,b,color='0.75',marker='o',markersize=11) # its degree from B&W
plt.plot(a,b,color='#FFDD44',marker='o',markersize=11) # its code
plt.plot(a,b,color=(1.0,0.2,0.3),marker='o',markersize=11) #its RGB degrees
plt.plot(a,b,color='chartreuse',marker='o',markersize=11) #its name in html




         * عنوانه
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()


ax.set(xlabel='Time', ylabel='Work' )
plt.title('time/work consumption')
plt.plot(a,b,color='blue',marker='o',markersize=11) 


  

         * نفس الأمر
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()


ax.set(xlabel='Time', ylabel='Work' )
ax.set_title('time/work consumption')


plt.plot(a,b,color='blue',marker='o',markersize=11)


  

         * نفس الأمر
import matplotlib.pyplot as plt
a = (1,2,3,4,5,6)
b = (3,9,10,12,16,18)
plt.style.use ('ggplot')
ax = plt.axes()


ax.set(xlabel='Time', ylabel='Work' )
ax.set(title='time/work consumption')
plt.plot(a,b,color='blue',marker='o',markersize=11)


  

         * دالة مركبة
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.005)
y = np.exp(-x/2) * np.sin(2*np.pi*x)
plt.plot (x,y)


  





         * رسم دالتين معا
import matplotlib.pyplot as plt
import numpy as np
def p1(x):  return x**4 - 4*x**2 + 3*x
def p2(x):  return np.sin(10*x)*10
x = np.linspace(-3,3,1000)
plt.plot(x,p1(x),x,p2(x))
  

         * نوع الخط المستخدم
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.005)


plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='-')


plt.plot(x, x + 4, linestyle='dashed')
plt.plot(x, x + 5, linestyle='--')


plt.plot(x, x + 8, linestyle='dashdot')
plt.plot(x, x + 9, linestyle='-.')


plt.plot(x, x + 12, linestyle='dotted')
plt.plot(x, x + 13, linestyle=':')


  

         * لون وستايل الخط
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.005)


plt.plot(x,x+0,'b--')
plt.plot(x,x+3,'g-')
plt.plot(x,x+6,'r-.')
plt.plot(x,x+9,'y:')


  

         * سمك الخط
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.005)
plt.plot(x,x+0,'b-',linewidth = 1)
plt.plot(x,x+3,'b-',linewidth = 5)
plt.plot(x,x+6,'b-',linewidth = 11)
plt.plot(x,x+9,'b-',linewidth = 20)
  



         * الوان الخطوط
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.005)


plt.plot(x, x + 0, color = 'b')
plt.plot(x, x + 2, color = 'g')
plt.plot(x, x + 4, color = 'y')
plt.plot(x, x + 6, color = 'r')
plt.plot(x, x + 8, color = 'c')
plt.plot(x, x + 10, color = 'm')
plt.plot(x, x + 12, color = 'k')
plt.plot(x, x + 14, color = 'w')


  

         * خطوط و نقاط
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.5)


plt.plot(x, x + 0, '-')
plt.plot(x, x + 5, 'o')
plt.plot(x, x + 10, '-o')


  



         * شكل النقاط
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.5)


plt.plot(x,x,'--')
plt.plot(x,x+3,'o')
plt.plot(x,x+6,'^')
plt.plot(x,x+9,'.')


  



import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.5)


plt.plot(x,x+9,'>')
plt.plot(x,x+6,'v')
plt.plot(x,x+3,'o')
plt.plot(x,x,',')
  

import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.5)


plt.plot(x,x+12,'<')
plt.plot(x,x+9,'1')
plt.plot(x,x+6,'2')
plt.plot(x,x+3,'3')
plt.plot(x,x,'4')
  

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.5)


plt.plot(x,x+12,'8')
plt.plot(x,x+9,'s')
plt.plot(x,x+6,'P')
plt.plot(x,x+3,'p')
  

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.5)


plt.plot(x,x+12,'*')
plt.plot(x,x+9,'h')
plt.plot(x,x+6,'x')
plt.plot(x,x+3,'+')


  



import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.5)


plt.plot(x,x+12,'d')
plt.plot(x,x+9,'|')
plt.plot(x,x+6,'_')


  



         * الالوان مع شكل المارك
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.5)


plt.plot(x,x+12,'r*')
plt.plot(x,x+9,'gh')
plt.plot(x,x+6,'bx')
plt.plot(x,x+3,'y+')


  



         * أكثر من دالة في نفس السطر
import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,10,0.5)


plt.plot(x,x,'r--',x,x**2,'bo',x,x**3,'g^')


  







         * مثال
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,10,0.05)
y = np.exp(-x/3)*np.sin(3*np.pi*x)
z = np.exp(x/2)*np.sin(3*np.pi*x)
w  = np.exp(x/2)**np.cos(4*np.pi*x)


plt.plot(x,y,'b',x,z,'g',x,w,'r')


  

         * مثال
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 500)
y = np.cumsum(np.random.randn(500, 6), 0)


plt.plot(x, y)


  

         * قيمة التفاوت 
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
dy = 0.2
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.b');


  

         * مثال
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
dy = 1.2
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='.r');


  

         * مثال
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
dy = 1.2
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, yerr=dy, fmt='o',
             color='black', ecolor='lightgray',
             elinewidth=3, capsize=0)


  

         * التفاوت الأفقي
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
dy = 1.2
y = np.sin(x) + dy * np.random.randn(50)
plt.errorbar(x, y, xerr=dy, fmt='.r')
  

         * قراءة من ملف و رسم بيانات
import matplotlib.pyplot as plt
def extract_data(filename):
    infile = open(filename, 'r')
    infile.readline() # skip the first line
    numbers = []
    for line in infile:
        words = line.split()
        number = float(words[1])
        numbers.append(number)
    infile.close()
    return numbers
values = extract_data('D:\\2.txt')
print(values)
month_indices = range(1, 13)
plt.plot(month_indices, values[:-1], '*r')


Average rainfall (in mm) in Rome: 1188 months between 1782 and 1970
Jan 81.2
Feb 63.2
Mar 70.3
Apr 55.7
May 53.0
Jun 36.4
Jul 17.5
Aug 27.5
Sep 60.9
Oct 117.7
Nov 111.0
Dec 97.9
Year 792.9
  

         * أمثلة عامة
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,10,0.05)
y = np.exp(-x/3)**np.cos(3*np.pi*x)


plt.plot(x,y)


  



import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,10,0.05)
y = np.exp(-x/3)*np.cos(3*np.pi*x)
plt.plot(x,y)


  



import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,10,0.05)
y = np.exp(-x/3)*np.sin(3*np.pi*x)
plt.plot(x,y)


  

3 . Scatter


         * هي لعمل الرسم البياني مستخدما نقاط , وليس خطوط
         * تأخذ قيمتي x  و y   (الزامي )
         * تأخذ لون النقاط  c  (اختياري)
         * تأخذ حجم النقاط  s   (اختياري)
         * تأخذ الشفافية alpha   (اختياري)


import matplotlib.pyplot as plt
import numpy as np


x=np.random.rand(500)
y=np.random.rand(500) 
plt.scatter(x,y)


  

         * التوزيع الطبيعي
import matplotlib.pyplot as plt
import numpy as np


x=np.random.normal(0,1,1000)
y=np.random.normal(0,1,1000)
plt.scatter(x,y)


  

         * اللون : بنفس عدد العناصر
import matplotlib.pyplot as plt
import numpy as np


x=np.random.normal(0,1,1000)
y=np.random.normal(0,1,1000)
z=np.random.normal(0,1,1000) 
plt.scatter(x,y,c=z)


  

         * الحجم
import matplotlib.pyplot as plt
import numpy as np


x=np.random.normal(0,1,1000)
y=np.random.normal(0,1,1000)
z=np.random.normal(0,1,1000)
w=50*np.random.normal(0,1,1000) 




plt.scatter(x,y,s=w,c=z)


  

         * مثال
import matplotlib.pyplot as plt


x=[1,2,3,4,5,6,7,8,9,10]
y=[4,7,8,3,0,5,9,4,1,9]
w=[600,900,800,700,400,200,300,100,600,300]
z=[7,5,6,9,8,5,6,3,2,1]
plt.scatter(x,y,s=w,c=z)
plt.show()


  

         * الشفافية
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
cl = rng.rand(100)
sz = 1000 * rng.rand(100)
plt.scatter(x, y,c=cl,s=sz,alpha=0.3)


plt.show()


  

         * عمود الالوان
import matplotlib.pyplot as plt
import numpy as np
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
cl = rng.rand(100)
sz = 1000 * rng.rand(100)
plt.scatter(x, y,c=cl,s=sz,alpha=0.3)
plt.colorbar()
plt.show()


  

________________


4. Pie


         * لعمل الاشكال البيانية علي هيئة قرص 
import matplotlib.pyplot as plt
plt.pie([15,30,45,10])
plt.show()


  

         * لجعل الدائرة متساوية الابعاد
import matplotlib.pyplot as plt
plt.pie([15,30,45,10])
plt.axis('equal')
plt.show()
  



         * تسمية القطع
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'))


plt.axis('equal')


plt.show()


  

         * ابعاد الاجزاء
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'),
        explode = [0.1,0.1,0.1,0.1])


plt.axis('equal')


plt.show()


  

         * تطبيق
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'),
        explode = [0,-0.2,0.3,1])


plt.axis('equal')


plt.show()


  

         * النسبة المئوية
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'),
        explode = [0.1,0.1,0.1,0.1],autopct ='%1.1f%%')


plt.axis('equal')


plt.show()


  

         * عمل ظل
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'),
        explode = [0.1,0.1,0.1,0.1],autopct ='%1.1f%%'
        ,shadow = True)


plt.axis('equal')


plt.show()


  

         * زاوية البداية
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'),
        explode = [0.1,0.1,0.1,0.1],autopct ='%1.1f%%'
        ,shadow = True,startangle = 90)


plt.axis('equal')


plt.show()


  

         * مثال
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'),
        explode = [0.1,0.1,0.1,0.1],autopct ='%1.1f%%'
        ,shadow = True,startangle = 180)


plt.axis('equal')


plt.show()


  

         * مسافة الكلام عن الشرائح
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'),
        explode = [0.1,0.1,0.1,0.1],autopct ='%1.1f%%'
        ,shadow = True, startangle = 180,
        labeldistance = 1.5)


plt.axis('equal')


plt.show()


  

         * مسافة النسبة المئوية
import matplotlib.pyplot as plt


plt.pie([15,30,45,10],labels=('Egypt','Syria','Tunise','Morroco'),
        explode = [0.1,0.1,0.1,0.1],autopct ='%1.1f%%'
        ,shadow = True, startangle = 180,
        labeldistance = 1.5, pctdistance =1.2)
plt.axis('equal')
plt.show()


  

________________


5. Bar


         * هي لرسم البيانات بالأعمدة
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,20,20)
y = np.random.randint(50,size = 20)


plt.bar(x , y)


  

         * سمك العمود
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,20,20)
y = np.random.randint(50,size = 20)


plt.bar(x,y,width=0.9)


  

         * اللون
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,20,20)
y = np.random.randint(50,size = 20)


plt.bar(x,y,width=0.9,color='r')


  

         * الشفافية
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,20,20)
y = np.random.randint(50,size = 20)


plt.bar(x,y,width=0.9,color='r',alpha=.5)


  

         * اللون الداخلي ولون الوجه
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,20,20)
y = np.random.randint(50,size = 20)
plt.bar(x,y,facecolor='r',edgecolor ='g')


  

         * عمل اسم للجراف
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,20,20)
y = np.random.randint(50,size = 20)


plt.bar(x,y,facecolor='r',edgecolor ='g')
plt.text(7, -9, 'Polulation Denisty', style='italic',
        bbox={'facecolor':'blue', 'alpha':0.5, 'pad':10})


  

         * ارقام فوق العواميد
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,20,20)
y = np.random.randint(50,size = 20)


plt.bar(x,y,facecolor='r',edgecolor ='g')
plt.text(7, -9, 'Polulation Denisty', style='italic',
        bbox={'facecolor':'blue', 'alpha':0.5, 'pad':15})


for xx , yy in zip(x,y): 
    plt.text(xx,yy,yy)# location of text the value
  



         * تعديل مكان الارقام
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,20,20)
y = np.random.randint(50,size = 20)


plt.bar(x,y,facecolor='r',edgecolor ='g')
plt.text(7, -9, 'Polulation Denisty', style='italic',
        bbox={'facecolor':'blue', 'alpha':0.5, 'pad':15})


for xx , yy in zip(x,y): 
    plt.text(xx,yy,yy,ha='center',va='bottom')# adjusting them


  

         * جرافين معا
import matplotlib.pyplot as pl
import numpy as np
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
pl.bar(X, +Y1, color='r',alpha = 0.5)
pl.bar(X, -Y2, facecolor='b',alpha = 0.5)
for x, y in zip(X, Y1):
    pl.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    pl.ylim(-1.25, +1.25)
  
________________

6. Histogram


         * وهو امر خاص بالتكتلات , سواء اعمدة او نقاط
         * مثال بسيط
import numpy as np
import matplotlib.pyplot as plt


data = np.random.randn(5000)
plt.hist(data)


  

         * خصائص
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(5000)


plt.hist(data, bins=50, normed=True,
         alpha=0.5,histtype='step',color='blue')


  

         * خصائص
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(5000)


plt.hist(data, bins=50, normed=True,
         alpha=0.5,histtype='bar',color='r')


  

         * جرافين معا
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
    plt.hist(data[col], normed=True, alpha=1)


  

         * اكثر من واحد
import numpy as np
import matplotlib.pyplot as plt




x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)


plt.hist(x1,histtype='bar',
         alpha=0.3, normed=True, bins=100)
plt.hist(x2,histtype='step',
         alpha=0.7, normed=True, bins=100)
plt.hist(x3,histtype='stepfilled',
         alpha=1, normed=True, bins=100)


  

         * بطريقة اخري
import numpy as np
import matplotlib.pyplot as plt




x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)




kwargs = dict(histtype='stepfilled',
              alpha=0.6, normed=True,
              bins=40)
 
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs);


  

         * الأمر  hist2d  خاص بمدي ترابط النقاط المتقاطعة
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(20)
y = np.random.rand(20)


print(x)
print('===================')
print(y)


plt.hist2d(x, y)


  

         * اعداد اكبر
import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(200)
y = np.random.rand(200)
plt.hist2d(x, y)


  

         * الالوان
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(200)
y = np.random.rand(200)


plt.hist2d(x, y, cmap='Reds')


  

         * عدد النقاط
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(200)
y = np.random.rand(200)


plt.hist2d(x, y, cmap='Blues', bins=30)


  

         * قائمة الالوان
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(200)
y = np.random.rand(200)


plt.hist2d(x, y, cmap='Blues', bins=30)
plt.colorbar()


  

         * اسم قائمة الالوان
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(200)
y = np.random.rand(200)


plt.hist2d(x, y, cmap='Blues', bins=30)
a = plt.colorbar()
a.set_label('counts in bin')


  

         * أمر  hexbin    مشابه لكن بخلايا مسدسة
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(200)
y = np.random.rand(200)


plt.hexbin(x, y, gridsize=30, cmap='Blues')
a = plt.colorbar()
a.set_label('counts in bin')
  



         * معادلة
import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(200)
y= x**(1/3)


plt.hist2d(x, y, bins=30, cmap='Blues')
plt.colorbar()


  

         * التوزيع الطبيعي
import numpy as np
import matplotlib.pyplot as plt


mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T


plt.hist2d(x, y, bins=30, cmap='Blues')
plt.colorbar()


  

         * باستخدام امر hexbin  
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white') 


mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T


plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')


  
________________

7 . Contour


         * الامر كونتور يعمل رسم كانه ثلاثي الابعاد , ويقوم بايثون برسم خطوط الحدود
         * نعطيه قيم اكس وواي , ثم زد الارتفاع 
         * ويجب ان زد مصفوفة ثناية الابعاد , وتكون صفوفها  نفس قيم اكس و اعمدتها نفس قيم واي , والذي يقوم علي اساسها برسم الحدود , ونعطيه اللون 
plt.contour(X, Y, Z, colors='red'); 
         * مثال بسيط
import matplotlib.pyplot as plt


X = [1,2,3,4,5,6,7]
Y = [1,2,3,4,5,6,7]
Z = [[1,1,1,1,1,1,1],
     [1,2,2,2,2,2,1],
     [1,2,3,3,3,2,1],
     [1,2,3,4,3,2,1],
     [1,2,3,3,3,2,1],
     [1,2,2,2,2,2,1],
     [1,1,1,1,1,1,1]]
plt.contour(X, Y, Z, colors='red')


  

         * قيم عشوائية
import matplotlib.pyplot as plt
import numpy as np


X = np.random.randint(1,10,6)
Y = np.random.randint(1,10,6)
Z = np.random.randint(1,10,36)
ZZ = np.reshape(Z,(6,6))


plt.contour(X, Y, ZZ, colors='red')


  

         * تطبيق متداخل
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    e = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    return e


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, colors='red');
  



         * كثافة الخطوط
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    e = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    return e


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, 20, colors='b')
  

         * تدريج الالوان
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    e = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    return e


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, 20 , cmap='RdGy')


  

         * الامر   contourf  يقوم بعمل ملئ fill   للخطوط البينية
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    e = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    return e


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contourf(X, Y, Z, 20 , cmap='RdGy')


  

         * عمود الالوان
import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    e = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    return e


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contourf(X, Y, Z, 20 , cmap='RdGy')
plt.colorbar()


  

         * تفاصيل هامة علي الرسم
import matplotlib.pyplot as plt
import numpy as np
def f(x, y):
    e = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    return e


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
contours = plt.contour(X, Y, Z, 3,colors='black')
plt.clabel(contours, inline=True, fontsize=8)
plt.imshow(Z, extent=[0, 5, 0, 5],cmap='RdGy',alpha=0.5)
plt.colorbar()
  

         * ألوان دون خطوط
import matplotlib.pyplot as pl
import numpy as np
    
def f(x, y):
    return(1-x/2+x**5+y**3)* np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
pl.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
#C = pl.contour(X,Y,f(X,Y),8,colors='b')
  



         * خطوط دون ألوان
import matplotlib.pyplot as pl
import numpy as np
    
def f(x, y):
    return(1-x/2+x**5+y**3)* np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
#pl.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = pl.contour(X,Y,f(X,Y),8,colors='b')


  

         * ألوان و خطوط
import matplotlib.pyplot as pl
import numpy as np
    
def f(x, y):
    return(1-x/2+x**5+y**3)* np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
pl.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = pl.contour(X,Y,f(X,Y),8,colors='b')


  
________________

8 . 3D


         *  هي الاداة الاكثر اهمية لرسم رسوم ثلاثية الابعاد
         *  غالبا  ما نستخدمها مع مكتبة numpy  او pandas  لرسم البيانات الناتجة منهما 
         *  يتم استدعائها بالأمر :       
mpl_toolkits.mplot3d 
         * لرسم الفراغ المجسم
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')


  

         * أمر plot_surface  
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.25) # X Value
Y = np.arange(-4,4,0.25) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z) # Draw them
plt.show()


  

         * عمل اسماء للمحاور
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.25) # X Value
Y = np.arange(-4,4,0.25) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z) # Draw them


ax.set_xlabel('Time')
ax.set_ylabel('Work')
ax.set_zlabel('Efficiency')
plt.show()


  



         * باقات الألوان
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.25) # X Value
Y = np.arange(-4,4,0.25) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z,
                cmap ='hot') # Color
plt.show()


  

         * الباقات المستخدمة في أمر cmap   هي : 
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Vega10, Vega10_r, Vega20, Vega20_r, Vega20b, Vega20b_r, Vega20c, Vega20c_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
         * تغيير الدالة و اللون
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.25) # X Value
Y = np.arange(-4,4,0.25) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.cos(R) # Z Value


ax.plot_surface(X,Y,Z,
                cmap ='gray_r') # Color
plt.show()


  

         * تغيير الدالة و اللون
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.25) # X Value
Y = np.arange(-4,4,0.25) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = (np.sin(R))**2 # Z Value


ax.plot_surface(X,Y,Z,
                cmap ='terrain') # Color
plt.show()
  



         * تغيير الدالة و اللون
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.25) # X Value
Y = np.arange(-4,4,0.25) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = (np.sin(R))*(np.cos(R)) # Z Value


ax.plot_surface(X,Y,Z,
                cmap ='gist_stern') # Color
plt.show()
  



         * تغيير الدالة و اللون
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.25) # X Value
Y = np.arange(-4,4,0.25) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = (1/(X+5)**0.5)*(Y**2) # Z Value


ax.plot_surface(X,Y,Z,
                cmap ='RdYlGn') # Color
plt.show()




  

         * تغيير الخطوة   0.25  
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.01) # X Value
Y = np.arange(-4,4,0.01) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z,
                cmap ='hot') # Color
plt.show()


  

         * تغيير الخطوة   0.25  
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,1) # X Value
Y = np.arange(-4,4,1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z,
                cmap ='hot') # Color
plt.show()
  



         * تغيير ابعاد x  عن  y 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-10,10,0.1) # X Value
Y = np.arange(-5,5,0.1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z,
                cmap ='Blues') # Color
plt.show()


  

         * لون الحواف
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.1) # X Value
Y = np.arange(-4,4,0.1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z,cmap ='Blues'
                ,edgecolors='w') # Color
plt.show()


  

         * تحديد ابعاد   z   الاقصي و الادني
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.1) # X Value
Y = np.arange(-4,4,0.1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z,cmap ='hot')


ax.set_zlim(-0.5,0.5)
plt.show()
  



         * زاوية الرؤية
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure() #adjust 3D figure
ax = Axes3D(fig)
X = np.arange(-4,4,0.1) # X Value
Y = np.arange(-4,4,0.1) # Y Value
X,Y = np.meshgrid(X,Y) # combine them
R = np.sqrt(X**2 + Y**2) # function
Z = np.sin(R) # Z Value


ax.plot_surface(X,Y,Z,cmap ='hot')
ax.view_init(-50, 26)
plt.show()


  

         * أمر   plot3d    
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
 
ax = plt.axes(projection='3d')
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'b')
  



         * أمر scatter3D  
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
z = 15 * np.random.random(500)
x =np.sin(z)+0.1*np.random.randn(500)
y =np.cos(z)+0.1*np.random.randn(500)
ax.scatter3D(x,y,z,c=z,cmap='Reds')


  

         * الاثنين معا
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()


ax = plt.axes(projection='3d')
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'b')


z= 15 * np.random.random(100)
x= np.sin(z) + 0.1 * np.random.randn(100)
y= np.cos(z) + 0.1 * np.random.randn(100)
ax.scatter3D(x,y,z,c=z,cmap='Reds')


  

         * جزء محدد
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9*np.pi,0.8*np.pi, 40)
r, theta = np.meshgrid(r, theta)
X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,cmap='Reds')


  

         * تغيير الزاوية
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
r = np.linspace(0, 6, 20)
theta = np.linspace(-0.7*np.pi,0.2*np.pi, 40)
r, theta = np.meshgrid(r, theta)
X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,cmap='Reds')


  

         * أمر   trisurf
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
 
theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = r * np.sin(theta)
y = r * np.cos(theta)
z = f(x, y)


ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z,cmap='viridis')


  

         * أمر contour3D   مشابه لأمر  3D  الي حد ما مع فارق انه يرسم خطوط كونتور مش مجسم
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='Blues')
  



         * زيادة الارقام
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 500, cmap='Blues')
  



         * تقليل الارقام
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 10, cmap='Blues')


  

         * تغيير الدالة
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return np.cos(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 120, cmap='Blues')


  

         * دالة اخري
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return -(x**(2))
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 180, cmap='Blues')


  

         * أمر plot_wireframe    يقوم بعمل رسم شبيه بالشبكة
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return np.cos(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 20)
y = np.linspace(-6, 6, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')


ax.plot_wireframe(X, Y, Z, cmap='Blues')


  

         * أمر plot_surface بيعمل رسم للاسطح مش الاسلاك
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return np.cos(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 20)
y = np.linspace(-6, 6, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z)


  

         * تغيير اللون , ولون الخط
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 20)
y = np.linspace(-6, 6, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, edgecolor='w')


  

         * أمر scatter   يقوم بعمل نقاط بدل الخطوط
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
x = np.linspace(-6, 6, 20)
y = np.linspace(-6, 6, 20)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(X, Y, Z)


  

________________


9 . Subplot


         * وهي الأداة التي تسمح لنا بعمل اكثر من جراف في نفس الرسم 


         * وتكون عبر اعطاء امر plt.subplot  ثلاث قيم : 
         * الاولي و الثانية , هي صفوف و اعمدة مصفوفة الرسومات
         * الثالث هو ترتيب الرسم
plt.subplot(2,2,4)
         * يليها كتابة plt.plot  و تفاصيل الدالة


         * مثال
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(1,2,1)
y = 3*x
plt.plot(x,y,c='r')


  

         * مثال
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(1,2,1)
y = 3*x
plt.plot(x,y,c='r')


plt.subplot(1,2,2)
y = -3*x
plt.plot(x,y,c='g')


  

         * مثال خطأ لن يتم استخدامه
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(1,2,1)
y = 3*x
plt.plot(x,y,c='r')


plt.subplot(1,2,2)
y = -3*x
plt.plot(x,y,c='g')


plt.subplot(1,2,3)
y = 12*x
plt.plot(x,y)




         * مثال
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(2,1,1)
y = 3*x
plt.plot(x,y,c='r')


plt.subplot(2,1,2)
y = -3*x
plt.plot(x,y,c='g')


  

         * مثال
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(2,2,1)
y = 3*x
plt.plot(x,y,c='r')


plt.subplot(2,2,2)
y = -3*x
plt.plot(x,y,c='g')


plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')


plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')
  



         * يمكن كتابة الرقم بفواصل او بدون
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')


plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')


plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')


plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


  

         * شكل مختلف للامر
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


fig, ax = plt.subplots(5)
ax[0].plot(x,3*x)
ax[1].plot(x,-x/400)
ax[2].plot(x,300*(0.002*x+3))
ax[3].plot(x,np.sin(x))
ax[4].plot(x,x**0.1)


  

         * الابعاد و المسافات بين الجرافات
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


plt.subplots_adjust(left=0,right=1.5
                    ,bottom=0,top=1.5
                    ,wspace=0,hspace=0)
  



         * تغيير الابعاد
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


plt.subplots_adjust(left=1,right=1.5
                    ,bottom=0,top=1.8
                    ,wspace=0,hspace=0)


  

         * العكس
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


plt.subplots_adjust(left=0,right=1.5
                    ,bottom=1,top=1.5
                    ,wspace=0,hspace=0)


  

         * المسافات الراسية
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


plt.subplots_adjust(left=0,right=1.5
                    ,bottom=0,top=1.5
                    ,wspace=0.5,hspace=0)


  

         * المسافات الافقية
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


plt.subplots_adjust(left=0,right=1.5
                    ,bottom=0,top=1.5
                    ,wspace=0,hspace=0.9)


  





         * المسافتين 
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,100)


plt.subplot(221)
y = 3*x
plt.plot(x,y,c='r')
plt.subplot(222)
y = -3*x
plt.plot(x,y,c='g')
plt.subplot(2,2,3)
y = x**2
plt.plot(x,y,c='b')
plt.subplot(2,2,4)
y =  x**0.5
plt.plot(x,y,c='r')


plt.subplots_adjust(left=0,right=1.5
                    ,bottom=0,top=1.5
                    ,wspace=0.3,hspace=0.9)


  

         * كتابة نص في المربعات
import matplotlib.pyplot as plt


for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i))
    ,fontsize=18, ha='center')
  

         * محور اكس مشترك
import matplotlib.pyplot as plt    
fig, ax = plt.subplots(2, 3, sharex='col')


  



         * محور واي مشترك
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 3, sharey='row')


  

         * المحورين مشتركين
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 3, sharex ='col' ,sharey='row')


  

         * تحديد اكثر من جراف و تعيين الاماكن
import matplotlib.pyplot as plt


grid = plt.GridSpec(2, 3)
plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])


  





         * قيم مختلفة
import matplotlib.pyplot as plt
grid = plt.GridSpec(3, 5)
plt.subplot(grid[0, :1])
plt.subplot(grid[0, 1])
plt.subplot(grid[0, 2:])
plt.subplot(grid[1, :])
plt.subplot(grid[2, :4])
plt.subplot(grid[2, 4])


  

         * محاور دائرية
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0,1,0.001)
theta = np.pi*r*4
line, = ax.plot(theta, r, color='r', lw=3)
  



         * مثال
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0,1,0.001)
theta = np.pi*r*25
line, = ax.plot(theta, r, color='r', lw=3)


  

         * مثال
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0,1,0.001)
theta = np.tan(r*2)
line, = ax.plot(theta, r, color='r', lw=3)


  
________________

10 . Annotate






         * و هي تستخدم لعمل الاسهم و الكتابة فوقها علي الجراف , وتاخذ القيم  : 


         * الكلام المكتوب جوار السهم
         *  موضع السهم (xy)
         *  موضع الكتابة (xytext)


         *  صفات السهم , ويكون قاموس   arrowprops  : 
         *          لونه       color   
         *          عرضه     lw
         *         الضغط    shirnk




         * أمثلة
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
x = np.linspace(0, 20, 1000)
y= -((x-10)**2) +5
ax.plot(x,y)


plt.annotate('Max',xy=(10,6),xytext =(15,10)
,arrowprops =dict(color='r',shrink=0.02,lw =1.5))




plt.annotate('5',xy=(5,-20),xytext =(2,0)
,arrowprops =dict(color='b',shrink=3,lw =5))


plt.annotate('15',xy=(15,-20),xytext =(10,-60)
,arrowprops =dict(color='g',shrink=3,lw =9))


  

         * سهم دائري
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


fig, ax = plt.subplots()
x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis('equal')


ax.annotate('local maximum', xy=(6.28, 1)
            ,xytext=(10, 4),arrowprops=dict(color='b'))


ax.annotate('local minimum', xy=(5*np.pi,-1)
            ,xytext=(2, -6),arrowprops=dict(color='r'
            ,connectionstyle="angle3,angleA=0,angleB=-90"))


  

________________


11 . Imshow


         * تستخدم لرسم مربعات بالوان تعبر عن الارقام بها 
         * وهو شبيه بالامر كونتور , مع الفارق انه لا يوجد قيم لاكس وواي , ولكن نعطيه مصفوفة من بعدين
         * , ويقوم برسمها بناء علي قيمتها , فالقيم العليا غامقة  , والدنيا فاتحة 
         * تستخدم الأمر
plt.imshow()
         * حسب الرقم , الاصغر للفاتح و الاكبر للغامق
import matplotlib.pyplot as plt
I=  [[1,1,1,1,1,1,1],
     [1,2,2,2,2,2,1],
     [1,2,3,3,3,2,1],
     [1,2,3,4,3,2,1],
     [1,2,3,3,3,2,1],
     [1,2,2,2,2,2,1],
     [1,1,1,1,1,1,1]]
plt.imshow(I)
plt.colorbar()
  



         * يتم تغيير الباقة
import matplotlib.pyplot as plt
plt.style.use('classic')
I=  [[1,1,1,1,1,1,1],
     [1,2,2,2,2,2,1],
     [1,2,3,3,3,2,1],
     [1,2,3,4,3,2,1],
     [1,2,3,3,3,2,1],
     [1,2,2,2,2,2,1],
     [1,1,1,1,1,1,1]]
plt.imshow(I)
plt.colorbar()


  







         * لو تم عكس الارقام
import matplotlib.pyplot as plt
plt.style.use('classic')
I=  [[4,4,4,4,4,4,4],
     [4,3,3,3,3,3,4],
     [4,3,2,2,2,3,4],
     [4,3,2,1,2,3,4],
     [4,3,2,2,2,3,4],
     [4,3,3,3,3,3,4],
     [4,4,4,4,4,4,4]]




plt.imshow(I)
plt.colorbar()


  





         * تحديد باقة الالوان من داخل الامر
import matplotlib.pyplot as plt
I=  [[1,1,1,1,1,1,1],
     [1,2,2,2,2,2,1],
     [1,2,3,3,3,2,1],
     [1,2,3,4,3,2,1],
     [1,2,3,3,3,2,1],
     [1,2,2,2,2,2,1],
     [1,1,1,1,1,1,1]]
plt.imshow(I, cmap='gray');
plt.colorbar()


  









         * ارقام معكوسة و باقة الازرق
import matplotlib.pyplot as plt
I=  [[4,4,4,4,4,4,4],
     [4,3,3,3,3,3,4],
     [4,3,2,2,2,3,4],
     [4,3,2,1,2,3,4],
     [4,3,2,2,2,3,4],
     [4,3,3,3,3,3,4],
     [4,4,4,4,4,4,4]]




plt.imshow(I, cmap='Blues')
plt.colorbar()


  





         * دالة غريبة و باقة مختلفة
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 1000)
I = np.cos(x) * np.sin(x[:, np.newaxis])




plt.imshow(I, cmap='Accent')
plt.colorbar()


  





         * تأثير النقاط علي الرسم
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 1000)
I = np.cos(x) * np.sin(x[:, np.newaxis])


speckles = (np.random.random(I.shape) < 0.01)


I[speckles] = np.random.normal(0, 3, 
             np.count_nonzero(speckles))


plt.figure(figsize=(10, 3.5))
plt.imshow(I, cmap='RdBu')
plt.colorbar()
plt.clim(-1, 1)


  











         * دالة مختلفة
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np


x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])
plt.imshow(I)
plt.colorbar()


  
________________

12 . Legend


         * وهو الخاص بكتابة تفاصيل الرسم في مربع منفصل
         * ولا بد ان يتم تحديد label   كل دالة اثناء عمل الـ plot
  

         * يتم كتابة اسم الـ label  لكل دالة , ومنها يتم عمل الصندوق الخاص بها
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
ax.plot(x, np.sin(x),  label='Sin')
ax.plot(x, np.cos(x), label='Cos')
leg = ax.legend()
  

         * مكان الصندوق , وهل بخط ام لا
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
ax.plot(x, np.sin(x),  label='Sin')
ax.plot(x, np.cos(x), label='Cos')


ax.legend(loc='upper left', frameon=False)


  





         * تغيير المكان , وجعلها عمودين
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
ax.plot(x, np.sin(x),  label='Sin')
ax.plot(x, np.cos(x), label='Cos')


ax.legend(frameon=False,
          loc='lower center', ncol=2)


  





         * خصائص الصندوق
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
ax.plot(x, np.sin(x),  label='Sin')
ax.plot(x, np.cos(x), label='Cos')




ax.legend(fancybox=True, # curvy or not
          framealpha=1, #1 for white,0 for black
          shadow=True, # shadow or not
          borderpad=1) #how big of box


  





         * تغيير الخصائص
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
ax.plot(x, np.sin(x),  label='Sin')
ax.plot(x, np.cos(x), label='Cos')




ax.legend(fancybox=False, # curvy or not
          framealpha=1, #1 for white,0 for black
          shadow=False, # shadow or not
          borderpad=5) #how big of box


  





         * تحديد حجم الخط
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
ax.plot(x, np.sin(x),  label='Sin')
ax.plot(x, np.cos(x), label='Cos')
ax.legend(fontsize=30)
  







         * عمل صندوق لخطوط معينة
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots()
plt.axis('equal')
 
y = np.sin(x[:, np.newaxis] + np.pi *
           np.arange(0, 2, 0.5))


lines = plt.plot(x, y)


# lines is a list of plt.Line2D instances
plt.legend(lines[:2], ['Cost', 'Time'])


  

________________




13 . Lines


         * خط رأسي
import matplotlib.pyplot as plt
plt.vlines(0,-1,1,lw=5, color='r')
# value of X then Y start then Y end


  





         * خصائص
import matplotlib.pyplot as plt


plt.vlines(-2,-5,5,lw=5, color='r')
plt.vlines(-1,-4,4,lw=10, color='g')
plt.vlines(0,-3,3,lw=15, color='b')
plt.vlines(1,-2,2,lw=20, color='y')
plt.vlines(2,-1,1,lw=25, color='black')


  





         * العديد منهم
import matplotlib.pyplot as plt


w =[-1.5,-1,-.5,0,.5,1,1.5]
plt.vlines(w,-1,1,lw=10, color='r')
# X as list
  







         * خطوط افقية
import matplotlib.pyplot as plt


w =[-1.5,-1,-.5,0,.5,1,1.5]
plt.hlines(w,-1,1,lw=10, color='b')


# X as list


  





         * مثال
import matplotlib.pyplot as plt


plt.hlines(-3,-1,1,lw=10, color='w')
plt.hlines(-2,-1,1,lw=10, color='b')
plt.hlines(-1,0,1,lw=10, color='b')
plt.hlines(1,0,1,lw=10, color='b')
plt.hlines(2,-1,1,lw=10, color='b')
plt.hlines(3,-1,1,lw=10, color='w')




plt.vlines(-2.5,-1,1,lw=10, color='w')
plt.vlines(-1,-2,2,lw=10, color='r')
plt.vlines(0,-1,1,lw=10, color='r')
plt.vlines(1,1,2,lw=10, color='r')
plt.vlines(1,-2,-1,lw=10, color='r')
plt.vlines(2.5,-1,1,lw=10, color='w')


  

________________


14 . Limits


         * ابعاد الجراف  وهي تقوم بتعيين ابعاد المربع الذي يظهر فيه الجراف 
         * و تكون بالامر : 


set_xlim
set_ylim 


         * قبل التحديد
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10) 
ax = plt.axes()
plt.plot(x,-x**2  )
  



         * بعد التحديد
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10) 
ax = plt.axes()
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)
plt.plot(x,-x**2  )


  



         * امر اخر
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10) 


plt.axis([-20,10,-10,20])
#X start , X end , Y start , Y end
plt.plot(x,-x**2  )


  

         * أمر اخر
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10) 
ax = plt.axes()
ax.set(xlim=(-5, 10), ylim=(-20, 20) )
plt.plot(x,-x**2  )


  



         * لجعل الخطوة في الاكس و الواي متساوية
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10) 


plt.axis('equal')
plt.plot(x,-x**2  )
  



         * بالأمر set_visible  يتم تحديد اذا ما كانت المحاور مرئية او مختفية
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10) 


ax = plt.axes()


ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)


plt.plot(x,-x**2  )
  
________________

15 . Shapes




         * رسوم هندسية بالأمر      matplotlib.patches
         * وهي تشتمل علي عدد من الاشكال : 


Rectangle , Circle  , Polygon  , Ellipse  , Arc


         * أمر Circle
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Circle((0.5, 0.5),radius=0.1)


ax = plt.axes()
ax.add_patch(c)


  



         * خصائص
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Circle((0.5, 0.5),radius=0.1
               ,edgecolor='red',facecolor='g')


ax = plt.axes()
 
ax.add_patch(c)


  



         * الشفافية
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Circle((0.5, 0.5),radius=0.1
               ,edgecolor='red',facecolor='g', alpha=0.3)


ax = plt.axes()
ax.add_patch(c)
  





         * انتظام شكل الدائرة , عبر الحدود
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Circle((0.5, 0.5),radius=0.5
               ,edgecolor='red',facecolor='g', alpha=0.3)
 
ax = plt.axes()
ax.set_xlim(-1,2)
ax.set_ylim(-0.5,1.5)
ax.add_patch(c)
  





         * تطبيق اخر
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Circle((-2,5),radius=4
               ,color='b', alpha=1)


 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-2,12)


ax.add_patch(c)


  



         * الشكل البيضاوي
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Ellipse((-2,5),2,3,20,color='r')
#center , width , height , angle , color
 
ax = plt.axes()
ax.set_xlim(-5,5)
ax.set_ylim(0,8)


ax.add_patch(c)


  



         * مربع او مستطيل
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Rectangle((0.2, 0.2), 1, 1.2, color='r',angle =20 )
 #location of southwest ,width ,hight ,color , angle
ax = plt.axes()
ax.set_xlim(-1,2)
ax.set_ylim(-0.5,1.5)


ax.add_patch(c)
  



         * مثال
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Rectangle((-2, 3), 4,2, color='b',angle =-30 )
 #location of southwest ,width ,hight ,color , angle
ax = plt.axes()
ax.set_xlim(-7,7)
ax.set_ylim(-3,7)
ax.add_patch(c)
  

         * مثلث
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Polygon(((-7,-7), (5,-2), (-5,5)) ,color='b')
# vertices , color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)


ax.add_patch(c)


  



         * مضلع باربع اضلاع
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Polygon(((-7,-7),(5,-2),(2,7),(-5,5)) ,color='b')
# vertices , color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)


ax.add_patch(c)


  



         * النقاط تكون بالترتيب
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Polygon(((-7,-7),(5,-2),(-5,5),(2,7)) ,color='b')
# vertices , color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)


ax.add_patch(c)


  



         * اي عدد من  من الاضلاع , النقاط بالترتيب
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Polygon(((-7,-7),(0,-8),(5,-7),(8,0),
                 (0,-3),(3,8),(0,10),(-10,5)),
                color='b')
# vertices , color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)


ax.add_patch(c)


  



         * القوس
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Arc((3,2),7,10,theta1=0,theta2=80  )
# center , width , height ,start angle , end angle
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.add_patch(c)


  

         * تغيير الخصائص + اللون
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Arc((3,2),7,10,theta1=80,theta2=300,color='r' )
# center , width , height ,start angle , end angle,color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)


ax.add_patch(c)


  



         * مثال
import matplotlib.patches as pat
import matplotlib.pyplot as plt 


c = pat.Arc((3,2),7,10,theta1=180,theta2=90,color='b')
# center , width , height ,start angle , end angle,color
 
ax = plt.axes()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)


ax.add_patch(c)


  
________________

16 . Images
  



         * قراءة الصور  imread    
import matplotlib.pyplot as plt 




a = plt.imread('D:\\1.jpg')




print(a.shape)
print(a)


         * عدد البيانات
import matplotlib.pyplot as plt 
a = plt.imread('D:\\1.jpg')


print('=================================')
print(a.size)


         * قراءة مصفوفة الصور و كتابتها في ملف   txt  
import matplotlib.pyplot as plt 
a = plt.imread('D:\\1.jpg')


f= open("D:\\2.txt","w+")


b,c,d = a.shape


for x in range(b):
    for y in range(c):
        for z in range(3):
            f.write('\n' + str('Data for : ' +str(x) 
            +' & ' + str(y) +' & ' + str(z)) +' is :  '
            + str((a[x,y,z])))
f.close()


Data for : 0 & 0 & 0 is :  70
Data for : 0 & 0 & 1 is :  53
Data for : 0 & 0 & 2 is :  59
Data for : 0 & 1 & 0 is :  69
Data for : 0 & 1 & 1 is :  52
Data for : 0 & 1 & 2 is :  58
Data for : 0 & 2 & 0 is :  67
Data for : 0 & 2 & 1 is :  50
Data for : 0 & 2 & 2 is :  56






Data for : 429 & 767 & 1 is :  60
Data for : 429 & 767 & 2 is :  39
Data for : 429 & 768 & 0 is :  141
Data for : 429 & 768 & 1 is :  91
Data for : 429 & 768 & 2 is :  68
Data for : 429 & 769 & 0 is :  137
Data for : 429 & 769 & 1 is :  87
Data for : 429 & 769 & 2 is :  64


         * اظهار الصورة
import matplotlib.pyplot as plt 


a = plt.imread('D:\\1.jpg')


plt.imshow(a)
  



         * اظهار الوان معينة في الصورة
import matplotlib.pyplot as plt 




a = plt.imread('D:\\1.jpg')


plt.subplot(221)
plt.imshow(a)


x = a[:,:,0]
plt.subplot(222)
plt.imshow(x)


y = a[:,:,1]
plt.subplot(223)
plt.imshow(y)


z = a[:,:,2]
plt.subplot(224)
plt.imshow(z)


  





         * اقتطاع جزء من الصورة
import matplotlib.pyplot as plt 




a = plt.imread('D:\\1.jpg')


plt.subplot(221)
plt.imshow(a)


x = a[:200,:300,:]
plt.subplot(222)
plt.imshow(x)


y = a[120:470,220:550,:]
plt.subplot(223)
plt.imshow(y)


z = a[300:350,450:500,:]
plt.subplot(224)
plt.imshow(z)


  



         * حفظ الصورة
import matplotlib.pyplot as plt 
a = plt.imread('D:\\1.jpg')
plt.imsave('D:\\6.jpg', a)




         * حفظ جزء من الصورة
import matplotlib.pyplot as plt 
a = plt.imread('D:\\1.jpg')
plt.imsave('D:\\6.jpg', a[:,0:500])
b = plt.imread('D:\\6.jpg')
plt.imshow(b)




         * حفظ جزء من الصورة
import matplotlib.pyplot as plt 


a = plt.imread('D:\\1.jpg')
plt.imsave('D:\\6.jpg', a[0:200,:])


b = plt.imread('D:\\6.jpg')
plt.imshow(b)




         * ضغط الصورة
import matplotlib.pyplot as plt 




a = plt.imread('D:\\1.jpg')


plt.imsave('D:\\6.jpg', a[::15,::15])




b = plt.imread('D:\\6.jpg')
plt.imshow(b)


________________
________________


Seaborn


         * وهي مشابهة لماتبلوتليب  , خاصة في الرسوم
import seaborn as sns


         * أمر kdeplot  لو اخد الـ data  كلها يرسمها كونتور  
import pandas as pd
import numpy as np
import seaborn as sns


data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])


sns.kdeplot(data)
  



         * ولو أخذ الـ data  علي مرحلتين يرسمها كالتوزيع الطبيعي
import pandas as pd
import numpy as np
import seaborn as sns


data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])


for col in 'xy':
    sns.kdeplot(data[col], shade=True)
   
         * نفس الأمر لكن مع إلغاء الـ shade
import pandas as pd
import numpy as np
import seaborn as sns


data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])


for col in 'xy':
    sns.kdeplot(data[col], shade=False)


  



         * أمر distplot  لعمل خطوط رأسية في الرسم  
import pandas as pd
import numpy as np
import seaborn as sns


data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])


for col in 'xy':
    sns.kdeplot(data[col], shade=True)


sns.distplot(data['x'])
sns.distplot(data['y'])


  



         * أمر joinplot  
import pandas as pd
import numpy as np
import seaborn as sns


data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='kde');
  





         * ولو تم تحويل الـ kind  لنوعية : hex   
import pandas as pd
import numpy as np
import seaborn as sns


data =np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])


with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='hex')


  

________________


Scipy


         * أمر fminbound  
import numpy as np
import scipy as sc


def f(x):
    return x**2 + 10*np.sin(x)


a = sc.optimize.fminbound(f,# function
                          x1 = -10,# first bound 
                          x2 = 10,#second bound
                          xtol = 0.01, # Max Tolerance
                          full_output = True,# details 
                          disp = 1 ) #show only numbers


print(a)
# Value of x , Value of y , 0 for convergence
# , number of iterations
(-1.3061484200406244, -7.94582288025181, 0, 11)






         * نفس الأمر disp = 2  
import numpy as np
import scipy as sc


def f(x):
    return x**2 + 10*np.sin(x)
a = sc.optimize.fminbound(f,# function
                          x1 = -10,# first bound 
                          x2 = 10,#second bound
                          xtol = 0.01, # Max Tolerance
                          full_output = True,# details 
                          disp = 2 ) #show some details


print(a)
# Value of x , Value of y , 0 for convergence
# , number of iterations
Optimization terminated successfully;
The returned value satisfies the termination criteria
(using xtol =  0.01 )
(-1.3061484200406244, -7.94582288025181, 0, 11)




         * نفس الأمر disp = 3 
import numpy as np
import scipy as sc




def f(x):
    return x**2 + 10*np.sin(x)


a = sc.optimize.fminbound(f,# function
                          x1 = -10,# first bound 
                          x2 = 10,#second bound
                          xtol = 0.01, # Max Tolerance
                          full_output = True,# details 
                          disp = 3 ) #show iterations




print(a)
# Value of x , Value of y , 0 for convergence
# , number of iterations
 Func-count     x          f(x)          Procedure
    1       -2.36068     -1.46647        initial
    2        2.36068      12.6121        golden
    3       -5.27864      36.3032        golden
    4      -0.715181     -6.04606        parabolic
    5      -0.795481     -6.50921        parabolic
    6       -1.28322     -7.94269        parabolic
    7       -1.69477     -7.05101        golden
    8       -1.29818     -7.94543        parabolic
    9       -1.30615     -7.94582        parabolic
   10       -1.30948     -7.94577        parabolic
   11       -1.30282     -7.94575        parabolic


Optimization terminated successfully;
The returned value satisfies the termination criteria
(using xtol =  0.01 )
(-1.3061484200406244, -7.94582288025181, 0, 11)




         * أمر fminbound  لإيجاد القيمة الدنيا  


from scipy import optimize


def a(x):
    return (x)
def b(x):
    return (x**2)
def c(x):
    return (x**3)
def d(x):
    return (x**2 - 4*x + 1)
def e(x):
    return (x**3 + x**2 - 4*x - 3)
def f(x):
    return (1/x)


amin = optimize.fminbound(a, -4, 4)
print(amin)
bmin = optimize.fminbound(b, -4, 4)
print(bmin)
cmin = optimize.fminbound(c, -4, 4)
print(cmin)
dmin = optimize.fminbound(d, -4, 4)
print(dmin)
emin = optimize.fminbound(e, -4, 4)
print(emin)
fmin = optimize.fminbound(f, -4, 4)
print(fmin)






         * أمر fmin_bfgs   لعمل الـ GD  
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
def f(x):
    return x**2 + 10*np.sin(x)


x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
plt.show()




a = sc.optimize.fmin_bfgs(f, #function
                          x0 = 50 , # a value to start
                          epsilon = 10 ,  # step
                          disp = 1 , # if 1 then display full details
                          retall = 1 ,# if 1 then display all iterations
                          maxiter = 2 ) #max no. if iterations
print(a)


  

Warning: Maximum number of iterations has been exceeded.
         Current function value: 1239.195121
         Iterations: 2
         Function evaluations: 12
         Gradient evaluations: 4
(array([35.29788524]), [array([50]), array([44.95]), array([35.29788524])])




         * قيم مختلفة
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
def f(x):
    return x**2 + 10*np.sin(x)


x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
plt.show()




a = sc.optimize.fmin_bfgs(f, #function
                          x0 = 50 , # a value to start
                          epsilon = 0.1 ,  # step
                          disp = 1 , # if 1 then display full details
                          retall = 1 ,# if 1 then display all iterations
                          maxiter = 20 ) #max no. if iterations
print(a)


  



Warning: Desired error not necessarily achieved due to precision loss.
         Current function value: -7.931319
         Iterations: 7
         Function evaluations: 258
         Gradient evaluations: 82
(array([-1.3562454]), [array([50]), array([44.95]), array([35.01154003]), array([17.00942323]), array([-2.5328942]), array([-1.21948726]), array([-1.36193066]), array([-1.3562454])])




         * أمر basinhopping  لنفس المهمة  
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc


def f(x):
    return x**2 + 10*np.sin(x)


x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
plt.show()


a = sc.optimize.basinhopping(f,  #function
                             x0 = 70 ,# a value to start
                             niter = 20 , #max no. if iterations
                             stepsize = .2 ,# step
                             disp = 0) # if 1 then display full details
print(a)


  

fun: -7.9458233756152845
 lowest_optimization_result:       fun: -7.9458233756152845
 hess_inv: array([[0.0857338]])
      jac: array([1.1920929e-07])
  message: 'Optimization terminated successfully.'
     nfev: 12
      nit: 2
     njev: 4
   status: 0
  success: True
        x: array([-1.30644001])
                    message: ['requested number of basinhopping iterations completed successfully']
      minimization_failures: 0
                       nfev: 318
                        nit: 20
                       njev: 106
                          x: array([-1.30644001])


         * صيغة مختلفة
import numpy as np
import scipy as sc




func = lambda x: np.cos(14.5 * x - 0.3) + (x + 0.2) * x
x0=[1.]


ret = sc.optimize.basinhopping(func, #function
                               x0 , # a value to start
                                # method = BFGS
                               minimizer_kwargs={"method": "BFGS"},
                               niter=200) #max no. if iterations
print("global minimum: x = %.4f, f(x0) = %.4f" % (ret.x, ret.fun))




global minimum: x = -0.1951, f(x0) = -1.0009




         * نفس الأمر لمعادلة من بعدين  
import numpy as np
import scipy as sc




def func2d(x):
    f = np.cos(14.5*x[0]-0.3)+(x[1]+0.2)*x[1]+(x[0]+0.2)*x[0]
    df = np.zeros(2)
    return f, df


x0 = [1.0, 1.0]
ret = sc.optimize.basinhopping(
        func2d,
        x0, 
        minimizer_kwargs={"method":"L-BFGS-B", "jac":True},
        niter=2000)


print("global minimum: x = [%.4f, %.4f], f(x0) = %.4f" % 
      (ret.x[0],ret.x[1],ret.fun))


global minimum: x = [-0.1968, -0.1259], f(x0) = -1.0099




         * أمر fsolve  لحل المعادلات : يأتي بالجذر الأكبر فقط
import scipy as sc


def f(x):
    return x**2 - 2*x -15


a = sc.optimize.fsolve(f,x0 = 10 , full_output=False )
print(a)
[5.]


         * لو تم عمل القيمة بـTrue   يأتي بالتفاصيل
import scipy as sc
def f(x):
    return x**2 - 2*x -15


a = sc.optimize.fsolve(f,x0 = 10 , full_output=True )


print(a)
(array([5.]), {'nfev': 9, 'fjac': array([[-1.]]), 'r': array([-8.00003226]), 'qtf': array([-1.23520701e-07]), 'fvec': array([4.97379915e-13])}, 1, 'The solution converged.')


         * أمر curve_fit  
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#function
def func(x, a, b, c):
    return a * np.exp(-b * x) + c
#random values of X 
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
# y noise
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')  # draw the blue line


popt, pcov = curve_fit(func, xdata, ydata) #fitting
plt.plot(xdata, func(xdata, *popt), 'r-', #draw the red line
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


#fit with bounds
popt, pcov =curve_fit(func,xdata,ydata,bounds=(0,[3., 1., 0.5]))
plt.plot(xdata, func(xdata, *popt),  #draw the green line
         'g--',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


  

 webbrowser




         * لفتح أي موقع   
import webbrowser as w


w.open('www.fb.com') 


         * لفتح ملف أونلاين كبيانات  
from pandas import read_csv
url='https://github.com/cs109/2014_data/blob/master/countries.csv'
data = read_csv(url, names=[2])
print(data.shape)


glob


         * للبحث عن الملفات   هنا يأتي بكل الملفات
import glob as gb
a = gb.glob(pathname= 'D:\\Machine Learning\\000\\*.*')


print(a)
['D:\\Machine Learning\\000\\06.pdf', 'D:\\Machine Learning\\000\\07.pdf', 'D:\\Machine Learning\\000\\08.pdf', 'D:\\Machine Learning\\000\\09.pdf', 'D:\\Machine Learning\\000\\10.pdf', 'D:\\Machine Learning\\000\\New Microsoft PowerPoint Presentation.ppt', 'D:\\Machine Learning\\000\\New Microsoft Word Document.doc']




         * أمر glob1  يأتي بالاسم فقط  
import glob as gb


b = gb.glob1('D:\\Machine Learning\\000\\' , '*.*' )
print(b)


['06.pdf', '07.pdf', '08.pdf', '09.pdf', '10.pdf', 'New Microsoft PowerPoint Presentation.ppt', 'New Microsoft Word Document.doc']


         * للبحث عن ملف معين  ,بالاسم و المسار 
import glob as gb
a = gb.glob(pathname= 'D:\\Machine Learning\\000\\*.pdf')
print(a)


['D:\\Machine Learning\\000\\06.pdf', 'D:\\Machine Learning\\000\\07.pdf', 'D:\\Machine Learning\\000\\08.pdf', 'D:\\Machine Learning\\000\\09.pdf', 'D:\\Machine Learning\\000\\10.pdf']


         * أمر glob1  للبحث عن ملف معين , بالاسم فقط  
import glob as gb
b = gb.glob1('D:\\Machine Learning\\000\\' , '*.pdf' )
print(b)


['06.pdf', '07.pdf', '08.pdf', '09.pdf', '10.pdf']










try except


         * و هي لاصطياد الأخطاء و تجاوزها 
         * و تبدأ بأمر try يليه الأوامر
         * ثم except  يليه ما الذي يحدث في حالة الخطأ
         * ثم finally  وهي أوامر يتم تنفيذها سواء فيه خطا ام لا
         * وقد نقوم بتجديد نوع الخطأ من الأخطاء : 
         * IOError , ValueError , ImportError , EOFError , KeyboadInterrupt


         * مثال عام
while True : 
    try : 
        n = input("Number?")
        n = int(n)
        print(n*5)
        break
    except   :
        print ("wrong format")
        break
    finally : 
        print ("end")


Number?7
35
end


Number?fff
wrong format
end




         * مثال القسمة علي صفر  
z = input ('number ? ')


try:
    x = 1 / int(z)
    print(x)
except ZeroDivisionError as err:
    print("Error message is:", err)




number ? 5
0.2




number ? 0
Error message is: division by zero


4 .datetime




         * لإظهار تاريخ اليوم
from datetime import date
now = date.today()
print(now)


2019-01-21


         * صياغة مختلفة  
from datetime import date
now = date.today()
a = now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(a)


01-21-19. 21 Jan 2019 is a Monday on the 21 day of January.


         * للتحويل من ارقام الي تاريخ  
from datetime import date
a = date(1982, 2, 2)
print(a)


1982-02-02


         * لحساب عدد الأيام من تاريخ معين الي اليوم   
from datetime import date
now = date.today()
a = date(1982, 2, 2)
z = now-a


print(z)


13502 days, 0:00:00


         * عدد الأيام من تاريخ لتاريخ  
from datetime import date
now = date.today()


a = date(1982, 2, 2)
b = date(2011, 3, 15)
z = b-a


print(z)


10633 days, 0:00:00


         * أمر datetime  يقوم بنفس المهام لكن مع الوقت 
from datetime import datetime
a = datetime(year=2011, month=3, day=15,
             hour=13 ,minute = 15, second = 9)


b = datetime(year=1982, month=2, day=2,
             hour=18 ,minute = 43, second = 12)
print(a)
print(b)
print(a-b)
2011-03-15 13:15:09
1982-02-02 18:43:12
10632 days, 18:31:57


         * مكتبة time  تأتي بالوقت و التاريخ بدقة  
import time
t = time.gmtime()
print(t)


time.struct_time(tm_year=2019, tm_mon=1, tm_mday=21, tm_hour=14, tm_min=1, tm_sec=38, tm_wday=0, tm_yday=21, tm_isdst=0)
         * عمل دالة للانتظار   
import time
def wait(x):
    t0 = time.time()
    while time.time() - t0 < x:
        time.sleep(1)
    return x


print('start')
wait(3)
print('finish')