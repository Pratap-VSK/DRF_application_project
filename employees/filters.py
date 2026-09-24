import django_filters
from .models import Employee

class Employeefilter(django_filters.filterset):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range' lable='from EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range' lable='To EMP ID')

    class meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id_min', 'id_max']

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id_gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id_lte=value)
        return queryset
