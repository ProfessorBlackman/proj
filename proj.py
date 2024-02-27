import click

import proj_in
import proj_out


@click.command(name="proj")
@click.argument("s")
@click.option("--feat", default="", help="Name of the feature")
@click.option("--path", default="", help="Path to project")
def proj(s, feat, path):
    click.echo("----------------------------------------------------------------------")
    click.secho("Welcome to proj. A tool for creating feature folders in flutter. (similar to django apps)", fg="blue")
    click.echo(f"you chose {s}")
    if feat == "":
        click.prompt("Enter the feature", type=str)
    if s == "in":
        try:
            proj_in.proj_in(feature_name=feat)
        except Exception as e:
            raise click.ClickException(f"${e}")
    elif s == "out":
        if path == "":
            click.prompt("Enter the project's path", type=str)
        try:
            proj_out.proj_out(feature_name=feat, project_path=path)
        except Exception as e:
            raise click.ClickException(f"${e}")
    else:
        raise click.ClickException("argument can only be 'in' or 'out'")

    click.secho("----------------------------------------------------------------------")

    click.secho(f"feature {feat} created successfully", fg="green")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    proj()
