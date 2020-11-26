# Generated by Django 3.0 on 2020-11-26 21:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_work', models.CharField(choices=[('IQ', 'العراق'), ('LB', 'لبنان'), ('JO', 'اﻷردن'), ('SY', 'سوريا'), ('TR', 'تركيا')], default=None, max_length=150, verbose_name='الدولة')),
                ('city_work', models.CharField(max_length=255, verbose_name='اسم المحافظة')),
                ('city_work_en', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='City En')),
                ('city_work_ku', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='City Ku')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم و الكنية')),
                ('work', models.CharField(max_length=255, verbose_name='العمل')),
                ('org_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم المنظمة')),
                ('email', models.EmailField(max_length=255, verbose_name='البريد الاكتروني')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrgProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم المنظمة')),
                ('name_en_ku', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم المنظمة باللغة الانكليزية أو الكردية')),
                ('short_cut', models.CharField(blank=True, max_length=255, null=True, verbose_name='الاسم المختصر')),
                ('org_type', models.CharField(choices=[('establishment', 'مؤسسة'), ('org', 'جمعية أو منظمة'), ('team', 'مبادرة / فريق'), ('union', 'اتحاد / تحالف / تجمع'), ('group', 'لجنة / تنسيقية / مجموعة')], max_length=150, verbose_name='نوع المنظمة')),
                ('position_work', django_countries.fields.CountryField(max_length=255, verbose_name='مكان العمل')),
                ('logo', models.ImageField(default='org_logos/default_logo.jpg', upload_to='org_logos', verbose_name='شعار المنظمة')),
                ('message', models.TextField(max_length=2000, verbose_name='الرؤية و الرسالة')),
                ('name_managing_director', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم رئيس مجلس اﻹدارة')),
                ('name_ceo', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم المدير التنفيذي')),
                ('site_web', models.URLField(blank=True, max_length=255, null=True, verbose_name='الموقع الالكتروني')),
                ('facebook', models.URLField(blank=True, max_length=255, null=True, verbose_name='صفحة فيسبوك')),
                ('twitter', models.URLField(blank=True, max_length=255, null=True, verbose_name='صفحة تويتر')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='البريد الاكتروني')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='رقم الهاتف')),
                ('name_person_contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم الشخص المسؤول عن التواصل')),
                ('email_person_contact', models.EmailField(blank=True, max_length=255, null=True, verbose_name='البريد الاكتروني للشخص المسؤول عن التواصل')),
                ('org_adress', models.CharField(max_length=255, verbose_name='عنوان المقر الرئيسي')),
                ('work_domain', models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, verbose_name='مجال العمل')),
                ('target_cat', models.CharField(choices=[('No category selected', 'لا يوجد فئة محددة'), ('womans', 'نساء'), ('Mans', 'رجال'), ('Youth 18-24', 'شباب 18-24'), ('Child 0-18', 'أطفال 0-18'), ('Religious groups', 'مجموعات دینیة'), ('Ethnic groups', 'مجموعة عرقیة'), ('Persons lacking breadwinner ', 'فاقدي المعیل'), ('Handicapped', 'ذوي الاحتیاجات الخاصة'), ('Refugees', 'لاجئین'), ('Displaced', 'نازحین'), ('Returned', 'عائدین'), ('Other civil society organizations', 'منظمات مجتمع مدني اخرى'), ('Other', 'أخرى')], max_length=255, verbose_name='الفئات المستهدفة')),
                ('date_of_establishment', models.CharField(blank=True, max_length=150, null=True, verbose_name='تاريخ سنة التأسيس')),
                ('is_org_registered', models.CharField(choices=[('0', 'لا'), ('1', 'نعم')], max_length=100, verbose_name='هل المنظمة مسجلة ؟')),
                ('org_registered_country', django_countries.fields.CountryField(blank=True, max_length=255, null=True, verbose_name='بلد التسجيل')),
                ('org_members_count', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='عدد اﻷعضاء')),
                ('org_members_womans_count', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='عدد النساء من اﻷعضاء')),
                ('w_polic_regulations', models.CharField(choices=[('No', 'لا يوجد'), ('Code of conduct', 'مدونة السلوك'), ('Child protection', 'حماية الطفل'), ('Anti-corruption', 'مكافحة الفساد'), ('Human resources policy', 'سياسة الموارد البشرية'), ('Procurement policy', 'سياسة المشتريات'), ('Volunteering policy', 'سياسة التطوع'), ('Anti-harassment Policy', 'سياسة منع التحرش'), ('Financial policy', 'السياسة المالية'), ('Equipment use Policy', 'سياسة استخدام المعدات'), ('privacy policy', 'سياسة الخصوصية'), ('Other', 'أخرى')], max_length=200, verbose_name='السياسات واللوائح المكتوبة')),
                ('org_member_with', models.CharField(blank=True, choices=[('0', 'لا'), ('1', 'نعم')], max_length=100, null=True, verbose_name='ھل المؤسسة عضو في اي شبكة او تحالف او جسم تنسیقي؟')),
                ('coalition_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم الشبكة / التحالف')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('city_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgs.City', verbose_name='المحافظة')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المستخدم')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersFundingOpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_funding', models.CharField(blank=True, max_length=255, null=True, verbose_name='الجهة المانحة')),
                ('logo', models.ImageField(blank=True, default='org_logos/default_logo.jpg', null=True, upload_to='funding_logos', verbose_name='لوغو الجهة المانحة')),
                ('category', models.CharField(blank=True, choices=[('total', 'كلية'), ('part', 'جزئية')], max_length=100, null=True, verbose_name='فئة المنحة')),
                ('fund_type', models.CharField(choices=[('study', 'دراسية'), ('prod', 'انتاجية'), ('study & reserch', 'دراسات و أبحاث')], max_length=150, verbose_name='نوع المنحة')),
                ('study_level', models.CharField(blank=True, choices=[('licence', 'إجازة جامعية'), ('m1', 'دبلوم'), ('m2', 'ماجيستير'), ('doctorat', 'دكتوراه')], max_length=255, null=True, verbose_name='المستوى التعليمي')),
                ('comp_study', models.CharField(blank=True, choices=[('1', 'إعلام/ اتصالات/ علاقات عامة'), ('2', 'أعمال وإدارة'), ('3', 'اقتصاد/ محاسبة'), ('4', 'تعليم/ تربية/ رياض أطفال'), ('5', 'حاسوب وتكنولوجيا المعلومات'), ('6', 'دراسات إسلامية'), ('7', 'دراسات إنسانية/ لغات'), ('8', 'زراعة وعلوم بيئية'), ('9', 'سياحة وعلوم فندقية'), ('10', 'علوم إنسانية'), ('11', 'علوم طبية/ طب/ صيدلة/ تمريض'), ('12', 'علوم طبيعية'), ('13', 'عمارة وتصميم'), ('14', 'فنون ومسارح وموسيقى'), ('15', 'قانون ودراسات قانونية'), ('16', 'هندسة وعلوم هندسية')], max_length=255, null=True, verbose_name='الاختصاص التعليمي')),
                ('domain', models.CharField(blank=True, choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, null=True, verbose_name='قطاع المنحة')),
                ('position_work', django_countries.fields.CountryField(max_length=255, verbose_name='دول المنحة')),
                ('fund_org_description', models.TextField(max_length=5000, verbose_name='لمحة عن الجهة المانحة')),
                ('funding_dead_date', models.DateField(verbose_name='تاريخ إغلاق المنحة')),
                ('funding_period', models.CharField(choices=[('less of 6 months', 'أقل من 6 أشهر'), ('from 6 mths to one year', 'ستة أشهر لسنة'), ('from one to 2 years', 'سنة إلى سنتين'), ('more than 2 years', 'أكثر من سنتين'), ('other', 'أخرى')], max_length=255, verbose_name='مدة المنحة')),
                ('funding_amounte', models.CharField(choices=[('less than 5000 ', 'أقل من 5000 دولار'), ('from 5000 to 10000 dollar', 'بين 5000 و 10000 دولار'), ('from 10000 to 50000', 'بين 10000 و50000 دولار'), ('from 50000 to 100000', 'بين 50000 و100000 دولار'), ('more than  100000', 'بين 50000 و100000 دولار'), ('other', 'أخرى')], max_length=255, verbose_name='حجم المنحة')),
                ('funding_description', models.TextField(max_length=2000, verbose_name='وصف المنحة')),
                ('funding_conditions', models.TextField(max_length=2000, verbose_name='شروط المنحة')),
                ('funding_reqs', models.TextField(max_length=2000, verbose_name='متطلبات التقديم')),
                ('funding_guid', models.TextField(max_length=2000, verbose_name='كيفية التقديم')),
                ('funding_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='الرابط الأصلي')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('city_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgs.City', verbose_name='المحافظة')),
                ('org_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile', verbose_name='اسم المنظمة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OtherOrgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='اضف اسم المنظمة اﻷخرى')),
                ('logo', models.ImageField(blank=True, default='org_logos/default_logo.jpg', null=True, upload_to='other_org_logos', verbose_name='شعار المنظمة')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_entity', models.CharField(max_length=255, verbose_name='اسم الجهة')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان البحث')),
                ('domaine', models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=150, verbose_name='مجال البحث')),
                ('media', models.FileField(upload_to='rapport_files', verbose_name='ملف البحث')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='رابط البحث')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgRapport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان التقرير')),
                ('domain', models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=150, verbose_name='مجال التقرير')),
                ('media', models.FileField(upload_to='rapport_files', verbose_name='صورة او ملف التقرير')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('org_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile', verbose_name='اسم المنظمة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان الخبر')),
                ('content', models.TextField(max_length=5000, verbose_name='تفاصيل الخبر')),
                ('image', models.ImageField(default='news_images/article_img.jpg', upload_to='news_images', verbose_name='صورة الخبر')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('org_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile', verbose_name='اسم المنظمة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان المحتوى')),
                ('media', models.FileField(upload_to='rapport_files', verbose_name='صورة او ملف المحتوى')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='رابط المحتوى')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('org_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255, verbose_name='عنوان الوظيفة')),
                ('period_months', models.PositiveIntegerField(blank=True, null=True, verbose_name='مدة العقد بالأشهر')),
                ('job_description', models.TextField(max_length=5000, verbose_name='وصف الوضيفة')),
                ('job_type', models.CharField(choices=[('Full time', 'دوام كامل'), ('Part time', 'دوام جزئي'), ('Expert', 'استشاري'), ('Traning', 'تدريب'), ('Volunteering', 'تطوع'), ('Fellowship', 'زمالة')], max_length=255, verbose_name='نوع الوظيفة')),
                ('experience', models.CharField(choices=[('Not necessary', 'الخبرة غير ضرورية'), ('1-2 year', '1-2 سنة'), ('2-5 years', '2-5 سنة'), ('5-9 years', '5-9 سنة'), ('up of 10 years', '10 وفوق'), ('Othre', 'أخرى')], max_length=255, verbose_name='الخبرة')),
                ('position_work', django_countries.fields.CountryField(max_length=255, verbose_name='مكان العمل')),
                ('job_area', models.CharField(blank=True, max_length=150, null=True, verbose_name='المنطقة')),
                ('job_domain', models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, verbose_name='مجال العمل')),
                ('dead_date', models.DateField(default=None, verbose_name='تاريخ إغلاق الوظيفة')),
                ('job_aplay', models.TextField(max_length=5000, verbose_name='طريقة التقدم للوظيفة')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('city_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgs.City', verbose_name='المحافظة')),
                ('org_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile', verbose_name='اسم المنظمة')),
                ('other_org_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgs.OtherOrgs', verbose_name='اسم المنظمة اﻷخرى')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgFundingOpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_funding', models.CharField(blank=True, max_length=255, null=True, verbose_name='الجهة المانحة')),
                ('logo', models.ImageField(blank=True, default='org_logos/default_logo.jpg', null=True, upload_to='funding_logos', verbose_name='لوغو الجهة المانحة')),
                ('funding_org_description', models.TextField(max_length=2000, verbose_name='لمحة عن الجهة المانحة')),
                ('work_domain', models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, verbose_name='قطاع المنحة')),
                ('position_work', django_countries.fields.CountryField(max_length=255, verbose_name='دول المنحة')),
                ('funding_dead_date', models.DateField(verbose_name='تاريخ إغلاق المنحة')),
                ('funding_period', models.CharField(choices=[('less of 6 months', 'أقل من 6 أشهر'), ('from 6 mths to one year', 'ستة أشهر لسنة'), ('from one to 2 years', 'سنة إلى سنتين'), ('more than 2 years', 'أكثر من سنتين'), ('other', 'أخرى')], max_length=255, verbose_name='مدة المنحة')),
                ('funding_amounte', models.CharField(choices=[('less than 5000 ', 'أقل من 5000 دولار'), ('from 5000 to 10000 dollar', 'بين 5000 و 10000 دولار'), ('from 10000 to 50000', 'بين 10000 و50000 دولار'), ('from 50000 to 100000', 'بين 50000 و100000 دولار'), ('more than  100000', 'بين 50000 و100000 دولار'), ('other', 'أخرى')], max_length=255, verbose_name='حجم المنحة')),
                ('funding_description', models.TextField(max_length=2000, verbose_name='وصف المنحة')),
                ('funding_conditions', models.TextField(max_length=2000, verbose_name='شروط المنحة')),
                ('funding_reqs', models.TextField(max_length=2000, verbose_name='متطلبات التقديم')),
                ('funding_guid', models.TextField(max_length=2000, verbose_name='كيفية التقديم')),
                ('funding_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='الرابط الأصلي')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('city_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgs.City', verbose_name='المحافظة')),
                ('org_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile', verbose_name='اسم المنظمة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان البيان')),
                ('media', models.FileField(upload_to='rapport_files', verbose_name='صورة او ملف البيان')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('org_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile', verbose_name='اسم المنظمة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrgCapacityOpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_capacity', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم الجهة الممولة')),
                ('title_capacity', models.CharField(max_length=255, verbose_name='عنوان الفرصة')),
                ('capacity_description', models.TextField(max_length=5000, verbose_name='وصف الفرصة')),
                ('capacity_type', models.CharField(choices=[('traning', 'تدريب'), ('college', 'زمالة')], max_length=255, verbose_name='نوع الفرصة')),
                ('position_work', django_countries.fields.CountryField(max_length=255, verbose_name='مكان الفرصة')),
                ('capacity_domain', models.CharField(choices=[('Media', 'اﻹعلام و المناصرة'), ('Education', 'تعليم'), ('Protection', 'حماية و الصحة النفسية'), ('Livelihoods and food security', 'سبل العيش واﻷمن الغذائي'), ('Project of clean ,water, sanitation ', 'النظافة والمياه والصرف الصحي'), ('Development', 'تنمية و بناء قدرات و ثقافة'), ('Law, suport, policy', 'المواطنة و الحوكمة و الديموقراطية و السلام و السياسة'), ('Donors and support volunteering', 'اﻷسرة و الجندرة و قضايا المرأة'), ('Religious org', 'المأوى و البنة التحتية'), ('Prof association and assembles', 'تنسيق و تجمعات المجتمع المدني'), ('Health', 'صحة'), ('Studies and research', 'دراسات وأبحاث'), ('Other', 'أخرى')], max_length=255, verbose_name='قطاع الفرصة')),
                ('capacity_dead_date', models.DateField(verbose_name='تاريخ إغلاق المنحة')),
                ('capacity_reqs', models.TextField(max_length=2000, verbose_name='متطلبات التقديم')),
                ('capacity_guid', models.TextField(max_length=2000, verbose_name='طريقة التقديم')),
                ('capacity_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='الرابط الأصلي')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('city_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orgs.City', verbose_name='المحافظة')),
                ('org_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile', verbose_name='اسم المنظمة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم المنظمة')),
                ('email', models.EmailField(max_length=255, verbose_name='البريد الاكتروني')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DevOrgOpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_dev', models.CharField(blank=True, max_length=255, null=True, verbose_name='اسم الجهة ')),
                ('title_dev', models.CharField(max_length=255, verbose_name='عنوان المادة')),
                ('dev_date', models.DateTimeField(blank=True, null=True, verbose_name='تاريخ الإعداد/النشر/التأليف')),
                ('dev_description', models.TextField(max_length=2000, verbose_name='لمحة عن الجهة')),
                ('subject', models.CharField(choices=[('Project development and management', 'تطوير وإدارة المشاريع'), ('Organizational governance', 'الحوكمة التنظيمية'), ('Advocacy and Campaigns', 'المناصرة والحملات'), ('Civil Society Library', 'مكتبة المجتمع المدني'), ('other', 'أخرى')], max_length=255, verbose_name='موضوع المادة')),
                ('content', models.FileField(blank=True, default='org_logos/default_logo.jpg', null=True, upload_to='dev_files', verbose_name='المادة ')),
                ('video', models.URLField(blank=True, max_length=255, null=True, verbose_name='رابط فيديو')),
                ('publish', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('updated_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('org_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgProfile', verbose_name='اسم المنظمة')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
