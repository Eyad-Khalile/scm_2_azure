from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


# ============ User =============================
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,  required=True,
                             help_text=_('حقل إجباري, يرجى إدخال بريد إلكتروني صحيح لتتمكن من تفعيل حسابك'), label=_('عنوان بريد إلكتروني'))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# CITYES
class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = [
            'position_work',
            'city_work',
        ]


# ORG PROFILE
class OrgProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=255, min_length=3, label=_('اسم المنظمة'),
                           help_text=_(
                               ''),
                           widget=forms.TextInput(
                               attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')})
                           )
    name_en_ku = forms.CharField(max_length=255, min_length=3, required=False, label=_('اسم المنظمة باللغة الانكليزية أو الكردية'),
                                 widget=forms.TextInput(
        attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')})
    )
    short_cut = forms.CharField(max_length=255, min_length=3, required=False, label=_('الاسم المختصر'),
                                widget=forms.TextInput(
        attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')})
    )
    message = forms.CharField(max_length=2000, min_length=3, required=False, label=_("الرؤية و الرسالة"), widget=forms.Textarea(
        attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')}))

    name_managing_director = forms.CharField(max_length=255, min_length=3, required=False, label=_('اسم رئيس مجلس اﻹدارة'),
                                             widget=forms.TextInput(
        attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')})
    )
    name_ceo = forms.CharField(max_length=255, min_length=3, required=False, label=_('اسم المدير التنفيذي'),
                               widget=forms.TextInput(
        attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')})
    )
    site_web = forms.URLField(
        max_length=255, min_length=3, required=False, label=_('الموقع الالكتروني'), widget=forms.TextInput(attrs={'placeholder': "Ex: mysite.com"}))

    facebook = forms.URLField(
        max_length=255, min_length=3, required=False, label=_('صفحة فيسبوك'), widget=forms.TextInput(attrs={'placeholder': ""}))

    twitter = forms.URLField(
        max_length=255, min_length=3, required=False, label=_('صفحة تويتر'), widget=forms.TextInput(attrs={'placeholder': ""}))

    email = forms.EmailField(
        max_length=255, min_length=3, required=False, label=_('البريد الاكتروني'), widget=forms.TextInput(attrs={'placeholder': "Ex: myemail@example.com"}))

    name_person_contact = forms.CharField(max_length=255, min_length=3, required=False, label=_('اسم الشخص المسؤول عن التواصل'),
                                          widget=forms.TextInput(
        attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')})
    )

    email_person_contact = forms.EmailField(
        max_length=255, min_length=3, required=False, label=_('البريد الاكتروني للشخص المسؤول عن التواصل'), widget=forms.TextInput(attrs={'placeholder': "Ex: email@example.com"}))

    org_adress = forms.CharField(max_length=255, min_length=3, label=_('عنوان المقر الرئيسي'),
                                 widget=forms.TextInput(
        attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')})
    )
    coalition_name = forms.CharField(max_length=255, min_length=3, required=False, label=_('اسم الشبكة / التحالف'),
                                     widget=forms.TextInput(
        attrs={'placeholder': _('هذا الحقل لا يقبل الحروف الخاصه و الرموز')})
    )

    class Meta:
        model = OrgProfile
        fields = [
            'user',
            'name',
            'name_en_ku',
            'short_cut',
            'org_type',
            'position_work',
            'city_work',
            'logo',
            'message',
            'name_managing_director',
            'name_ceo',
            'site_web',
            'facebook',
            'twitter',
            'email',
            'phone',
            'name_person_contact',
            'email_person_contact',
            'work_domain',
            'target_cat',
            'date_of_establishment',
            'is_org_registered',
            'org_registered_country',
            'org_adress',
            'org_members_count',
            'org_members_womans_count',
            'w_polic_regulations',
            'org_member_with',
            'coalition_name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_work'].queryset = City.objects.none()

        if 'position_work' in self.data:
            try:
                position_work = self.data.get('position_work')
                self.fields['city_work'].queryset = City.objects.filter(
                    position_work=position_work)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif 'city_work' in self.data:
        #     self.fields['city_work'].queryset = self.instance.position_work.city_work_set.all()
        # else:
        #     self.fields['city_work'].queryset = City.objects.all()
        elif self.instance.pk and self.instance.city_work:
            print(self.instance.city_work)
            position_work = self.instance.position_work
            self.fields['city_work'].queryset = City.objects.filter(
                position_work=position_work)
        # else:
        #     self.fields['city_work'].queryset = City.objects.all()

        elif self.instance.pk and not self.instance.city_work:
            self.fields['city_work'].queryset = City.objects.all()
            # if 'position_work' in self.data:
            #     print(self.data)
        #         try:
        #             position_work = self.data.get('position_work')
        #             self.fields['city_work'].queryset = City.objects.filter(
        #                 position_work=position_work)
        #         except (ValueError, TypeError):
        #             pass  # invalid input from the client; ignore and fallback to empty City queryset

            # self.fields['city_work'].queryset = self.instance.position_work.city_work_set.order_by(
            #     'city_work')
            # self.fields['city_work'].queryset = self.instance.position_work.city_work_set.all()


class OrgConfirmForm(forms.ModelForm):
    class Meta:
        model = OrgProfile
        fields = [
            'publish',
        ]


# ::::::::::::::::: ORGS NEWS :::::::::::::::::
class NewsForm(forms.ModelForm):

    class Meta:
        model = OrgNews
        fields = [
            'org_name',
            'title',
            'content',
            'image',
        ]


class NewsConfirmForm(forms.ModelForm):

    class Meta:
        model = OrgNews
        fields = [
            'publish',
        ]


# ::::::::::::::::: ORGS RAPPORT :::::::::::::::::
class RapportForm(forms.ModelForm):

    class Meta:
        model = OrgRapport
        fields = [
            'org_name',
            'title',
            'domain',
            'media',
        ]


class RapportConfirmForm(forms.ModelForm):

    class Meta:
        model = OrgRapport
        fields = [
            'publish',
        ]


class DataForm(forms.ModelForm):

    class Meta:
        model = OrgData
        fields = [
            'org_name',
            'title',
            'media',
        ]


class DataConfirmForm(forms.ModelForm):

    class Meta:
        model = OrgData
        fields = [
            'publish',
        ]


class MediaForm(forms.ModelForm):

    class Meta:
        model = OrgMedia
        fields = [
            'org_name',
            'title',
            'media',
            'url',
        ]


class MediaConfirmForm(forms.ModelForm):

    class Meta:
        model = OrgMedia
        fields = [
            'publish',
        ]


class ResearchForm(forms.ModelForm):

    class Meta:
        model = OrgResearch
        fields = [
            'name_entity',
            'title',
            'domaine',
            'media',
            'url',
        ]


class ResearchConfirmForm(forms.ModelForm):

    class Meta:
        model = OrgResearch
        fields = [
            'publish',
        ]
#:::::::::::::::::org job::::::::::::::::::::::::::::


class OtherOrgsForm(forms.ModelForm):
    class Meta:
        model = OtherOrgs
        fields = [
            'name',
            'logo',
        ]


class JobsForm(forms.ModelForm):

    class Meta:
        model = OrgJob
        fields = [
            'org_name',
            'other_org_name',
            'job_title',
            'job_description',
            'period_months',
            'job_type',
            'experience',
            'position_work',
            'city_work',
            'job_area',
            'job_domain',
            'job_aplay',
            'dead_date',
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city_work'].queryset = City.objects.none()

            if 'position_work' in self.data:
                try:
                    position_work = self.data.get('position_work')
                    self.fields['city_work'].queryset = City.objects.filter(
                        position_work=position_work)
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset

            elif self.instance.pk and self.instance.city_work:
                position_work = self.instance.position_work
                self.fields['city_work'].queryset = City.objects.filter(
                    position_work=position_work)

            elif self.instance.pk and not self.instance.city_work:
                self.fields['city_work'].queryset = City.objects.all()


class JobsConfirmForm(forms.ModelForm):

    class Meta:
        model = OrgJob
        fields = [
            'publish',
        ]


###################funding org opport###############
class FundingForm(forms.ModelForm):

    class Meta:
        model = OrgFundingOpp
        fields = [
            'org_name',
            'name_funding',
            'logo',
            'funding_org_description',
            'work_domain',
            'position_work',
            'city_work',
            'funding_dead_date',
            'funding_period',
            'funding_amounte',
            'funding_description',
            'funding_conditions',
            'funding_reqs',
            'funding_guid',
            'funding_url',
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city_work'].queryset = City.objects.none()

            if 'position_work' in self.data:
                try:
                    position_work = self.data.get('position_work')
                    self.fields['city_work'].queryset = City.objects.filter(
                        position_work=position_work)
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset

            elif self.instance.pk and self.instance.city_work:
                position_work = self.instance.position_work
                self.fields['city_work'].queryset = City.objects.filter(
                    position_work=position_work)

            elif self.instance.pk and not self.instance.city_work:
                self.fields['city_work'].queryset = City.objects.all()


class FundingConfirmForm(forms.ModelForm):

    class Meta:
        model = OrgFundingOpp
        fields = [
            'publish',
        ]


class PersoFunForm(forms.ModelForm):

    class Meta:
        model = PersFundingOpp
        fields = [
            'org_name',
            'name_funding',
            'logo',
            'category',
            'fund_type',
            'study_level',
            'comp_study',
            'domain',
            'position_work',
            'city_work',
            'fund_org_description',
            'funding_dead_date',
            'funding_period',
            'funding_amounte',
            'funding_description',
            'funding_conditions',
            'funding_reqs',
            'funding_guid',
            'funding_url',
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city_work'].queryset = City.objects.none()

            if 'position_work' in self.data:
                try:
                    position_work = self.data.get('position_work')
                    self.fields['city_work'].queryset = City.objects.filter(
                        position_work=position_work)
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset

            elif self.instance.pk and self.instance.city_work:
                position_work = self.instance.position_work
                self.fields['city_work'].queryset = City.objects.filter(
                    position_work=position_work)

            elif self.instance.pk and not self.instance.city_work:
                self.fields['city_work'].queryset = City.objects.all()


class PersoFundConfirmForm(forms.ModelForm):

    class Meta:
        model = PersFundingOpp
        fields = [
            'publish',
        ]


# capacity guid for orgs
class CapacityForm(forms.ModelForm):

    class Meta:
        model = OrgCapacityOpp
        fields = [
            'org_name',
            'name_capacity',
            'title_capacity',
            'capacity_description',
            'capacity_type',
            'position_work',
            'city_work',
            'capacity_domain',
            'capacity_dead_date',
            'capacity_reqs',
            'capacity_guid',
            'capacity_url',
            'publish',
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['city_work'].queryset = City.objects.none()

            if 'position_work' in self.data:
                try:
                    position_work = self.data.get('position_work')
                    self.fields['city_work'].queryset = City.objects.filter(
                        position_work=position_work)
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset

            elif self.instance.pk and self.instance.city_work:
                position_work = self.instance.position_work
                self.fields['city_work'].queryset = City.objects.filter(
                    position_work=position_work)

            elif self.instance.pk and not self.instance.city_work:
                self.fields['city_work'].queryset = City.objects.all()


class CapacityConfirmForm(forms.ModelForm):

    class Meta:
        model = OrgCapacityOpp
        fields = [
            'publish',
        ]
# dev form


class DevForm(forms.ModelForm):

    class Meta:
        model = DevOrgOpp
        fields = [
            'org_name',
            'name_dev',
            'title_dev',
            'dev_date',
            'dev_description',
            'subject',
            'content',
            'video',
        ]
        help_texts = {
            'video': _('رابط يوتيوب فقط'),
            'content': _('صورة أو ملف PDF فقط '),
        }


class DevConfirmForm(forms.ModelForm):

    class Meta:
        model = DevOrgOpp
        fields = [
            'publish',
        ]


class NewsLetterForm(forms.ModelForm):
    name = forms.CharField(max_length=255, min_length=3, label='',
                           help_text=_(
                               ''),
                           widget=forms.TextInput(
                               attrs={'placeholder': _('الاسم و الكنية')}))
    work = forms.CharField(max_length=255, min_length=3, label='',
                           help_text=_(
                               ''),
                           widget=forms.TextInput(
                               attrs={'placeholder': _('العمل')}))

    org_name = forms.CharField(max_length=255, min_length=3, label='',
                               help_text=_(
                                   ''),
                               widget=forms.TextInput(
                                   attrs={'placeholder': _('اسم المنظمة')}))

    email = forms.EmailField(max_length=255, min_length=3, label='',
                             help_text=_(
                                 ''),
                             widget=forms.EmailInput(
                                 attrs={'placeholder': _('البريد الاكتروني')}))

    class Meta:
        model = NewsLetter
        fields = [
            'name',
            'work',
            'org_name',
            'email',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = NewsLetter.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError(
                _('هذا البريد الالكتروني موجود مسبقاً'))
            # raise alert(text=_('This email already exists'),
            #             title='', button='OK')

        return email

    # def salut(self, *args, **kwargs):
    #     salut = self.cleaned_data.get('name')
    #     print(salut)
    #     return salut


class FriendInviteForm(forms.ModelForm):

    class Meta:
        model = Invitation
        fields = [
            'name',
            'email',
        ]
