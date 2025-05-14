from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import UploadedFile
from .serializers import UploadedFileSerializer
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from .models import UploadedFile
import os

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role != 'operation':
            return Response({"error": "Only Operation users can upload files."}, status=403)
        
        serializer = UploadedFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Upload successful."})
        return Response(serializer.errors, status=400)
    
    
class FileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'client':
            return Response({"error": "Only Clients can view files."}, status=403)

        files = UploadedFile.objects.all()
        file_links = [
            {
                "download_link": "http://localhost:8000/api/files/download-file/"+ str(f.assignment_id) +"/"
            }
            for f in files
        ]
        return Response({"files": file_links, "message": "success"})
    
    


class FileDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, uuid):
        assignment = get_object_or_404(UploadedFile, assignment_id=uuid)

        file_path = assignment.file.path

        if not os.path.exists(file_path):
            raise Http404("File not found.")

        file_name = os.path.basename(file_path)

        # File will be downloaded with original name
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
        return response