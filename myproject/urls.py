from django.contrib import admin
from django.urls import path
from notes import views
from accounts import views as accounts_views # Avoiding conflict
urlpatterns = [
   path('admin/', admin.site.urls),
   path('signup/', accounts_views.sign_up,
       name='signup'), # <= sign up route
   path('logout/', accounts_views.log_out,
       name='logout'), # <= log out route
   path('login/', accounts_views.log_in,
       name='login'), # <= log in route
   path('notes/', views.home,
       name='notes'),  # <=notes_home
   path('items/<int:id>/', views.notes_view,
       name='items'),# <=items_page
   path('update/<int:id>/', views.update_note,
       name='update'),# <=update note
   path('delete/<int:id>/', views.delete_note,
      name='delete'),# <=delete note
 ]
