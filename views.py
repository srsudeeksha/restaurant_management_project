from rest_framework.generics import CreateAPIView
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer

class ContactFormSubmissionCreateView(CreateAPIView):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer