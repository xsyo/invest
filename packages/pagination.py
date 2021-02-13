from rest_framework.pagination import CursorPagination



class JournalPagination(CursorPagination):
    page_size = 5
    ordering = ['-date', '-id']