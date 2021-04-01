from django.shortcuts import render

def home(request): #запрос
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reverse_text = user_text[::-1]
	user_text_len = len(user_text.split())
	print(user_text_len)
	return render(request, 'reverse.html', {'usertext':user_text,
		'reversedtext': reverse_text, 'text_len': user_text_len})
