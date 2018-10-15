from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict
from django_filters import rest_framework as rest_framework_filters
from django.db import models

class Pager (pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "per_page"
    max_page_size = 50
    per_page = page_size

    # Untuk dapetin query-per-page dari request
    def paginate_queryset(self, queryset, request, view=None):
        val = request.GET.get(self.page_size_query_param)
        if val :
            val = int(val)
            if val != self.per_page and val > 0 and val <= self.max_page_size :
                self.per_page = val
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        total = self.page.paginator.count
        per_page = total if self.per_page > total else self.per_page
        if per_page == 0 : per_page = 1
        total_page = total/per_page
        str_total_page = (str(total_page)).split('.')[1]

        last_page = int(total_page)
        if int(str_total_page) > 0 : last_page += 1

        start_from = 1 + (self.page.number * per_page) - per_page
        if start_from < 1 : start_from = 1

        end_at = (start_from + per_page) - 1
        if end_at > total : end_at = total

        if per_page >= total:
            start_from = 1
            end_at = total

        return Response(OrderedDict([
            ('total', total),
            ('per_page', per_page),
            ('current_page', self.page.number),
            ('last_page', last_page),
            ('next_page_url', self.get_next_link()),
            ('prev_page_url', self.get_previous_link()),
            ('from', start_from),
            ('to', end_at),
            ('data', data)
        ]))


class BaseDjangoFilter(rest_framework_filters.FilterSet):
    text_column = ()
    id_column = 'id'
    filterlist = []

    def filter_queryset(self, request, queryset, view):
        req = request.GET
        if req.get(self.id_column) is None :
            return self.doFilter(req, self.text_column, queryset)
        else :
            myFilter = queryset.filter(id=req[self.id_column])
        return myFilter

    def doFilter(self, request, params, queryset):
        filterlist = self.filterlist
        filterlist.clear()
        for param in params :
            value = request.get(param)
            if value :
                filterkey = {f"{param}__icontains" : value}
                if filterlist :
                    filterlist.append(filterlist[-1].filter(**filterkey))
                else :
                    filterlist.append(queryset.filter(**filterkey))

        if len(filterlist) > 0 :
            finalfilter = filterlist[-1]
        else :
            finalfilter = queryset.filter()
        filterlist.clear()
        return finalfilter


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
