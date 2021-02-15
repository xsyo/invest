from rest_framework.pagination import CursorPagination



class UserPagination(CursorPagination):
    page_size = 5
    ordering = ['-date_joined', '-id']