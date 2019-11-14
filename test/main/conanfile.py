from conans import ConanFile, tools
import os


class Recipe(ConanFile):
    name = "issue"
    version = "testing"
    scm = {"type": "git", "url": "auto", "revision": "auto"}

    def source(self):
        file_root = os.path.join(self.source_folder, "file_root.txt")
        file_test = os.path.join(self.source_folder, "test", "file_test.txt")
        file_conanfile = os.path.join(self.source_folder, "test", "main", "file_conanfile.txt")

        print("{}: {}".format(file_root, os.path.exists(file_root)))
        print("{}: {}".format(file_test, os.path.exists(file_test)))
        print("{}: {}".format(file_conanfile, os.path.exists(file_conanfile)))
