from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data() #ctxtは任意だがよく使われる
        ctxt["username"] = "kazuki"
        return ctxt
    

class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data() #ctxtは任意だがよく使われる
        ctxt["num_services"] = 12345678
        ctxt["skills"] = [
            "Python",
            "C++",
            "Java",
            "Go",
            ]
        return ctxt