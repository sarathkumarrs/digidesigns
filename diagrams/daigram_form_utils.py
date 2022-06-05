from users.form_utils import FormUtils


class DiagramFormUtils(FormUtils):
    def save_process_datas(self, module_instance):
        print("On saving")
        if self.form.is_valid():
            print("From vaild")
            data = self.form.save(commit=False)
            data.module = module_instance
            data.save()
            return {"status": True, "message": "Created"}
        else:
            return {"status": False, "message": self.form.errors}

    def save_module_datas(self, project_instance):
        print("On saving")
        if self.form.is_valid():
            print("From vaild")
            data = self.form.save(commit=False)
            data.project = project_instance
            data.save()
            return {"status": True, "message": "Created"}
        else:
            return {"status": False, "message": self.form.errors}
