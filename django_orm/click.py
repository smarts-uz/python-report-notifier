import click

all = []


@click.command()
@click.argument("keyword", type=str)
def add_keyword(keyword):
    all.append(keyword)
    click.echo(f'Keyword : {keyword} successfully created!!')
    print(all)
