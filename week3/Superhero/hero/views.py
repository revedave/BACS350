from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class SpiderView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider-Man',
            'body': 'Aah! Whoa. Whoa. Whoa. Please dont put your eggs in me!',
            'image': '/static/images/spider-man.jpg'
        }


class AntView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Ant-Man',
            'body': 'Does anyone have any orange slices?',
            'image': '/static/images/ant-man.jpg'
        }


class ThorView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Thor',
            'body': 'By Odins beard, you shall not cut my hair, lest you feel the wrath of the mighty Thor! Please! Please kind sir, do not cut my hair! No! Nooo!',
            'image': '/static/images/black_widow.jpg'
        }