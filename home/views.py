from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import AbstractForm, AuthorForm

# Create your views here.
def index(request):
    abstract_form = AbstractForm(prefix="abstract_form")
    author_form = AuthorForm(prefix="author_form")
    context_dict = {"abstract_form": abstract_form, "author_form": author_form}
    return render(request, 'home/index.html', context_dict) 


def submit_abstract(request):
    # handle post
    if request.method == "POST":
        abstract_form = AbstractForm(request.POST, prefix="abstract_form")
        author_form = AuthorForm(request.POST, prefix="author_form")

        if abstract_form.is_valid() and author_form.is_valid():
            # form is valid, save to database
            abstract = abstract_form.save(commit=False)

            # word limit
            num_words = len(abstract.abstract_text.split())
            if num_words <= 300:
                abstract.save()
                author = author_form.save(commit=False)
                author.abstract = abstract
                author.save()

                # send confirmation email
                subject = 'SABPA Poster Contest 2018: Abstract Confirmation'
                html_content = "<p>Dear " + author.first_name + "," +\
                    "<p>Congratulations! Your&nbsp;abstract has been successfully submitted " +\
                    "to the 2nd SABPA Life Science and Technology Poster Contest. " +\
                    "Please reply to this email if you need any assistance.</p>" +\
                    "<p>Sincerely,</p><p>SABPA Poster Contest Team</p>"
                from_email = "sabpa.poster@gmail.com"
                to = author.email
                msg = EmailMessage(subject, html_content, from_email, [to])
                msg.content_subtype = "html"
                msg.send()

                return HttpResponseRedirect(reverse('home:submission_success'))

        # word limit failed
        return HttpResponseRedirect(reverse('home:submission_fail'))


def submission_success(request):
    # return html code to tell the user that the submission is successful 
    return render(request, 'home/submission_success.html')

def submission_fail(request):
    # return html code to tell the user that the submission is failed 
    return render(request, 'home/submission_fail.html')


