from diagrams.models import Module, Process, Project


class DiagramUtils:
    def __init__(self, id=None, request=None):
        self.id = id
        self.request = request

    @staticmethod
    def get_all_projects():
        return Project.objects.all()

    def get_project_of_user(self):
        return Project.objects.filter(creator=self.request.user)

    @staticmethod
    def get_all_modules(pk):
        return Module.objects.filter(project__id=pk)

    @staticmethod
    def get_all_modules_of_process(module_id):
        return Process.objects.filter(module=module_id)

    @staticmethod
    def get_module_instance_by_id(module_id):
        return Module.objects.get(id=module_id)

    @staticmethod
    def get_project_instance_by_id(module_id):
        return Project.objects.get(id=module_id)
