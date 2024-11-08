class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        newline = "\n"
        return (
            f"Name: {self.name}" 
            f"\nDescription: {self.description or '-'}" 
            f"\nLicense: {self.license}" 
            f"\n"
            f"\nAuthors:\n"
            f"{newline.join(f'- {key}' for key in self.authors)}"+
            f"\n"
            f"\nDependencies:\n" +
            f"{newline.join(f'- {key}' for key, value in self.dependencies.items())}" +
            f"\n"
            f"\nDevelopment dependencies:\n" +
            f"{newline.join(f'- {key}' for key, value in self.dev_dependencies.items())}"
        )
