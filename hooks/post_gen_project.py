#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def rename_file(from_path, to_path):
    os.rename(os.path.join(PROJECT_DIRECTORY, from_path),
              os.path.join(PROJECT_DIRECTORY, to_path))

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.use_pytest }}' == 'y':
        remove_file('tests/__init__.py')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        click_file = os.path.join('{{ cookiecutter.project_slug }}', 'click_cli.py')
        remove_file(click_file)
        argp_file = os.path.join('{{ cookiecutter.project_slug }}', 'argp_cli.py')
        remove_file(argp_file)
    elsif '{{ cookiecutter.command_line_interface|lower }}' == 'argparse':
        click_file = os.path.join('{{ cookiecutter.project_slug }}', 'click_cli.py')
        remove_file(click_file)
        argp_file = os.path.join('{{ cookiecutter.project_slug }}', 'argp_cli.py')
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        rename(argp_file, cli_file)
    elsif '{{ cookiecutter.command_line_interface|lower }}' == 'click':
        argp_file = os.path.join('{{ cookiecutter.project_slug }}', 'argp_cli.py')
        remove_file(argp_file)
        click_file = os.path.join('{{ cookiecutter.project_slug }}', 'click_cli.py')
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        rename(click_file, cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
