from cProfile import label
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Blood_Request, User, email_id

class RegisterForm(UserCreationForm):
	# The form for recieving the data for authentication details (phone_no and password)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password1'].widget.attrs.update({ 
			'placeholder' : 'Password',
			'class' : 'form-control',
		})
		self.fields['password2'].widget.attrs.update({
			'placeholder' : 'Repeat Password',
			'class' : 'form-control',
		})
		
	class Meta:
		model = User
		fields = ['email', 'full_name', 'address', 'height', 'weight', 'phn_no', 'pincode', 'blood_group', 'gender']
		widgets = {
			'email' : forms.EmailInput(attrs={
				'placeholder' : 'Email',
				'class' : 'form-control',
			}),
			'full_name' : forms.TextInput(attrs={
				'placeholder' : 'Full Name',
				'class' : 'form-control',
			}),
			'address' : forms.TextInput(attrs={
				'placeholder' : 'Address',
				'class' : 'form-control',
			}),
            'height' : forms.NumberInput(attrs={
				'placeholder' : 'Height',
				'class' : 'form-control',
			}),
            'weight' : forms.NumberInput(attrs={
				'placeholder' : 'Weight',
				'class' : 'form-control',
			}),
            'phn_no' : forms.NumberInput(attrs={
				'placeholder' : 'Phone Number',
				'class' : 'form-control',
			}),
            'pincode' : forms.NumberInput(attrs={
				'placeholder' : 'Pincode',
				'class' : 'form-control',
			}),
            'blood_group' : forms.RadioSelect(attrs={
				'class' : 'form-check-input',
			}),
            'gender' : forms.RadioSelect(attrs={
				'class' : 'form-check-input',
			}),

		}
class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({
			'placeholder' : 'Email',
			'class' : 'form-control',
		})
		self.fields['password'].widget.attrs.update({
			'placeholder' : 'Password',
			'class' : 'form-control',
		})
	
class BloodForm(forms.ModelForm):
	class Meta:
		model = Blood_Request
		fields = ['p_name', 'p_hospitalname', 'p_bystander', 'p_unit', 'p_phn_number', 'p_bloodneed', 'p_bloodgroup', 'p_gender']
		widgets = {
			'p_name' : forms.TextInput(attrs={
				'placeholder' : 'Patient name',
				'class' : 'form-control',
			}),
			'p_hospitalname' : forms.TextInput(attrs={
				'placeholder' : 'Hospital name',
				'class' : 'form-control',
			}),
			'p_bloodneed' : forms.TextInput(attrs={
				'placeholder' : 'Hospital name',
				'class' : 'form-control',
			}),
			'p_bystander' : forms.TextInput(attrs={
				'placeholder' : 'Bystander details',
				'class' : 'form-control',
			}),
            'p_unit' : forms.NumberInput(attrs={
				'placeholder' : 'Number of units of blood',
				'class' : 'form-control',
			}),
            'p_phn_number' : forms.NumberInput(attrs={
				'placeholder' : 'Phone Number',
				'class' : 'form-control',
			}),
            'pincode' : forms.NumberInput(attrs={
				'placeholder' : 'Pincode',
				'class' : 'form-control',
			}),
            'blood_group' : forms.RadioSelect(attrs={
				'class' : 'form-check-input',
			}),
            'gender' : forms.RadioSelect(attrs={
				'class' : 'form-check-input',
			}),
			
		}

		labels = {
			'p_name' : 'Patient name', 
			'p_hospitalname' : 'Hospital name',
			'p_bystander' : 'Bystander details', 
			'p_unit' : 'Units of blood required', 
			'p_phn_number' : 'Contact number', 
			'p_bloodneed' : 'Purpose for  blood', 
			'p_bloodgroup' : 'Blood group', 
			'p_gender' : 'Gender'
		}		