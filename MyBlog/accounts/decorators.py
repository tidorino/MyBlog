# from django.shortcuts import render
#
#
# def allow_groups(groups=None):
#     if groups is None:
#         groups = []
#
#     def decorator(view_func):
#         def wrapper(request, *args, **kwargs):
#
#             if request.user.is_superuser:
#                 return view_func(request, *args, **kwargs)
#
#             user_groups = request.user.groups.filter(name__in=groups)
#
#             if user_groups or request.user.is_superuser:
#                 return render(request, 'my_blog/home-page.html')
#             else:
#                 return render(request, 'my_blog/all_post_list.html')
#
#         return wrapper
#
#     if callable(groups):
#         func = groups
#         groups = []
#         return decorator(func)
#
#     return decorator
