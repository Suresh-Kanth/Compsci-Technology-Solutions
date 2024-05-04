from django.contrib import admin
from home.models import Employee
import river_admin
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.
def create_river_button(obj, transition_approval):
    approve_Employee_url = reverse('approve_Employee', kwargs={'Employee_id': obj.pk, 'next_state_id': transition_approval.transition.destination_state.pk})
    return f"""
        <input
            type="button"
            style="margin:2px;2px;2px;2px;"
            value="{transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}"
            onclick="location.href=\'{approve_Employee_url}\'"
        />
    """
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('no', 'firstname', 'lastname', 'email','dob','phone_number','address','Aadhar_number','pan_number','my_state_field', 'river_actions')

    def get_list_display(self, request):
        self.user = request.user
        return super(EmployeeAdmin, self).get_list_display(request)

    def river_actions(self, obj):
        content = ""
        for transition_approval in obj.river.status.get_available_approvals(as_user=self.user):
            content += create_river_button(obj, transition_approval)

        return mark_safe(content)
        
admin.site.register(Employee,EmployeeAdmin)

class EmployeeRiverAdmin(river_admin.RiverAdmin):
    name = "Issue Tracking Flow"
    icon = "mdi-employee-account"
    list_displays = ['pk', 'no', 'firstname', 'lastname', 'email','dob','phone_number','address','Aadhar_number','pan_number','my_state_field']


river_admin.site.register(Employee, "status", EmployeeAdmin)