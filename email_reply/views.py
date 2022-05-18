from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from Mailserver.settings import EMAIL_HOST_USER


@csrf_exempt
def portfolio_mail_reply(request):
    if request.method == "POST":
        form_name = request.POST['form_name']
        form_email = request.POST['form_email']
        form_message = request.POST['form_message']
        message = "Thanks " + form_name + "  visiting my website. I got your response and will reach out to you " \
                                          "soon. :) "
        print("sending email")
        send_mail(
            form_name,
            message,
            EMAIL_HOST_USER,
            [form_email],
            fail_silently=False,
        )
        send_mail(
            form_name,
            "Here is a response from portfolio: \n \n" + form_message,
            EMAIL_HOST_USER,
            [EMAIL_HOST_USER],
            fail_silently=False,
        )

    return HttpResponse("Email sent successfully")
    # message_name = request


def celeryTest(request):
    return HttpResponse('Done')

# Create your views here.
