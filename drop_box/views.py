from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from google.cloud import storage
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drives_data.serializers import UserSerializer
from drives_data.tasks import data_syscronization
from google_drive.models import User
from social_drive import constants
import dropbox

from drives_data.models import DrivesData


class DropBoxHome(APIView):
    login_url = '/login/'
    template_name = 'dropbox_home.html'
    permission_class = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        # user = User.objects.filter(id=request.user.id).first()
        # if user.dropbox_access_token:
        #     list_of_files = DrivesData.objects.filter(drive_type=DrivesData.DROPBOX, user=request.user)
            # dbx = dropbox.Dropbox(user.dropbox_access_token)
            # account_info=dbx.users_get_current_account()
            # total_files=dbx.file_requests_count()
            # list_of_files=dbx.files_list_folder('').entries

            # return render(request, self.template_name,
            #               {'list_of_files': list_of_files, 'drive_type': DrivesData.DROPBOX})
        return Response(constants.DOPBOX_CONNECT)


class DropBoxReturnURLView(View):
    template_name = 'drop_box_connect.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SaveDropboxDataView(APIView):
    permission_class = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        if request.user.dropbox_access_token:
            # storage_client = storage.Client()
            # bucket_list = storage_client.list_buckets()
            # print(bucket_list)
            data_syscronization(DrivesData.DROPBOX, request.user.email)
        return JsonResponse({'msg': 'You are connected'})



class UpdateDropBoxCredentialsView(APIView):
    permission_class = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        token = request.GET.get('access_token')
        # token = request.get_full_path()
        # url, token = token.split('/update_drpbox_credentials/?')
        if token:
            user = User.objects.filter(id=request.user.id).first()
            user.dropbox_access_token = token
            user.save()
            data_syscronization(DrivesData.DROPBOX, user.email)
        return JsonResponse({'msg': 'You are connected'})
