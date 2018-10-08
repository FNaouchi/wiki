from django.shortcuts import render
import .models import Page
# Create your views here.

def page_list(request):
	context = {
		"pages" : Page.object.all()
		}
	return render(request, 'list.html', context)


def page_detail(request, page_id):
	context = {
		"page" : Page.object.get(id = page_id)
		}
	return render(request, 'detail.html', context)