import click
import os

file_types: dict = {1: "page", 2: "models/", 3: "components/", 4: "assets", 5: "helper", 6: "state_management/"}


def create_file(file_type: int):
    file_typ: str = file_types.get(file_type)
    file_name: str = file_typ.rstrip(file_typ[-1])
    if not file_typ.endswith("/"):
        click.secho("----------------------------------------------------------------------", fg="magenta")
        click.echo(f"creating file {file_typ}")
        try:
            with open(f"{file_typ}.dart", 'w') as file:
                file.write(f"// TODO: your {file_typ} classes should be here")
        except Exception as e:
            raise click.ClickException(f"{e}")
    else:
        click.echo(f"creating folder {file_typ}")
        try:
            os.mkdir(file_typ)
        except Exception as e:
            raise click.ClickException(f"{e}")

        with open(f"{file_typ}/{file_name}.dart", 'w') as file:
            file.write(f"// TODO: your {file_name} classes should be here")


def create_multiple():
    for key in file_types.keys():
        try:
            create_file(key)
            click.secho(f"{file_types.get(key)} created successfully", fg="cyan")
            click.secho("----------------------------------------------------------------------", fg="magenta")
        except Exception as e:
            raise click.ClickException(f"{e}")
