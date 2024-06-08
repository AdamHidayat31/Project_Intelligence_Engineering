from django import forms
from .models import IE, IntExp, IntImp, Kendala, Status, PerImp

STATUS = (
    ('', 'Choose...'),
    ('S','Selesai'),
    ('B','Berlangsung'),
    ('G','Gagal')
)

class IEForm(forms.ModelForm):
    status_penyelesaian =forms.ChoiceField(choices=STATUS)

    class Meta:
        model = IE
        fields = '__all__'
        labels = {
            'organization_objective': 'Organization Objective',
            'leading_indicator':'Leading Indicator',
            'user_outcomes':'User Outcomes',
            'model_properties':'Model Properties',
            'tanggal_mulai':'Tanggal Mulai',
            'tanggal_selesai':'Tanggal Selesai',
            'status_penyelesaian':'Status Penyelesaian'
        }
        widgets={
            'organization_objective': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'leading_indicator': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'user_outcomes': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'model_properties': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'tanggal_mulai': forms.TextInput(attrs={'placeholder':'yyyy-mm-dd'}),
            'tanggal_selesai': forms.TextInput(attrs={'placeholder':'yyyy-mm-dd'})
        }

class IntExpForm(forms.ModelForm):
    class Meta:
        model = IntExp
        fields = '__all__'
        labels = {
            'achieve_system':'Achieve System Objective',
            'minimize_flaws':'Minimize Intelligence Flaws',
            'data_grown_system':'Create Data to Grown Sytem',
        }
        widgets = {
            'automate': forms.Textarea(attrs={'style':'height:80px '}),
            'prompt': forms.Textarea(attrs={'style':'height:80px '}),
            'organization': forms.Textarea(attrs={'style':'height:80px '}),
            'annotate': forms.Textarea(attrs={'style':'height:80px '}),
            'achieve_system': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'minimize_flaws': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'data_grown_system': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
        }

class IntImpForm(forms.ModelForm):
    class Meta:
        model = IntImp
        fields = '__all__'
        labels = {
            'proses_bisnis':'Proses Bisnis Sistem Cerdas',
            'teknologi_dipakai':'Teknologi Yang Akan di Pakai',
            'sistem_cerdas':'Proses Yang Akan di Bangun Menjadi Cerdas',
        }
        widgets = {
            'proses_bisnis': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'teknologi_dipakai': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'sistem_cerdas': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
        }

class KendalaForm(forms.ModelForm):
    class Meta:
        model = Kendala
        fields = '__all__'
        labels = {
            'masalah_pengembangan': 'Kendala atau Masalah Pengembangan Sistem',
        }
        widgets = {
            'masalah_pengembangan': forms.Textarea(attrs={'placeholder': 'Masukan Kendala atau Masalah Pengembangan Sistem',
                                                          'style': 'width:100% ; height:80px '}),
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        labels = {
            'status':'Status Realisasi'
        }
        widgets = {
            'status': forms.Textarea(attrs={'placeholder': 'Masukan Perkembangan Sistem Cerdas',
                                                          'style': 'width:100% ; height:80px '}),
        }

class PerImpForm(forms.ModelForm):
    class Meta:
        model = PerImp
        fields = '__all__'
        labels = {
            'pelaksanaan_deployment':'Penetapan Pelaksanaan Deployment',
            'pemeliharaan_sistem':'Pemeliharaan Sistem Cerdas',
            'pelaksanaan_operasi':'Pelaksanaan Operasi Sistem Cerdas',
        }
        widgets = {
            'pelaksanaan_deployment': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'pemeliharaan_sistem': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
            'pelaksanaan_operasi': forms.Textarea(attrs={'style': 'width:100% ; height:80px '}),
        }
