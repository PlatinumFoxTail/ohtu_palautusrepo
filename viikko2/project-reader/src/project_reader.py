from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        #print("Tiedoston sisältö:")
        #print(content)

        parsed_data = toml.loads(content)
        #print("Deserialisoitu sisältö:")
        #print(parsed_data)

        name = parsed_data["tool"]["poetry"]["name"]
        description = parsed_data["tool"]["poetry"]["description"]
        license = parsed_data["tool"]["poetry"]["license"]
        authors = parsed_data["tool"]["poetry"]["authors"]
        dependencies = parsed_data["tool"]["poetry"]["dependencies"]

        dev_dependencies = parsed_data["tool"]["poetry"]["group"]["dev"]["dependencies"]

        authors_list = ["- " + author for author in authors]
        dependency_list = ["- " + dep for dep in dependencies.keys()]
        dev_dependency_list = ["- " + dep for dep in dev_dependencies.keys()]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])

        project_string = f"Name: {name}\nDescription: {description}\nLicense: {license}\n\nAuthors:\n"
        project_string += "\n".join(authors_list) + "\n\nDependencies:\n" + "\n".join(dependency_list)
        project_string += "\n\nDevelopment dependencies:\n" + "\n".join(dev_dependency_list)

        return project_string