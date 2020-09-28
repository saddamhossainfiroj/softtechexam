# from django import template
# import datetime
# from django.utils.dateparse import parse_date
# from hr.models import UserPrivilege
# register = template.Library()

# @register.simple_tag
# def variable_assign_tag(val=None):
#     return val

# @register.filter(name='menu_list')
# def menu_list_load(employee_id):
#     data_list = UserPrivilege.objects.filter(user_id = employee_id).order_by('menu_id__menu_for','menu_id__module_order','menu_id__menu_order')
#     for data in data_list:
#         print(data.menu,data.menu.get_menu_for_display(), data.menu.module_order)
#     if data_list: return data_list    
#     else:return None

# @register.filter(name='module_list')
# def module_load(employee_id):
#     modules = UserPrivilege.objects.raw('select uac.id, menu.module_name as module_name, menu.menu_icon as menu_icon from hr_user_access_control uac inner join hr_menu_list menu on menu.id = uac.menu_id where uac.status = true and uac.employee_id = %s group by menu.module_name', [employee_id])
#     if modules: return modules    
#     else:return None
