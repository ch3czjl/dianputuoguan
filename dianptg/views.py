from django.shortcuts import render
from django.views.generic import FormView, RedirectView
from .forms import bangdingForm

# Create your views here.
def post_list(request):
    return render(request, "post_list.html", {})

class bangdingview(FormView):
    form_class = bangdingForm
    template_name = 'dianptg/paimaipin.html'
    def form_valid(self, form):
        if form.is_valid():
            user = form.save(False)
            user.is_active = False
            user.source = 'Register'
            user.save(True)
            site = get_current_site().domain
            sign = get_md5(get_md5(settings.SECRET_KEY + str(user.id)))

            if settings.DEBUG:
                site = '127.0.0.1:8000'
            path = reverse('account:result')
            url = "http://{site}{path}?type=validation&id={id}&sign={sign}".format(
                site=site, path=path, id=user.id, sign=sign)

            content = """
                            <p>请点击下面链接验证您的邮箱</p>

                            <a href="{url}" rel="bookmark">{url}</a>

                            再次感谢您！
                            <br />
                            如果上面链接无法打开，请将此链接复制至浏览器。
                            {url}
                            """.format(url=url)
            send_email(
                emailto=[
                    user.email,
                ],
                title='验证您的电子邮箱',
                content=content)

            url = reverse('accounts:result') + \
                '?type=register&id=' + str(user.id)
            return HttpResponseRedirect(url)
        else:
            return self.render_to_response({
                'form': form
            })