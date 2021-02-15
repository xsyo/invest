from rest_framework.pagination import CursorPagination



class TransactionPagination(CursorPagination):
    page_size = 5
    ordering = ['-updated_at', '-created_at', '-id']