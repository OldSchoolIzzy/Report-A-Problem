from django import forms


# class TicketForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = ['location', 'room', 'issue', 'proximity', 'image', 'comments', 'ticket_id']
#
#     location = forms.ChoiceField(choices=[('location1', 'Location 1'), ('location2', 'Location 2')])
#     room = forms.ChoiceField(choices=[('room1', 'Room 1'), ('room2', 'Room 2')])
#     issue = forms.ChoiceField(choices=[('issue1', 'Issue 1'), ('issue2', 'Issue 2')])
#     proximity = forms.CharField(max_length=100)
#     image = forms.ImageField()
#     comments = forms.CharField(widget=forms.Textarea)
#     ticket_id = forms.IntegerField()