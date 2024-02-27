import os

import click

import helper


def proj_out(feature_name: str, project_path: str):
    click.echo(f"current_dir: {os.getcwd()}")
    if not project_path.endswith("/lib"):
        project_path = os.path.join(project_path, "lib")
    try:
        os.chdir(project_path)
    except Exception as e:
        raise click.ClickException(f"{e}")
    click.echo("Switched to /lib dir")

    feature_dir = os.path.join(project_path, feature_name)
    click.echo(f"path to feature: {feature_dir}")

    os.mkdir(feature_dir)

    os.chdir(feature_dir)
    helper.create_multiple()
