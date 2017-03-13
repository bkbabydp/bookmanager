# -*- coding: UTF-8 -*-


from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpRequest, Http404

import requests
from urllib.parse import urlencode
from pyquery import PyQuery as jQ

from .models import Book


# Create your views here.

def index(request):
    """

    :param request:
    :type request: HttpRequest
    :return:
    """
    keyword = request.GET.get('q', None)
    page = int(request.GET.get('page', 1))
    if keyword:
        init = False
        # try:
        #     books = Book.objects.get(name=keyword)
        #     message = '以下是搜索结果：'
        # except Book.DoesNotExist:
        #     books = None
        #     message = '啊，这本书估计还在火星！'
        count = 20
        start = count * (page - 1)
        query = urlencode(
            query={
                'q': keyword,
                'start': start,
                'count': count
            }
        )
        url = 'https://api.douban.com/v2/book/search?%s' % query
        result = requests.get(url)

        if result and result.status_code == 200:
            warning = ''

            data = result.json()
            total = data.get('total', 0)
            print(total)

            books = data.get('books', None)
            if total > 100:
                warning = '搜索结果过多，仅显示前100条，请调整关键字精准搜索！'
                total = 100
            paginator = Paginator(range(total), count)

            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)
        else:
            warning = '啊，这本书估计还在火星！'
            pages, books = None, None

            # jq = jQ(url='https://read.douban.com/search?q=%s' % keyword, method='get')
            # for i in jq.items('.item'):

    else:
        init = True
        pages, books = None, None

    context = {
        'init': init,
        'pages': pages,
        'books': books,
        'keyword': keyword,
        'warning': warning,
    }

    return render(request=request, template_name='search.html', context=context)
