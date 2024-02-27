import os

import click

import helper


def proj_in(feature_name: str):
    current_dir = os.getcwd()
    click.echo(f"current_dir: {current_dir}")

    if not current_dir.endswith("/lib"):
        current_dir = os.path.join(current_dir, "lib")
        try:
            os.chdir(current_dir)
        except Exception as e:
            raise click.ClickException(f"{e}")
        click.echo("Switched to /lib dir")

    feature_dir = os.path.join(current_dir, feature_name)
    click.echo(f"path to feature: {feature_dir}")

    os.mkdir(feature_dir)

    os.chdir(feature_dir)
    helper.create_multiple()
